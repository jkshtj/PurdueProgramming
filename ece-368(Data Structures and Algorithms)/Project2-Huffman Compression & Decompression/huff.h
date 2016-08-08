#include <stdio.h>

//struct for the linked list node
typedef struct node_tree
{
  char c;
  int val;
  struct node_tree *left;
  struct node_tree *next;
  struct node_tree *right;
}Node;

//function declarations
Node* createNode(int, int);
int findsmallest(int[]);
void delete_node(Node **, Node *);
void insert_node(Node **, Node *);
Node* createHuff(Node*, int);
void assigncode(Node*,char*, char**);
void makeheader(Node*,FILE*);
void writedata(FILE *, char *);
long binary_decimal(long);
void writebinarypath(FILE *, FILE *, char *, char *, char **);
+void Destroy_tree(Node *tree)

//function definitions

//Creates new linked list node
Node* createNode(int c, int value)
{
  Node *retnode=malloc(sizeof(Node));
  retnode->c = (char)c;
  retnode->val = value;
  retnode->next=NULL;
  retnode->left = NULL;
  retnode->right = NULL;
  return retnode;
}


//Finds largest element in the val array for passing it for creating a linked list
int findsmallest(int arr[])
{
  int min=10000000;
  int i=0;
  int index=0;
  //printf("here\n");
  for(i=0;i<256;i++)
    {
      if(arr[i] < min && arr[i] != 0)
	{
	  min = arr[i];
	  index = i;
	}
    }
  return index;
}


//Functions to create Huffman tree
Node* createHuff(Node* head, int n)
{
  while(n != 1)
    {
      Node *new = createNode('a',0);
      new->val = head->val + head->next->val;
      new->left = head;
      new->right = head->next;
      insert_node(&head,new);
      delete_node(&head,head);
      delete_node(&head,head);

      n = n - 1; //decreasing num of nodes by 1 each time as 2 nodes combine to form 1
    }
  return head;
}


//Inserts node when the huffman tree is being created
void insert_node(Node **list, Node *node)
{
  Node *prev =*list;
  Node *pres = *list; //preserves head of the list
  Node *temp=NULL;
  if(node->val < (*list)->val) //checking if new node could be the new head
    {
      temp = *list;
      *list = node;
      (*list)->next = temp;
    }
  else
    {
      while(*list != NULL  &&  node->val >= (*list)->val)
	{
	  prev = *list;
	  *list = (*list)->next;
	}
      if(*list != NULL)
	{
	  temp = prev->next;
	  prev->next = node;
	  node->next = temp;
	}
      else
	{
	  prev->next = node;
	}
    }
  *list = pres; //reassigning head of the list;
}


//Deletes node when huffman tree is being created
void delete_node(Node **list, Node *node)
{
  Node *prev = *list;
  Node *pres = *list;

  if(node->c == (*list)->c)
    {
      *list = (*list)->next; //head of list preserved automatically 
    }
  else
    {
      while(node->c != (*list)->c)
	{
	  prev = *list;
	  *list = (*list)->next;
	}
      prev->next = (*list)->next;
      *list = pres;
    }
}

//Function to traverse tree and assign codes
void assigncode(Node *tree, char *code, char **code_arr)
{
  char *str = malloc(sizeof(char*));
  strcpy(str,code);
  if(tree->left != NULL  &&  tree->right != NULL)
    {
      //recursing on left sub-tree
      strcat(code,"0"); //encountered zero
      assigncode(tree->left,code,code_arr); 
      
      //recursing on right sub-tree
      strcat(str,"1");
      assigncode(tree->right,str,code_arr);
    }
  else
    {
      strcpy(code_arr[(int)tree->c],str);
      //printf("%c  :  %s\n",tree->c,str);
    }
  free(str);
}


//makeheader part of output file for uncompression; Basically traverses the huffman tree post-order
void makeheader(Node *tree, FILE *fptr)
{
  if(tree->left != NULL && tree->right != NULL)
    {
      makeheader(tree->left,fptr);
      makeheader(tree->right,fptr);
      fprintf(fptr, "0");
    }
  else
    {
     fprintf(fptr, "1%c",tree->c);
    }
}  


//Reads characters from the input file, compresses them to binary and with helper functions writes them to output file

void writebinarypath(FILE *fptr, FILE *out, char *byte, char *str, char **codes) //fptr is input file ptr and out is output file ptr
{
  int ctr = 0;
  int size_byte=0; //stores the diff b/w the size of the byte that is under construction and 8 bits
  size_t size = 1000;

  while(fgets(str,size,fptr) != NULL)
    {
      while(*(str+ctr) != '\n' && *(str+ctr) != '\0') //to stop when newline is encountered and to exclude null
  	{
	  if((strlen(byte) + strlen(codes[(int)*(str+ctr)])) < 8) //Keeps adding binary codes of diff input chars to byte till it's less than 8
	    {
	      strcat(byte,*(codes+(int)*(str+ctr)));
	    }
	  else if((strlen(byte) + strlen(codes[(int)*(str+ctr)])) > 8) //If adding anymore chars to byte makes it > 8, this part just adds size_byte number of chars to byte to make its len 8
	    {
	      size_byte = 8 - strlen(byte);
	      strncat(byte,*(codes+(int)*(str+ctr)),size_byte);
	      writedata(out,byte); //now the byte can be written to the output file since it's length is 8
	      strcpy(byte,codes[(int)*(str+ctr)]+size_byte); //copies remaining part of the most recent char's binary code into byte
	    }
	  else if((strlen(byte) + strlen(codes[(int)*(str+ctr)])) == 8) //If byte len == 8, it can just be written to the file
	    {
	      strcat(byte,*(codes+(int)*(str+ctr)));
	      writedata(out,byte);
	      strcpy(byte,"\0");
	    }
  	  ctr++;
  	}

      if(*(str+ctr) != '\n' || *(str+ctr) != '\0') //Takes into account the newline chars at the end of each line in input file, i.e, if the input file is made that way //Does the same thing as above essentially
	{

	  if((strlen(byte) + strlen(codes[(int)*(str+ctr)])) < 8)
	    {
	      strcat(byte,*(codes+(int)*(str+ctr)));
	    }
	  else if((strlen(byte) + strlen(codes[(int)*(str+ctr)])) > 8)
	    {
	      size_byte = 8 - strlen(byte);
	      strncat(byte,*(codes+(int)*(str+ctr)),size_byte);
	      writedata(out,byte); //now the byte can be written to the output file since it's length is 8
	      strcpy(byte,codes[(int)*(str+ctr)]+size_byte);
	    }
	  else if((strlen(byte) + strlen(codes[(int)*(str+ctr)])) == 8)
	    {
	      strcat(byte,*(codes+(int)*(str+ctr)));
	      writedata(out,byte);
	      strcpy(byte,"\0");
	    }
	}

      ctr=0;
    }

  if(strcmp(byte,"\0") != 0) //Takes into account the corner case, i.e, when the file's end has been reached but byte len != 8; Pads the byte with zeroes
    {
      while(strlen(byte) != 8)
	{
	  strcat(byte,"0");
	}
    }

  writedata(out,byte); //helper function to write data to output file
}


//Converts the binary number stored in a long integer to an actual long integer
long binary_decimal(long n) /* Function to convert binary to decimal.*/

{
    long decimal=0, i=0, rem;
    while (n!=0)
    {
        rem = n%10;
        n/=10;
        decimal += rem*pow(2,i);
        ++i;
    }
    return decimal;
}


//Writes binary data as char to the output file
void writedata(FILE *fptr, char * byte)
{
  long b = 0;
  //printf("%s\n",byte);
  b = strtol(byte,NULL,10); //here we have the binary number that has to be written to the file
  b = binary_decimal(b); //here we convert the binary to a long integer
  fprintf(fptr,"%c",(char)b);
}

//Frees huffman tree
void Destroy_tree(Node *tree)
{
  if(tree != NULL)
    {
      if(tree->left != NULL)
	{
	  Destroy_tree(tree->left);
	}
      free(tree);
      if(tree->right != NULL)
	{
	  Destroy_tree(tree->right);
	}
    }
}
