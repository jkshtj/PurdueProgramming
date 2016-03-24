#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main( int argc, char *argv[] )  
{
  int i=0;//counter variable
  if(argc < 2)
    {
      printf("\n");
      return EXIT_SUCCESS;
    }
  for(i=1;i<argc;i++)
    {
      if(argv[i]!= NULL)
	{
          printf("%s ",argv[i]);
	}
    }
  printf("\n");
  return EXIT_SUCCESS;
}
