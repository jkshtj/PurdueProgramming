
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include"answer03.h"

int main()
{
  const char* str="The\nTuring test";
  const char* delims=" \t\v\n\r\f";
  int len;
  char * * strArr=explode(str, delims, &len);
  printf("len= %d, strArr is divided into %s, %s and %s \n", len, strArr[0], strArr[1], strArr[2]);
  /* char *str1= (char*) malloc(13); */
  /* scanf("%s",str1); */
  /* char *src="Zippy!"; */
  /* int i= sizeof(str1); */
  /* char *ptr=strcat_ex(&str1,&i,src); */
  /* printf("ptr= %s \n",*ptr); */
  return 0; 
}

char * * explode(const char * str, const char * delims, int * arrLen)
{
  int N=0;//number of delimiters in str
  int str_len; //length of str
  int ind=0; //loop control variable or the variable that we are currently viewing
  //  int j=0;//loop control
  int arrInd = 0; // this is the next position where we'll create a string
  int last = 0; // 1 + the last index we saw a delimiter. Init to 0.
  str_len= strlen(str);
  for(ind=0;ind<str_len;ind++)
    {
      if(strchr(delims,str[ind]) != NULL)
	{
	  N++;
	}
    }
  char * * strArr = malloc((N+1) * sizeof(char *));
  for(ind=0;ind<str_len;ind++)
    {
      if(strchr(delims,str[ind]) != NULL)
        {
          strArr[arrInd]= (char*) malloc(last - ind + 1);//ask why you have to use malloc again
          strArr[arrInd]=memcpy(&strArr[arrInd],str+last,last-ind);
          strArr[arrInd][last-ind]='\0';
	  last=ind+1;
	  arrInd++;
	}
    }
  strArr[N]= (char*) malloc(last - ind + 1);//ask why you have to use malloc again
  strArr[N]=memcpy(&strArr[arrInd],str+last,last-ind);
  strArr[N][last-ind]='\0';
  *arrLen=N+1;
  for(ind=0;ind<=str_len;ind++)
    {
      free(strArr[ind]);
    }
  return strArr;
}

/**
 * Append the C-string 'src' to the end of the C-string '*dest'.
 *
 * strcat_ex(...) will append the C-string 'src' to the end of the string
 * at '*dest'. The parameter 'n' is the address of a int that specifies how
 * many characters can safely be stored in '*dest'. 
 *
 * If '*dest' is NULL, or if '*dest' is not large enough to contain the result
 * (that is, the sum of the lengths of *dest, src, and the null byte), then
 * strcat_ex will:
 * (1) malloc a new buffer of size 1 + 2 * (strlen(*dest) + strlen(src))
 * (2) set '*n' to the size of the new buffer
 * (3) copy '*dest' into the beginning of the new buffer
 * (4) free the memory '*dest', and then set '*dest' to point to the new buffer
 * (5) concatenate 'src' onto the end of '*dest'.
 *
 * Always returns *dest.
 *
 * Why do we need to pass dest as char * *, and n as int *? 
 * Please see the FAQ for an answer.
 *
 * Hint: These <string.h> functions will help: strcat, strcpy, strlen.
 * Hint: Leak no memory.
 */



char * strcat_ex(char * * dest, int * n, const char * src)
{
  int c1=strlen(*dest);
  int c2=strlen(src);
  int i=0;//counter
  char *buffer=NULL;

  if((*dest == NULL) || (*n < c1+c2+1))
    {
	  *n = 1 + 2 * (c1+c2);
      buffer = malloc(sizeof(*n));
      strcpy(buffer,*dest);
      free(*dest);
      /* for(i=0;i<c1;i++) */
      /* 	{ */
      /*     free(dest[i]); */
      /* 	} */
      *dest = buffer;
      free(dest);
    }
  else
    {
      strcat(*dest,src);
    }
  return (char*) *dest;

}
