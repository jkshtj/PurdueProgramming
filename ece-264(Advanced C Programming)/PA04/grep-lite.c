
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 2001

int main(int argc, char * * argv)
{
  int i=0;//counter for the loop
  //  int ch=0;
  char oneline[SIZE];
  int count=0;
  int count1=0;
  // FILE* fptr;

  for(i=1;i<argc;i++)
    {
      if(strcmp(argv[i],"--help")==0)
  	{
  	  printf("\nUsage: grep-lite [OPTION]... PATTERN\nSearch for PATTERN in standard input. PATTERN is a\nstring. grep-lite will search standard input line by\nline, and (by default) print out those lines which\ncontain pattern as a substring.\n\n  -v, --invert-match     print non-matching lines\n  -n, --line-number      print line numbers with output\n  -q, --quiet            suppress all output\n\nExit status is 0 if any line is selected, 1 otherwise;\nif any error occurs, then the exit status is 2.\n\n");
  	}
    }
  for(i=1;i<argc-1;i++)
    {
      if((strcmp(argv[i],"-v")!=0) && (strcmp(argv[i],"-n")!=0) && (strcmp(argv[i],"-q")!=0) && (strcmp(argv[i],"--invert-match")!=0) && (strcmp(argv[i],"--line-number")!=0) && (strcmp(argv[i],"--quiet")!=0))
	{
	  fprintf(stderr, "You have entered bogus command line arguments\n");
	  return 2;
	}
    }
 
 
  if(argv[argc-1][0]=='-')
    {
      fprintf(stderr, "You have begun the last argument with a minus sign.\n");
      return 2;
    }
 

  while(fgets(oneline,SIZE,stdin)!=NULL)
    {
      ++count;
      if(argc>2)
	{
      for(i=1;i<argc-1;i++)
	{
	  if(((strcmp(argv[i],"-v")==0) && (strcmp(argv[i+1],"-n")!=0) && (strcmp(argv[i-1],"-n")!=0) && (strcmp(argv[i+1],"-v")!=0) && (strcmp(argv[i-1],"-v")!=0) && (strcmp(argv[i+1],"-q")!=0)) || ((strcmp(argv[i],"--invert-match")==0) && (strcmp(argv[i+1],"--line-number")!=0) && (strcmp(argv[i-1],"--line-number")!=0) && (strcmp(argv[i+1],"--invert-match")!=0) && (strcmp(argv[i-1],"--invert-match")!=0) && (strcmp(argv[i+1],"--quiet")!=0)))
	    {
	      if(strstr(oneline,argv[argc-1])==NULL)
		{
		  printf("%s",oneline);
		  count1++;
		}
	    }

	  else if(((strcmp(argv[i],"-n")==0) && (strcmp(argv[i+1],"-v")!=0) && (strcmp(argv[i-1],"-v")!=0) && (strcmp(argv[i+1],"-n")!=0) && (strcmp(argv[i-1],"-n")!=0) && (strcmp(argv[i+1],"-q")!=0)) || ((strcmp(argv[i],"--line-number")==0) && (strcmp(argv[i+1],"--invert-match")!=0) && (strcmp(argv[i-1],"--invert-match")!=0) && (strcmp(argv[i-1],"--line-number")!=0) && (strcmp(argv[i-1],"--line-number")!=0) && (strcmp(argv[i+1],"--quiet")!=0)))
	    {
	      if(strstr(oneline,argv[argc-1])!=NULL)
		{
		  printf("%d: %s",count,oneline);
		  count1++;
		}
	    }

	  else if(((strcmp(argv[i],"-n")==0) && (strcmp(argv[i+1],"-v")==0)) || ((strcmp(argv[i],"--line-number")==0) && (strcmp(argv[i+1],"--invert-match")==0)))
	    {
	      if(strstr(oneline,argv[argc-1])==NULL)
		{
		  printf("%d: %s",count,oneline);
		  count1++;
		}
	    }

	  else if(((strcmp(argv[i],"-v")==0) && (strcmp(argv[i+1],"-n")==0)) || ((strcmp(argv[i],"--invert-match")==0) && (strcmp(argv[i+1],"--line-number")==0)))
	    {
	      if(strstr(oneline,argv[argc-1])==NULL)
		{
		  printf("%d: %s",count,oneline);
		  count1++;
		}
	    }

	  else if(((strcmp(argv[i],"-v")==0) && (strcmp(argv[i+1],"-v")==0)) || ((strcmp(argv[i],"--invert-match")==0) && (strcmp(argv[i+1],"--invert-match")==0)))
	    {
	      if(strstr(oneline,argv[argc-1])==NULL)
		{
		  printf("%s",oneline);
		  count1++;
		}
	    }

	  else if(((strcmp(argv[i],"-n")==0) && (strcmp(argv[i+1],"-n")==0)) || ((strcmp(argv[i],"--line-number")==0) && (strcmp(argv[i+1],"--line-number")==0)))
	    {
	      if(strstr(oneline,argv[argc-1])!=NULL)
		{
		  printf("%d: %s",count,oneline);
		  count1++;
		}
	    }

	  else if(((strcmp(argv[i],"-v")==0) && (strcmp(argv[i+1],"-q")==0)) || ((strcmp(argv[i],"--invert-match")==0) && (strcmp(argv[i+1],"--quiet")==0)))
	    {
	      return 0;
	    }

	  else if(((strcmp(argv[i],"-q")==0) && (strcmp(argv[i+1],"-v")==0)) || ((strcmp(argv[i],"--quiet")==0) && (strcmp(argv[i+1],"--invert-match")==0)))
	    {
	      return 0;
	    }

	  else if(((strcmp(argv[i],"-n")==0) && (strcmp(argv[i+1],"-q")==0)) || ((strcmp(argv[i],"--line-number")==0) && (strcmp(argv[i+1],"--quiet")==0)))
	    {
	      return 0;
	    }

	  else if(((strcmp(argv[i],"-q")==0) && (strcmp(argv[i+1],"-n")==0)) || ((strcmp(argv[i],"--quiet")==0) && (strcmp(argv[i+1],"--line-number")==0)))
	    {
	      return 0;
	    }

	  else if((strcmp(argv[i],"-q")==0) || (strcmp(argv[i],"--quiet")==0))
	    {
	      return 0;
	    }
	}
 
	}
      else
	{
	  if(strstr(oneline,argv[argc-1])!=NULL)
	    {
	      printf("%s",oneline);
	      count1++;
	    }
	}
    }
  if(count1>0){return 0;}
  else{return 1;}
}
