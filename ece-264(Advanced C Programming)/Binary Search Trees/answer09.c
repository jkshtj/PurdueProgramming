#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "answer09.h"


///explode
char * * explode(const char * str, const char * delims, int * arrLen)
{

  int N=0;//number of delimiters in str
  
  int last = 0; // 1 + the last index we saw a delimiter. Init to 0.
  int ind=0; //loop control variable or the variable that we are currently viewing
  int arrInd = 0; // this is the next position where we'll create a string

  int str_len; //length of str
  str_len= strlen(str);
  
  for(ind=0;ind<str_len;ind++)
    {
      if(strchr(delims,str[ind]) != NULL)
		N++;
    }
  
  char * * strArr = malloc((N+1) * sizeof(char *));

  for(ind=0;ind<str_len;ind++)
    {
	  if (strchr(delims, str[ind]) != NULL)
	  {
		  strArr[arrInd] = malloc((ind - last + 1)*sizeof(char));//ask why you have to use malloc again
		  
		  memcpy(strArr[arrInd], str + last, ind-last);
		  strArr[arrInd][ind-last] = '\0';

		 last = ind + 1;
		 arrInd++;
	  }
	}
  

  strArr[N]=malloc(ind-last+1);//ask why you have to use malloc again 
  memcpy(strArr[arrInd], str + last, ind - last);
  strArr[N][ind-last]='\0';

  *arrLen=N+1;
  return strArr;

}

/* A BusinessNode contains the name, address, and average rating of a Business.
 * It also contains pointers to the left and right children of the node.
 */

/* typedef struct bnode { */
/*   char * name; */
/*   char * stars; */
/*   char * address; */

/*   struct bnode * left; */
/*   struct bnode * right; */
/* } BusinessNode; */

/*
 * Construct one BusinessNode. You need to allocate memory for this node first.
 *
 * The caller needs to make sure to use strdup(...) for the arguments, do not
 * use strdup(...) inside of this function.
 *
 * stars: the stars of this business
 * name: name of this business
 * address: address of this business
 */
BusinessNode *create_node(char * stars, char * name, char * address)
{
  BusinessNode* retnode=malloc(sizeof(BusinessNode));
  retnode->name=name;
  retnode->stars=stars;
  retnode->address=address;
  retnode->left=NULL;
  retnode->right=NULL;
  return retnode;
}


/* Insert a node into a BST. Primarily used in load_tree_from_file(). Return a
 * pointer to the root of the BST.
 */
BusinessNode* tree_insert(BusinessNode * node, BusinessNode * root)
{
  if((node!=NULL) && (root==NULL))
    {
      root=node;
      return root;
    }
  if((node!=NULL) && (root!=NULL))
    {
      if(strcmp(node->name,root->name)<=0)
	{
	  root->left= tree_insert(node,root->left);
	}
      else
	{
	  root->right=tree_insert(node,root->right);
	}
     }
  return root;
}

/* Parse a .tsv file line by line, create a BusinessNode for each entry, and
 * enter that node into a new BST. Return a pointer to the root of the BST.
 *
 * To break up a line of the read buffer into seperate fields, use the
 * explode(...) function from PA03. To do this, copy your answer03.h and
 * answer03.c into this directory and include "answer03.h" at the top of your
 * answer09.c
 */
BusinessNode* load_tree_from_file(char * filename)
{
  BusinessNode* new=NULL;
  BusinessNode* node;
  int len=3;
  char str[2001];
  FILE* fp;
  char** strArr;

  fp=fopen(filename,"r"); 
  if(fp==NULL) 
    {
      return NULL;
    } 

  while(fgets(str,2001,fp)!=NULL)
    {
      strArr=explode(str,"\t",&len);
      node=create_node(strArr[0],strArr[1],strArr[2]);
      free(strArr);
      new=tree_insert(node,new);
    }
  fclose(fp);
  return new;
}


/* Search a BusinessNode BST for the node with the name 'name'. Returns
 * pointer to the node with a match.
 *
 * If there is no match, return NULL.
 */
BusinessNode* tree_search_name(char * name, BusinessNode * root)
{
  BusinessNode* ans=NULL;
  if(root!=NULL)
    {
      if(strcmp(root->name,name)==0)
	{
	  ans=root;
	  return ans;
	}
      else if(strcmp(name,root->name)<=0)
	{
	 ans=tree_search_name(name,root->left);
	 return ans;
	}
      else
	{
	  ans=tree_search_name(name,root->right);
	  return ans;
	}
    }
  else
    {
      return ans;
    }
}
 
/* Print out a single node: name, address, and stars
 * The format can be similar to this:
 *
 * Country Cafe
 * ============
 * Stars:
 *    3.5
 * Address:
 *    1030 Emerald Ter, Sun Prairie, WI 53590
 *
 * This function is not graded, but it could come in very handful while
 * debugging this assignment.
 */
void print_node(BusinessNode * node)
{
  if(node!=NULL)
    {
      printf("%s\n============\n",node->name);
      printf("Stars: %s\n",node->stars);
      printf("Address: %s\n",node->address);
    }
}

/* Print the entire tree, starting from the root. Like the print_node(...)
 * function, this is not graded.
 */
void print_tree(BusinessNode * tree)
{
  if(tree!=NULL)
    {
      print_node(tree);
      printf("LEFT:\n");
      print_tree(tree->left);
      printf("RIGHT:\n");
      print_tree(tree->right);
    }
}

/* Deallocate all of the memory used by a BusinessNode BST, without memory
 * leaks.
 */
void destroy_tree(BusinessNode * root)
{
  if(root!=NULL)
    {
      free(root->name);
      free(root->stars);
      free(root->address);
      destroy_tree(root->left);
      destroy_tree(root->right);
    }
  free(root);
}

int main(int argc, char * * argv)
{
   BusinessNode * root = create_node("5.0", "random name", "random address");
   BusinessNode* ans;
   root->left = create_node("3.5", "another name", "another address");
   root->right = create_node("4.0", "yet another name", "some address");
   root->left->right = create_node("1.5", "name 3", "address 3");
   //print_tree(root);
   //ans=tree_search_name("name 3",root);
   //   printf("the value at the returned root is:\n %s\n%s\n",ans->name,ans->address);
   ans=load_tree_from_file("shortfile.tsv");
   print_tree(ans);
   return 0;
}
