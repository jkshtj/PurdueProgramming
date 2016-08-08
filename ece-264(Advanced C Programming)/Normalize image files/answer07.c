#include "answer07.h"

#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <libgen.h>
#include <string.h>

#define ECE264_MAGIC_NUMBER 0x21343632
#define DEFAULT_DPI_X 3780
#define DEFAULT_DPI_Y 3780

#define FALSE 0
#define TRUE 1


/**
 * Loads an ECE264 image file, returning an Image structure.
 * Will return NULL if there is any error.
 *
 * Hint: Please see the README for extensive hints
 */

//---ECE264 header printing function---//
static void ECE264_printHeader(ImageHeader* header)
{
  printf("Printing ECE264 header information:\n");
  printf("  file type (should be %x): %x \n", ECE264_MAGIC_NUMBER,header->magic_number);
  printf("  width: %d\n", header->width);
  printf("  height: %d\n", header->height);
  printf("  comment length: %d\n", header->comment_len);
}

//--ECE264_checkValid--//
static int ECE264_checkValid(ImageHeader * header)
{
  // Make sure this is a ECE264 file
  if (header->magic_number !=ECE264_MAGIC_NUMBER) return FALSE;

  // Make sure width is not zero
  if (header->width == 0) return FALSE;

  // Make sure height is not zero
  if (header->height == 0) return FALSE;

  // Make sure there is no compression
  if (header->comment_len == 0) return FALSE;

  // We're winners!!!
  return TRUE;
}


Image * Image_load(const char * filename)
{
  FILE* fp=NULL;
  size_t read;
  ImageHeader header;
  Image* tmp_im=NULL;
  Image* im=NULL;
  size_t n_bytes;
  int err= FALSE;

  if(!err)
    {//open file
      fp= fopen(filename,"rb");
      if(!fp)
	{
	  fprintf(stderr,"Failed to read header from %s\n",filename);
	  err=TRUE;
	}
    }

  if(!err)
    {//read header
      read=fread(&header,sizeof(ImageHeader),1,fp);
      if(read!=1)
	{
	  fprintf(stderr,"Failed to read header from %s\n",filename);
	  err=TRUE;
	}
    }

  if(!err)
    {//print header
      ECE264_printHeader(&header);
    }

  if(!err)
    {//check if the file is valid
      if(!ECE264_checkValid(&header))
	{
	  fprintf(stderr,"Invalid header in %s\n",filename);
	  err=TRUE;
	}
    }

  if(!err)
    {//reserve memory for the image object "tmp_im" created earlier
      tmp_im=malloc(sizeof(Image));
      if(tmp_im==NULL){
	fprintf(stderr,"Failed to allocate memory\n");
	err=TRUE;
      }
    }

  if(!err)
    {//Init the Image struct object
      tmp_im->width = header.width;
      tmp_im->height = header.height;
      tmp_im->comment=NULL;
      tmp_im->data=NULL;
      // Handle the comment---------------///also ask why using basename?????????????
      n_bytes = sizeof(char) * (header.comment_len);
      tmp_im->comment = malloc(n_bytes);
      if(tmp_im->comment == NULL)
	{
	fprintf(stderr, "Failed to allocate %zd bytes for comment\n",n_bytes);
	err = TRUE;
      } 
      else 
	{
	  read=fread(tmp_im->comment,sizeof(char),n_bytes,fp);
	  if(read != n_bytes) 
	    {
	      fprintf(stderr, "Failed to read header from '%s'\n", filename);
	      err = TRUE;
	    }
	}
    }
  if(!err)
    {
      if(tmp_im->comment[header.comment_len-1]!='\0')
	{
	  fprintf(stderr,"The comment does not end with a null character.\n");
	  err=TRUE;
	}
    }

  if(!err)
    { // Handle image data
      n_bytes = sizeof(uint8_t) * header.width * header.height;
      tmp_im->data = malloc(n_bytes);
      if(tmp_im->data == NULL) 
	{
	  fprintf(stderr, "Failed to allocate %zd bytes for image data\n",
		  n_bytes);
	  err = TRUE;
	}
    }

  if(!err)
    {//read the image data
      read=fread(tmp_im->data,sizeof(uint8_t),header.width*header.height,fp);
      if(read!=header.width*header.height)
	{
	  fprintf(stderr,"Failed to read image data.\n");
	  err=TRUE;
	}
    }

  if(!err) 
    { // We should be at the end of the file now
      uint8_t byte;
      read = fread(&byte, sizeof(uint8_t), 1, fp);
      if(read != 0) 
	{
	  fprintf(stderr, "Stray bytes at the end of bmp file '%s'\n",
		  filename);
	  err = TRUE;
	}
    }

  if(!err) 
    { // We're winners...
      im = tmp_im;  // bmp will be returned
      tmp_im = NULL; // and not cleaned up
    }

  // Cleanup
  if(tmp_im != NULL) 
    {
      free(tmp_im->comment); // Remember, you can always free(NULL)
      free(tmp_im->data);
      free(tmp_im);
    }
  if(fp)
    {
      fclose(fp);
    }

  return im; 
}

/**
 * Save an image to the passed filename, in ECE264 format.
 * Return TRUE if this succeeds, or FALSE if there is any error.
 *
 * Hint: Please see the README for extensive hints
 */


////////////////////////////////////////////////////////////////////////////////////////////////////////
int Image_save(const char * filename, Image * image)
{
  int err = FALSE; 
  FILE * fp = NULL;
  size_t written = 0;

  // Attempt to open file for writing
  fp = fopen(filename, "wb");
  if(fp == NULL) 
    {
      fprintf(stderr, "Failed to open '%s' for writing\n", filename);
      return FALSE; // No file ==> out of here.
    }

  // Prepare the header
  ImageHeader header;
  header.magic_number = ECE264_MAGIC_NUMBER;
  header.width = image->width;
  header.height = image->height;
  header.comment_len = strlen(image->comment) + 1;
 
  if(!err) 
    {  // Write the header
      written = fwrite(&header, sizeof(ImageHeader), 1, fp);
      if(written != 1) 
	{
	  fprintf(stderr,"Error: only wrote %zd of %zd of file header to '%s'\n", written, sizeof(ImageHeader), filename);
	  err = TRUE;	
	}
    }
  if(!err)
    {
      written=fwrite(image->comment,sizeof(char),header.comment_len,fp);
      if(written!=header.comment_len)
	{
	  fprintf(stderr,"Error:did not write the comment properly.\n");
	  err=TRUE;
	}
    }
 
  if(!err)
    { // Write pixels	
       written = fwrite(image->data, sizeof(uint8_t), header.width*header.height, fp);
      if(written != header.width*header.height)
	{
	  fprintf(stderr, "Failed to write pixel data to file\n");
	  err = TRUE;
	}
    }
    
  // Cleanup
  if(fp)
    fclose(fp);

  return !err;
}
/**
 * Free memory for an image structure
 *
 * Image_load(...) (above) allocates memory for an image structure. 
 * This function must clean up any allocated resources. If image is 
 * NULL, then it does nothing. (There should be no error message.) If 
 * you do not write this function correctly, then valgrind will 
 * report an error. 
 */
void Image_free(Image * image)
{
  if(image != NULL) 
    {
      free(image->comment); // Remember, you can always free(NULL)
      free(image->data);
      free(image);
    }
}

/**
 * Performs linear normalization, see README
 */
void linearNormalization(int width, int height, uint8_t * intensity)
{
  int min=255;
  int max=0;
  int i=0;
  for(i=0;i<width*height;i++)
    {
      if(intensity[i]<min)
	{
	  min=intensity[i];
	}
      else if(intensity[i]>max)
	{
	  max=intensity[i];
	}
    }
  for(i=0;i<width*height;i++)
    {
      intensity[i]=(intensity[i]-min)*255.0/(max-min);
    }
}

