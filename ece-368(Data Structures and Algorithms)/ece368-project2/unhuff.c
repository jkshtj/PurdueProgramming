#include<stdlib.h>
#include<string.h>
#include <stdio.h>
#include "unhuff.h"

int main(int argc, char **argv)
{
  char *numchar = malloc(sizeof(char*));
  char *extra = malloc(sizeof(char*));
  char *filename = malloc(sizeof(char*));
  strcpy(filename,argv[1]);
  FILE *fptr = fopen(filename,"r");
  HuffNode *tree = NULL;
  tree =  HuffTree_readTextHeader(fptr);
  while(strcmp(numchar,"\n") != 0) //Counts the number of characters in the input file
    {
      fread(numchar , sizeof(unsigned char), 1, fptr);
      if(strcmp(numchar,"\n") != 0)
	{
	  strcat(extra,numchar);
	}
    }
  decode(fptr,strcat(filename,".unhuff"),tree,strtol(extra,NULL,10));
  //freeing previously allocated memory
  free(numchar);
  free(extra);
  free(filename);
  Destroy_tree(tree);
  return 0;
}

