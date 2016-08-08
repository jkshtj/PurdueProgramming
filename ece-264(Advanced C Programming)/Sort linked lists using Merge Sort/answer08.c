#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include"answer08.h"

/**
 * Create a new list-node with the passed string. 
 * str should be copied (with strdup).
 */
List * List_createNode(const char * str)
{
  List * retlist = malloc(sizeof(List));
  retlist->str=strdup(str);
  retlist->next=NULL;
  return retlist;
}

/**
 * Free all memory associated with the linked list, including memory for
 * contained strings. Must safely handle NULL lists.
 */
void List_destroy(List * list)
{
  List* ptr=list;
  if(ptr!=NULL)
    {
      free(list->str); ////is free(ptr->str) same as free(list->str)
      List_destroy(ptr->next);
    }
  free(list);
}


/**
 * Length of a linked list. 
 * The length of "NULL" is 0.
 */
int List_length(List * list)
{
  int len=0;
  List* ptr=list;
  while(ptr!=NULL)
    {
      ptr=ptr->next;
      len++;
    }
  return len;
}

/**
 * Merge two sorted lists to produce a final sorted list.
 * 
 * 'lhs' and 'rhs' are two sorted linked-list. Read 'left-hand-side' and 'right-
 * hand-side'. Note that either (or both) could be NULL, signifying the empty
 * list.
 * 'compar' is a function that is used to compare two nodes. This parameter is 
* similar to the parameter in qsort(...), except that it only compares two
 * strings. You can pass 'strcmp' to this function if you want to sort lists in
 * ascending order.
 *
 * When implementing this function, do not call List_createNode(...) or
 * malloc(...) Instead, think about how to build a new list by:
 * (1) Create a new (empty -- i.e., NULL) list where we build the result. You 
 *     will need to track the first and last node of this list.
 * (2) In a while-loop:
 * (2.a) Use compar to identify whether the front node of lhs or rhs is smaller.
 *       Remember that lhs or rhs could be NULL. 
 * (2.b) Move the front node of 'lhs/rhs' to the end of the result list. 
 *
 * You will need to consider what happens when 'lhs' or 'rhs' becomes NULL.
 *
 * Well-written code should be 20-30 lines long, including comments and spacing.
 * If your code is longer than this, then you may save time by rethinking your
 * approach.
 */
List * List_merge(List * lhs, List * rhs, int (*compar)(const char *, const char*))
{
  List* head1=lhs;
  List* head2=rhs;
  List* result=NULL;
  int res=0;//result of comparison of two string components
  int len1=0;//length of lhs
  int len2=0;//length of rhs
  if((head1!=NULL)&&(head2!=NULL))
    {
      while((head1!=NULL) && (head2!=NULL))
	{
	  res=compar(head1->str,head2->str);
	  if(res < 0)
	    {
	      result=head1;
	      head1=head1->next;
	      if(head1!=NULL)
		{
		  if((compar(head1->str,head2->str)<0) || (compar(head1->str,head2->str)==0))
		    {
		      result->next=head1;
		    }
		  else
		    {
		      result->next=head2;
		    }
		}
	    }
	  else
	    {
	      result=head2;
	      head2=head2->next;
	      if(head2!=NULL)
		{
		  if((compar(head1->str,head2->str)>0) || (compar(head1->str,head2->str)==0))
		    {
		      result->next=head2;
		    }
		  else
		    {
		      result->next=head1;
		    }
		}
	    }
	}
      if(head1==NULL)
	{
	  result->next=head2;
	}
      else
	{
	  result->next=head1;
	}
      len1=List_length(lhs);
      len2=List_length(rhs);
      if(len1>len2) return lhs;
      else return rhs;
     }
  else if(head1==NULL){lhs=rhs; return lhs;}
  else if(head2==NULL){rhs=lhs; return rhs;}
  return NULL;
}

/////////////List_print///////////
void List_print(List* list)
{
  List* ptr=list;
  while(ptr!=NULL)
    {
      printf(" + %p ['%s' %p]\n",ptr,ptr->str,ptr->next);
      ptr=ptr->next;
    }
  printf("\n");
}

/** 
 * Sorts the list's elements using the merge-sort algorithm.
 * Merge-sort is a recursive algorithm. See the README for hints.
 * 
 * The brief instructions are as follows:
 *
 * (1) Base case: 
 * Lists of length 0 or 1 are already (defacto) sorted. In this case, return
 * 'list'.
 *
 * (2) Recursive case: 
 * (2.a) Split the linked-list into two approx. equal sized lists.
 * (2.b) Call List_sort(...) on each of these smaller lists.
 * (2.c) Call List_merge(...) to merge the now sorted smaller lists into a 
 *       single larger sorted list, which you return.
 *
 * Well-written code should be 20-30 lines long, including comments and spacing.
 * If your code is longer than this, then you may save time by rethinking your
 * approach.
 */
List * List_sort(List * list, int (*compar)(const char *, const char*))
{
  int len=0;//length of the list
  int l=1;//will act as ctr for the while loop
  List* sorted1=NULL;
  List* sorted2=NULL;
  List* final=NULL;//list to be returned
  len=List_length(list);
  if(len>1)
    {
      List* ptr=list;//will point to first part of the list
      List* list1=NULL;//will point to second part of the list in the future
      while(list!=NULL)
	{
	  if((l==len/2))
	    {
	      list1=list->next;
	      list->next=NULL;
	    }
	  if(list!=NULL)
	    {
	      list=list->next;
	    }
	  l++;
	}
      list=ptr;
      sorted1= List_sort(list,compar);
      sorted2= List_sort(list1,compar);
      final= List_merge(sorted1,sorted2,compar);
      return final;
    }
  return list;
}

int strrcmp(const char * a, const char * b)
{
  return -strcmp(a, b);
}


