#include "answer06.h"
#include <stdio.h>

#define EAST 0
#define SOUTH 1
#define WEST 2
#define NORTH 3

#define TRUE 1
#define FALSE 0

//---returns the element on maze(row,column)---//
char squareAt(char * * maze, int w, int h, int row, int col)
{
  if(row >= 0 && col >= 0 && row < h && col < w)
    { return maze[row][col];}
  return FALSE;
}

//---checks whether mower can move to maze(row,column)---//
int canMove(char * * maze, int w, int h, int row, int col, int direction)
{
  switch(direction)
 {
  case EAST:  return squareAt(maze, w, h, row+0, col+1) == ' ';
  case SOUTH: return squareAt(maze, w, h, row+1, col+0) == ' ';
  case WEST:  return squareAt(maze, w, h, row+0, col-1) == ' ';
  case NORTH: return squareAt(maze, w, h, row-1, col+0) == ' ';
  }
  return FALSE; // Really this is a fatal error
}

//--moves the mower one step at a time--//
void move(char * * maze, int * row, int * col, int direction)
{
  int drow = 0, dcol = 0;
  switch(direction)
    {
    case EAST:  dcol = 1; break;
    case SOUTH: drow = 1; break;
    case WEST:  dcol = -1; break;
    case NORTH: drow = -1; break;
    }
  *row += drow;
  *col += dcol;
  maze[*row][*col]='o';
}

//--recursive function--//
void recursive(char** maze, int w, int h, int row, int col)
{
  int i=0;
  for(i=0;i<4;i++)
    {
      if(canMove(maze,w,h,row,col,i)) //i is the direction
	{
	  move(maze,&row,&col,i);
	  switch(i)
	    {
	    case EAST:  printf("%c %d\n",'E',1); break;
	    case SOUTH: printf("%c %d\n",'S',1); break;
	    case WEST:  printf("%c %d\n",'W',1); break;
	    case NORTH: printf("%c %d\n",'N',1); break;
	    }
	  recursive(maze,w,h,row,col);
	  if((i==0)||(i==1))
	    {
	      move(maze,&row,&col,i+2);
	      switch(i+2)
		{
		case EAST:  printf("%c %d\n",'E',1); break;
		case SOUTH: printf("%c %d\n",'S',1); break;
		case WEST:  printf("%c %d\n",'W',1); break;
		case NORTH: printf("%c %d\n",'N',1); break;
		}
	    }
	  else
	    {
	      move(maze,&row,&col,i-2);
	      switch(i-2)
		{
		case EAST:  printf("%c %d\n",'E',1); break;
		case SOUTH: printf("%c %d\n",'S',1); break;
		case WEST:  printf("%c %d\n",'W',1); break;
		case NORTH: printf("%c %d\n",'N',1); break;
		}
	    }
	}
    }
}

//---print_directions--//
void print_directions(char** maze, int w, int h)
{
  int i=0;//rows
  int j=0;//columns

  // Find the entrance of the maze
  while(maze[i][j]!=' ')
    {
      j++;
    }
  recursive(maze,w,h,i,j);
}

