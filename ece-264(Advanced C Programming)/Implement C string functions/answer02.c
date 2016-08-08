#include "answer02.h"


size_t my_strlen(const char * str)
{
	int count = 0;
	while (str[count] != '\0')
	{
		count++;
	}
	return count;
}


int my_countchar(const char * str, char ch)
{
	int count = my_strlen(str);
	int len;
	int i=0;
	for (len = 0; len <= count; ++len)
	{
		if (str[len] == ch)
		{
			i++;
		}
	}
	return i;
}


char * my_strrchr(const char * str, int ch)
{
	int count = my_strlen(str);
	int len;
	int i = count;
	char * ptr;
	for (len = count; len >= 0; --len)
	{
	  if (str[len] != ch)
		{
			i--;
		}
		else
		{
			len = -1;
		}
	}
	if (i<0)
	{
	  ptr = NULL;
	}
	else
	{
		ptr = (char*)str + i;
	}
	return (char *)ptr;
}


char * my_strchr(const char * str, int ch)
{
	int count = my_strlen(str);
	int len;
	char * ptr=NULL;
	for (len = 0; len <= count; ++len)
	{
		if (str[len] == ch)
		{
		  ptr=(char*)str+ len;
		  return (char*)ptr;
		}
	}
	if (len > count)
	{
	  ptr = NULL;
        }
	return (char *)ptr;
}


char * my_strstr(const char * haystack, const char * needle)
{
  int c1 = my_strlen(haystack);
  int c2 = my_strlen(needle);
  int i=0;
  int j=0;
  int k=0;
  int count=0;//counts how many characters of needle are there in haystack
  int count1=0;//counts how many characters of needle are there in haystack exactly as they appear in needle
  char *ptr=NULL;
  for(i=0;i<c2;i++)
    {
      for(j=0;j<c1;j++)
	{
	  if(i==0)
	    {
	      if(*(needle+i)==*(haystack+j))
		{
		  k=j;
		  count++;
		}
	    }
          else
	    {
              if(*(needle+i)==*(haystack+j))
		{
		  count++;
		}
	    }
	}
    }
  for(i=0;i<c2;i++)
    {
      if(*(needle+i)==*(haystack+k))
	{
	  count1++;
	  k++;
	}
    }
  if(*(needle)=='\0')
    {
      ptr=(char *)haystack;
    }
  else if(count>=c2)
    {
      if(count1==c2)
        {
	  ptr=my_strchr(haystack,*(needle));
	}
    }
  else
    {
     ptr=NULL;
    }      
  return (char*)ptr;
}


char * my_strcpy(char * dest, const char * src)
{
  int c2 = my_strlen(src);
  int i=0;
  char *ptr;
  for(i=0;i<=c2;i++)
    {
      dest[i]=src[i];
    }
  ptr=(char*)dest;
  return (char *)ptr;
}


char * my_strcat(char * dest, const char * src)
{
  int c1=my_strlen(dest);
  int c2 = my_strlen(src);
  int i=c1;
  int j=0;
  char *ptr=NULL;
  //*(dest + c2)= ' ';
  for(i=c1;i<=c1+c2;i++)
    {
      dest[i]=src[j];
      j++;
    }
  *(dest + c1+c2)='\0';
  ptr=(char*)dest;
  return (char *)ptr;
}


int my_isspace(int ch)
{
	if(ch=='\f' || ch=='\n' || ch=='\r' || ch=='\t' || ch=='\v' || ch==' ')
	{
		return 1;
	}
	return 0;
}

int my_atoi(const char * str)
{
  int ch_neg=1;
  int count=0; //counts number of blank spaces
  int ret=0;
  while(my_isspace(*(str+count)) || *(str+count)=='-')
    {
      if(*(str+count)=='-')
	{
	  count++;
	  ch_neg=-1;
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
  if(ch_neg==-1)
    {
      return (-1*ret);
    }
  else
    {
      return ret;
    }
}



