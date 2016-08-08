/* #include<stdio.h> */
/* #include<stdlib.h> */
/* #include<string.h> */
/* #include<math.h> */
/* #include<pthread.h> */
/* #include"answer12.h" */

/* typedef struct chunk_of_numbers{ */
/*   long start; */
/*   long stop; */
/*   uint128 value; */
/*   int if_prime; */
/* }chunk; */
/* /\** */
/*  * Convert the initial portion of C-string 'str' to an unsigned 128-bit integer */
/*  * */
/*  * This function should be just like atoi(...), except that it returns an 128 */
/*  * bit unsigned integer. Return 0 on any error. Don't forget you must skip  */
/*  * white-space. */
/*  * */
/*  * See PA02 for hints on implementing this function. */
/*  *\/ */
/* int my_isspace(int ch) */
/* { */
/* 	if(ch=='\f' || ch=='\n' || ch=='\r' || ch=='\t' || ch=='\v' || ch==' ') */
/* 	{ */
/* 		return 1; */
/* 	} */
/* 	return 0; */
/* } */

/* uint128 alphaTou128(const char * str) */
/* { */
/*   //int ch_neg=1; */
/*   int count=0; //counts number of blank spaces */
/*   uint128 ret=0; */
/*   while(my_isspace(*(str+count)) || *(str+count)=='-') */
/*     { */
/*       if(*(str+count)=='-') */
/* 	{ */
/* 	  //count++; */
/* 	  // ch_neg=-1; */
/* 	  return 0; */
/* 	} */
/*       if(my_isspace(*(str+count)))   */
/* 	{ */
/* 	  count++; */
/* 	} */
/*     }   */
/*   while(*(str+count)>='0' && *(str+count)<='9') */
/*     { */
/*       ret = (ret*10) + (*(str+count)-'0'); */
/*       count++; */
/*     } */
/*   /\* if(ch_neg==-1) *\/ */
/*   /\*   { *\/ */
/*   /\*     return (-1*ret); *\/ */
/*   /\*   } *\/ */
/*   /\* else *\/ */
/*   /\*   { *\/ */
/*   return ret; */
/*       // } */
/* } */

/* /\** */
/*  * Return a newly allocated C-string which represents the passed value. */
/*  * The caller is responsible for freeing the allocated string. */
/*  * */
/*  * If you have already implemented alphaTou128(...) (see hint), then you should */
/*  * be able to figure out how to implement u128ToString(...). */
/*  *\/ */
/* char * u128ToString(uint128 value) */
/* { */
/*   int len=0; */
/*   int i; */
/*   uint128 val_res=value; */
/*   int num; */
/*   char ch; */

/*   while((len==0) || (value!=0)) */
/*     { */
/*       value=value/10; */
/*       len++; */
/*     } */
/*   if(len==0) return NULL; */
/*   char* str=malloc((len+1)*sizeof(char)); // remember to free this memory  */
/*   value=val_res; */
/*   str[len]='\0'; */
/*   for(i=len-1;i>=0;i--) */
/*     { */
/*       num=value % 10; */
/*       value=value/10; */
/*       ch=48+num; */
/*       *(str+i)=ch; */
/*     } */
/*   return str; */
/* } */

/* /\** */
/*  * Test is 'value' is prime. */
/*  * 'n_threads' is the number of threads to create to complete this computation. */
/*  * Return TRUE of FALSE. */
/*  * */
/*  * LEAK NO MEMORY. */
/*  * */
/*  * Good luck! */
/*  *\/ */

/* void* worker(void* arg1) */
/* { */
/*   uint128 i=0; */
/*   chunk* c=(chunk*) arg1; */

/*   for (i = c->start; i <= c->stop; i++) */
/*     { */
/*       if (c->value % i == 0) */
/* 	{ */
/* 	  c->if_prime=FALSE; */
/* 	  return NULL; */
/* 	} */
/*     } */
/*   c->if_prime=TRUE; */
/*   return NULL; */
/* } */

/* int primalityTestParallel(uint128 value, int n_threads) */
/* { */
/*   uint128 i=0; */
/*   int created; */
/*   int j=0; */
/*   int joined=0; */
/*   int result=1; */
/*   int ctr=0; */

/*   if(value==1) */
/*     return FALSE; */
/*   else if((value==2)) */
/*     return TRUE; */
/*   else if ((value!=2) && (value%2==0)) */
/*     return FALSE; */
/*   else */
/*     { */
/*       uint128 max = floor(sqrt(value)); */
/*       uint128 chunk_size=(max+n_threads+1)/n_threads; */
/*       if((chunk_size==1) && (chunk_size*n_threads > max)) {n_threads=max;} */
/*       pthread_t* thread=malloc(n_threads*sizeof(pthread_t)); */
/*       chunk* c1=malloc(n_threads*sizeof(chunk)); */
/*       for(i = 0; i < n_threads; i++) */
/* 	{ */
/* 	  c1[i].value = value; */
/* 	  if(i==0) {c1[i].start = i * chunk_size;} */
/* 	  else { */
/* 	    c1[i].start = i * chunk_size + 1; */
/* 	  } */
/* 	  if(c1[i].start < 3){c1[i].start = 3;} */
/* 	  if(((i+1)*chunk_size <= max)){c1[i].stop = (i+1)*chunk_size;} */
/* 	  else{c1[i].stop=max;} */
/* 	  //Create the actual thread, pass in function and object */
/* 	  created = pthread_create(&thread[i], NULL, worker, (void *) &c1[i]); */
/* 	  if(c1[i].stop == max) {i = n_threads;} */
/* 	  if (created) */
/* 	    { */
/* 	      printf("ERROR, Thread not created properly!!"); */
/* 	      return 0; */
/* 	    } */
/* 	  ctr++; */
/* 	} */
/*   //////////JOIN THE THREADS//////////// */
/*       for(j = 0; j < ctr; j++) */
/* 	{ */
/* 	  joined = pthread_join(thread[j], NULL); */
/* 	  if(joined != 0) */
/* 	    { */
/* 	      printf("ERROR, Thread not joined properly!!"); */
/* 	      return 0; */
/* 	    } */
/* 	} */
/*       for(j=0; j <ctr;j++) */
/* 	{ */
/* 	  if(c1[j].if_prime != 1) */
/* 	    { */
/* 	      result = 0; */
/* 	      j = ctr; */
/* 	    } */
/* 	} */
/*       free(thread); */
/*       free(c1); */
/*       return result; */
/*     } */
/* } */


/* int main() */
/* { */
/*   uint128 i=9; */
/*   int res=primalityTestParallel(i,4); */
/*   return 0; */
/* } */


#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<pthread.h>
#include"answer12.h"

typedef struct chunk_of_numbers{
  long start;
  long stop;
  uint128 value;
}chunk;

int primality=0;
/**
 * Convert the initial portion of C-string 'str' to an unsigned 128-bit integer
 *
 * This function should be just like atoi(...), except that it returns an 128
 * bit unsigned integer. Return 0 on any error. Don't forget you must skip 
 * white-space.
 *
 * See PA02 for hints on implementing this function.
 */
int my_isspace(int ch)
{
	if(ch=='\f' || ch=='\n' || ch=='\r' || ch=='\t' || ch=='\v' || ch==' ')
	{
		return 1;
	}
	return 0;
}

uint128 alphaTou128(const char * str)
{
  //int ch_neg=1;
  int count=0; //counts number of blank spaces
  uint128 ret=0;
  while(my_isspace(*(str+count)) || *(str+count)=='-')
    {
      if(*(str+count)=='-')
	{
	  //count++;
	  // ch_neg=-1;
	  return 0;
	}
      if(my_isspace(*(str+count)))  
	{
	  count++;
	}
    }  
  while(*(str+count)>='0' && *(str+count)<='9')
    {
      ret = (ret*10) + (*(str+count)-'0');
      count++;
    }
  /* if(ch_neg==-1) */
  /*   { */
  /*     return (-1*ret); */
  /*   } */
  /* else */
  /*   { */
  return ret;
      // }
}

/**
 * Return a newly allocated C-string which represents the passed value.
 * The caller is responsible for freeing the allocated string.
 *
 * If you have already implemented alphaTou128(...) (see hint), then you should
 * be able to figure out how to implement u128ToString(...).
 */
char * u128ToString(uint128 value)
{
  int len=0;
  int i;
  uint128 val_res=value;
  int num;
  char ch;

  while((len==0) || (value!=0))
    {
      value=value/10;
      len++;
    }
  if(len==0) return NULL;
  char* str=malloc((len+1)*sizeof(char)); // remember to free this memory 
  value=val_res;
  str[len]='\0';
  for(i=len-1;i>=0;i--)
    {
      num=value % 10;
      value=value/10;
      ch=48+num;
      *(str+i)=ch;
    }
  return str;
}

/**
 * Test is 'value' is prime.
 * 'n_threads' is the number of threads to create to complete this computation.
 * Return TRUE of FALSE.
 *
 * LEAK NO MEMORY.
 *
 * Good luck!
 */

void* worker(void* arg1)
{
  uint128 i=0;
  chunk* c=(chunk*) arg1;

  for (i = c->start; i <= c->stop; i++)
    {
      if (c->value % i == 0)
	{
	  primality=0;
	  return NULL;
	}
    }
  primality=1;
  return NULL;
}

int primalityTestParallel(uint128 value, int n_threads)
{
  uint128 i=0;
  int created;
  int j=0;
  int joined=0;
  int result=1;
  int ctr=0;

  if(value==1)
    return FALSE;
  else if((value==2))
    return TRUE;
  else if ((value!=2) && (value%2==0))
    return FALSE;
  else
    {
      uint128 max = floor(sqrt(value));
      uint128 chunk_size=(max+n_threads+1)/n_threads;
      if((chunk_size==1) && (chunk_size*n_threads > max)) {n_threads=max;}
      pthread_t* thread=malloc(n_threads*sizeof(pthread_t));
      chunk* c1=malloc(n_threads*sizeof(chunk));
      for(i = 0; i < n_threads; i++)
	{
	  c1[i].value = value;
	  if(i==0) {c1[i].start = i * chunk_size;}
	  else {
	    c1[i].start = i * chunk_size + 1;
	  }
	  if(c1[i].start < 3){c1[i].start = 3;}
	  if(((i+1)*chunk_size <= max)){c1[i].stop = (i+1)*chunk_size;}
	  else{c1[i].stop=max;}

	  //Create the actual thread, pass in function and object
	  created = pthread_create(&thread[i], NULL, worker, (void *) &c1[i]);
	  if(c1[i].stop == max) {i = n_threads;}
	  if(primality==1) {i= n_threads;}
	  ctr++;
	}
  //////////JOIN THE THREADS////////////
      for(j = 0; j < ctr; j++)
	{
	  joined = pthread_join(thread[j], NULL);
	}
 
      if(primality!=1) {result=0;}
      else result =1;
      free(thread);
      free(c1);
      return result;
    }
}

