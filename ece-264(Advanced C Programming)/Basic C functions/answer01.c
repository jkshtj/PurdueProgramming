#include <stdlib.h>
#include "answer01.h"

int arraySum(int * array, int len)
{
  int sum = 0; //sum of the array
  while (len > 0)
    {
      sum = sum + array[len - 1];
      len = len - 1;
    }
    return sum;
}

int arrayCountNegative(int * array, int len)
{
  int count = 0; //number of negatives
  while (len > 0)
    {
      if (array[len - 1] < 0)
	{
          count = count + 1;
	}
      len = len - 1;
    }
    return count;
}

int arrayIsIncreasing(int * array, int len)
{
  int result = 1; //array increasing or decreasing
  while (len > 1)
    {
      if (array[len - 1] >= array[len - 2])
	{
	  result = 1;
	}
      else
	{
	  result = 0;
	  len = -1;
	}
      len = len - 1;
    }
    return result;
}

int arrayIndexRFind(int needle, const int * haystack, int len)
{
  int index = 0; //position of the needle
  int index_copy = -1;
  while (index < len)
    {
      if (haystack[index] == needle)
	{
	  index_copy = index;
	}
      index = index + 1;
    }
    return index_copy;
}

int arrayFindSmallest(int * array, int len)
{
  int smallest_index = len - 1; //stores the smallest element's index
  if(len == 0 || len == 1)
    {
      smallest_index = 0;
    }
  else
    {
      while(len > 0)
      {
	if(len > 1)
	  {
            if(array[smallest_index] >= array[len - 2])
  	    {
	      smallest_index = len - 2;
	    }
          }
	len = len - 1;
      }
    }
    return smallest_index;
}
