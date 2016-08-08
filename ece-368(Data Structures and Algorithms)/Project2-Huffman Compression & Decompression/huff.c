#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "huff.h"


int main(int argc, char * * argv)
{
  int flag1=1; //indicates that the first node has been created and that head should be preserved 
  int flag2=0; //indicates that the consequential node has been created and the list should be linked
  int ctr=0;  //ctr variables
  int ctr1=0; //^
  int ctr2=0; //^
  int i=0;  //^
  char *str = malloc(1000*sizeof(char)); //free at the end
  size_t size=1000; //max number of chacracters read from the input file at once
  char *filename = argv[1]; //input file name
  FILE *fptr = fopen(filename,"r");
  FILE *out; //output file ptr
  int c[256]={0}; //Stores the chars read from input file here
  int val[256]={0}; //Stores the chars' frequencies here  (Could've just used one array also)
  Node *head=NULL;
  Node *prev=NULL;
  Node *treenode=NULL;
  Node *tree = NULL; //huffman tree
  char *str1=malloc(sizeof(char*));  //free at the end
  char **codes = malloc(256*sizeof(char*));  //free at the end
  char *byte = malloc(sizeof(char*)); //Byte used to write to the output file,  //free at the end

  //mallocing memory for individual blocks of the array that will store binary codes
  for(i=0;i<256;i++)
    {
      codes[i] = malloc(sizeof(char*));
    }


  //Reading file, counting characters and making character-frequency table
  while(fgets(str,size,fptr) != NULL)
    {
      while(*(str+ctr) != '\n' && *(str+ctr) != '\0') //to stop when newline is encountered and to exclude null 
	{
	  c[(int)*(str+ctr)]=(*(str+ctr));
	  val[(int)*(str+ctr)]= val[(int)*(str+ctr)] + 1;
	  ctr++;
	}
      if(*(str+ctr) == '\n' || *(str+ctr) == '\0')
	{
	  c[(int)*(str+ctr)]=(*(str+ctr));
	  val[(int)*(str+ctr)]= val[(int)*(str+ctr)] + 1;
	}
	    ctr=0;
    }  
  fclose(fptr); //Closing file for now; Reopened later when we write compressed characters to the output file


  //Making linked list from character frequency table
  for(ctr=0 ;ctr<256;ctr++)
    {
      if(c[ctr]!=0)
	{
	  ctr1 = findsmallest(val);
	  treenode = createNode(c[ctr1],val[ctr1]);
	  val[ctr1]=0; //removing the smallest value from the frequency array by making it 0
	  if(flag2==1)
	    {
	      prev->next=treenode; //linking the list
	      prev=prev->next;
	    }
	  if(flag1==1)
	    {
	      head=treenode; //preserving head node
	      prev=head; //assigning the head node to prev so that the nodes can be linked
	      flag1=0;
	      flag2=1;
	    }
	  ctr2++; //number of nodes in the linked list
	}
    }

  treenode=head; //reassigning the head of the linked list to treenode

  
  //Now creating the Huffman tree from the linked list
  tree=createHuff(treenode,ctr2);


  //Assigning codes to each character in the input file
  assigncode(tree,str1,codes);

  //Writing huffman tree header and the binary code to an output file
  fptr = fopen(filename,"r");
  strcat(filename,".huff"); //naming output file as per the naming convention
  out = fopen(filename,"w+");
  ctr = 0;


  //First making the header and writing it to an output file
  makeheader(tree,out);
  fprintf(out,"0%d\n",tree->val);

  //Now writing binary code to the same output file
  writebinarypath(fptr,out,byte,str,codes);

  //Closing files opened
  fclose(fptr);
  fclose(out);

  //freeing previously allocated memory

  free(str);
  free(str1);
  free(byte);

  //freeing the codes array that stored binary codes for each character in the input file
  for(i=0;i<256;i++)
    {
      free(codes[i]);
    }
  free(codes);

  //freeing the huffman tree
  Destroy_tree(tree);

  return 0;
}

