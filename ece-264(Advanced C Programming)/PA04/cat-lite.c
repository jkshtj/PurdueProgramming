
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main( int argc, char *argv[] )  
{
  int i=0;//counter for the loop
  int ch=0;
  FILE* fptr;

  if(argc<2)
    {
      while(!feof(stdin))
	{
	  ch=fgetc(stdin);
	  if(ch!=EOF)
	    {
	      printf("%c",ch);
	    }
	}
      return EXIT_SUCCESS;
    }
  else
    {
      for(i=1;i<argc;i++)
	{
	  if(strcmp(argv[i],"--help")==0)
	    {
	      printf("\nUsage: cat-lite [--help] [FILE]...\nWith no FILE, or when FILE is -, read standard input.\n\nExamples:\n");
	      printf("  cat-lite README   Print the file README to standard output.\n  cat-lite f - g    Print f's contents, then standard input,\n                    then g's contents.\n  cat-lite          Copy standard input to standard output.\n\n");
	      return EXIT_SUCCESS;
	    }
	}
      //--------------------Printing files -------------------------//
      for(i=1;i<argc;i++)
	{
	  if(strcmp(argv[i],"-")==0)
	    {
	      while(!feof(stdin))
		{
		  ch=fgetc(stdin);
		  if(ch!=EOF)
		    {
		      printf("%c",ch);
		    }
		}
	    }
	  else //if(strcmp(argv[i],"")!=0)
	    {
	      fptr=fopen(argv[i],"r");
	      if(fptr!=NULL)
		{
		  do
		    {
		      ch=fgetc(fptr);
		      if(ch!=EOF)
			{
			  printf("%c",ch);
			}
		    }while(ch!=EOF);
		  fclose(fptr);
		}
	      else
		{
		  fprintf(stderr, "%s\n",argv[i]);
		  // printf("cat cannot open %s\n",argv[i]);
		  return EXIT_FAILURE;
		}
	    }
	}
    }
  return EXIT_SUCCESS;
}
