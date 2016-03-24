#ifndef UNHUFF_H
#define UNHUFF_H
#define TRUE 1
#define FALSE 0 
#include <stdio.h>

//Data structures used
typedef struct leaf {
    int value;
    struct leaf * left;  // left sub-tree
    struct leaf * right; // right sub-tree
} HuffNode;

typedef struct StackNode_st
{
    HuffNode * tree;
    struct StackNode_st * next;
} StackNode;


typedef struct Stack_st
{
    StackNode * head; // head node of a linked-list
} Stack;


//Function Declarations
HuffNode * HuffNode_create(int value);
void HuffNode_destroy(HuffNode * tree);
Stack * Stack_create();
void StackNode_destroy(StackNode* stacknode);
void Stack_destroy(Stack * stack);
int Stack_isEmpty(Stack * stack);
HuffNode * Stack_popFront(Stack * stack);
void Stack_pushFront(Stack * stack, HuffNode * tree);
void Stack_popPopCombinePush(Stack * stack);
HuffNode * HuffTree_readTextHeader(FILE * fp);
HuffNode * HuffTree_readBinaryHeader(FILE * fp);
void decode(FILE * infptr, char * outfile, HuffNode *tree, long);
void Destroy_tree(HuffNode*);


//Function Definitions

//Create a new, properly intialized HuffNode
HuffNode * HuffNode_create(int value)
{
  HuffNode* retnode=malloc(sizeof(HuffNode));
  retnode->value=value;
  retnode->left=NULL;
  retnode->right=NULL;
  return retnode;
}

// Destroy a tree, including all sub-children. Must handle NULL values safely.
void HuffNode_destroy(HuffNode * tree)
{
  if(tree==NULL){return;}

  HuffNode_destroy(tree->left);
  HuffNode_destroy(tree->right);
  free(tree);
  
}

//Stack
/**
 * We need a "Stack" to build the tree structure that is used to decode
 * a Huffman encoding. Stacks are very simple to implement with linked lists.
 * We must implement the following functions (given below). Each of these 
 * functions should only be a few lines of code.
 *
 * (1) Stack_create();              // Allocate a brand new stack.
 * (2) Stack_destroy(stack);        // Clean up memory for the stack.
 * (3) Stack_isEmpty(stack);    // TRUE iff (if and only if) the stack is empty.
 * (4) Stack_pushFront(stack, tree); // Push a tree onto the stack.
 * (6) Stack_popFront(stack);  // Remove a tree from the stack and return it.
 *
 * Altogether, these six functions should be around 40 lines of code.
 */

/**
 * Returns a pointer to a new empty stack struct
 */
Stack * Stack_create()
{
  Stack* nstack=malloc(sizeof(Stack));
  nstack->head=NULL;
  return nstack;
}

/**
 * Frees all memory associated with the stack. 
 * Don't forget that you must free the entire contained linked-list.
 * Also, you must safely do nothing if stack == NULL. 
 */
void Stack_destroy(Stack * stack)
{
  if(stack!=NULL){return;}
  if(stack->head==NULL)
    {
      free(stack);
      return;
    }
  while(stack->head!=NULL)
    {
      StackNode* stacknode=stack->head->next;
      free(stack->head);
      stack->head=stacknode;
    }
  free(stack);
}

/**
 * Returns TRUE (something other than zero) if the stack is empty.
 */
int Stack_isEmpty(Stack * stack)
{
  if(stack== NULL)
    {
      return TRUE;
    }
  else
    {
      return FALSE;
    }
}

/**
 * Pop the front (top) 'value' (i.e. Huffman tree) from the stack.
 *
 * More precisely, this function must do three things:
 * (1) Save the value (i.e. Huffman tree) of the head node of the stack's list
 * (2) Remove the head node of the stack's list, freeing it.
 * (3) Return the value (i.e. Huffman tree) saved in (1).
 */
HuffNode * Stack_popFront(Stack * stack)
{
  if(stack==NULL)
    {
    return NULL;
    }

  HuffNode* retnode=stack->head->tree;
  StackNode* stacknode=stack->head->next;
  free (stack->head);
  stack->head=stacknode;
  return retnode;
}

/**
 * Push a 'value' (i.e. Huffman tree) onto the front (top) of the stack.
 *
 * More precisely, this function must do two things:
 * (1) Create a new StackNode with 'tree' for its tree.
 * (2) Push that new StackNode onto the front of the stack's list.
 */
void Stack_pushFront(Stack * stack, HuffNode * tree)
{
  StackNode* stacknode=malloc(sizeof(StackNode));
  stacknode->tree=tree;
  stacknode->next=stack->head;
  stack->head=stacknode;
}

// -------------------------------------------------------- Pop Pop combine Push

/**
 * This function helps simplify building a Huffman Coding Tree from the header
 * information. It takes a stack as input. As a precondition, you can assume 
 * that the stack has at least two nodes. This function pops the front (top) 
 * two nodes, combines them into a single node, and pushes the new node back 
 * onto the stack. See Huffman_Coding.pdf to understand conceptually how this
 * should be done.
 */
void Stack_popPopCombinePush(Stack * stack)
{
  HuffNode* retnode1=Stack_popFront(stack);
  HuffNode* retnode2=Stack_popFront(stack);
  HuffNode* retnode3=HuffNode_create(0);
  retnode3->left=retnode2;
  retnode3->right=retnode1;
  Stack_pushFront(stack,retnode3);
}

//Reading HuffTree headers

/**
 * Read a Huffman Coding Tree (in text format) from 'fp'.
 */
HuffNode * HuffTree_readTextHeader(FILE * fp)
{
  Stack* stack=Stack_create();
  int i=0;//loop control
  int ch=0;
  while(i!=-1)
    {
      if(fgetc(fp)=='1')
	{
	  ch=fgetc(fp);
	  HuffNode* newnode=HuffNode_create(ch);
	  Stack_pushFront(stack,newnode);
	}
      else
	{
	  if(stack->head->next==NULL)
	    {
	      i=-1;
	    }
	  else
	    {
	      Stack_popPopCombinePush(stack);
	    }
	}
    }
  HuffNode* tree=stack->head->tree;
  free(stack->head);
  free(stack);
  return tree;
}

//Helper function for uncompression, which reads the chars from the input file and extracts binary data
int readBit(FILE * fptr , unsigned char * bit,unsigned char * whichbit , unsigned char * curbyte)
{
  int ret = 1;
  if ((* whichbit) == 0)
    {
      ret = fread(curbyte , sizeof(unsigned char), 1, fptr);
    }
  if (ret != 1)
    {
      return -1;
    }
  unsigned char temp = (* curbyte) >> (7 - (* whichbit));
  temp = temp & 0X01; // get only 1 bit, ignore the other bits
  * whichbit = ((* whichbit) + 1) % 8;
  * bit = temp;
  return 1;
}

//Decodes the bit data from the binary compressed files and prints it to an output file
void decode(FILE * infptr, char * outfile, HuffNode *root, long numchar)
{
  unsigned char whichbit = 0;
  unsigned char onebit = 0;
  unsigned char curbyte = 0;
  FILE * outfptr = fopen(outfile, "w");

  if (infptr == NULL)
    {
      printf("Error");
      return;
    }

  while(numchar != 0)
    {
      HuffNode * tn = root;
      while ((tn -> left) != NULL || (tn -> right) != NULL)
  	{
  	  readBit(infptr, &onebit, &whichbit, &curbyte);
  	  if(onebit == 0)
  	    tn = tn -> left;
  	  else
  	    tn = tn -> right;
  	}
      //printf("%c", tn -> value);
      fprintf(outfptr, "%c", tn -> value);
      numchar--;
    }
  printf("\n");
  fclose(infptr);
  fclose(outfptr);
  return;
}

//Frees the huffman tree created
void Destroy_tree(HuffNode *tree)
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

#endif

