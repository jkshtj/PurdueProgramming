#include <stdio.h>
#include <string.h>
#include "answer03.h"

int main(int argc, char * * argv)
{
	
	// Testing strCat_ex function
	int length;
	char * catStr;

	catStr = malloc ( 3 * sizeof ( int ) );

	strcpy ( catStr, "ECE" );

	length = strlen ( catStr );
	
	free ( catStr );	
	catStr = NULL;

	catStr = strcat_ex ( &catStr, &length , "How did it get so late so soon?" );

	printf ( "Concatenated string = %s\n", catStr );

	free ( catStr );

	//STRCAT_EX ends here
		
	// Testing explode function

	
	int len=0; 
	int i = 0;

	char ** strArr1 = explode ( "What the fuck is this shit?", " \t\v\n\r\f", &len );

	if ( strArr1 != NULL )
	{
			for ( i = 0; i < len ; i++ )
			{
				printf( "strArr = %s\n", strArr1[i] );
				free ( strArr1[i] );
			}
			free ( strArr1 );
		}
	//	EXPLODE ends here

    //	Testing implode function
	len=3;
	i=0;
	char * implodedStr;

	char * * strArr = malloc(len * sizeof(char*));
	strArr[0] = strdup("The");
   	strArr[1] = strdup("Turing");
   	strArr[2] = strdup("test");
   	const char * glue = " ";
   	implodedStr = implode(strArr, len, glue);
	
	
	if ( implodedStr != NULL )
	{
			printf ( "imploded String = %s\n", implodedStr );
			//free ( implodedStr );
	}
	
	//	for ( i = 0; i < len; i++ )
		  //	free ( strArr[i] );
	
		  //	free ( strArr);
	//	IMPLODE ends here

	// Testing sortStringArray

	len = 3;
	char * * sortArr = malloc(len * sizeof(char*));
    sortArr[0] = strdup("lady");
    sortArr[1] = strdup("beatle");
   	sortArr[2] = strdup("brew");
   	sortStringArray(sortArr, len);
	
	for ( i = 0; i<len; i ++ )
	{
		printf("String Arr[%d] = %s\n", i, sortArr[i] );
		free ( sortArr[i] );
	}

	free ( sortArr );

	// Testing sortStringChar

	char * s1 = strdup("The more that you read, the more things you will know. The more that you learn, the more places you\'ll go.");
	sortStringCharacters(s1);

	printf ( "Sorted String = %s\n", s1 );

	free ( s1 );
	
	
	len = 6;
	//----------------------------//


    /* char * * expArr = malloc(len * sizeof(char*)); */
    /* expArr[0] = strdup("1"); */
    /* expArr[1] = strdup("2"); */
    /* expArr[2] = strdup("3"); */
    /* 	expArr[3] = strdup("4"); */
    /* 	expArr[4] = strdup("5"); */
    /* expArr[5] = strdup("6"); */
    /* const char * gl = ", "; */
    /* char * impArr = implode(expArr, len, gl); */
    /* 	printf("Imploded array = %s\n", impArr ); */

    /* 	free ( impArr ); */

   int len1 = 1;
   char * * strArr1 = malloc(len1 * sizeof(char*));
   strArr1[0] = strdup("");
   destroyStringArray(strArr1, len1);


	return EXIT_SUCCESS;
}

 
