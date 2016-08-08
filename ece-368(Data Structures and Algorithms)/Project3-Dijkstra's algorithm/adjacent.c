#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include"adjacent.h"
#define true 1
#define false 0 


/*
  Main begins
*/
int main(int argc, char* argv[])
{
  char* filename = malloc(sizeof(char*));
  int nvert = 0; //no. of vertices
  int nedge = 0; //no. of edges
  int nquery = 0; //no. of queries
  int src = 0; //source vertex in map query
  int dest = 0; //destination vertex in map query
  int ctr1 = 0; //counter
  int i, j = 0; //arbitrary variables used in fscanf
  int adj_weight = 0; //stores weights of adjacent nodes during the creation of adj_list
  int Dijkstra_res = 0; //result of Dijkstra's algorithm
  FILE* fptr = NULL;

  strcpy(filename,argv[1]);
  fptr = fopen(filename,"r");
  fscanf(fptr,"%d %d",&nvert,&nedge);

/*
  Doing these declarations here because we are reading value of nvert here
*/
  Vertex vertices[nvert]; 
  Adj_List *adj_list = malloc(nvert * sizeof(Adj_List));
  for (i=0; i<nvert; i++)
    {
      adj_list[i].head = NULL;
    }

/*
  Initializing the vertex array's attributes
*/
  for(ctr1 = 0; ctr1 < nvert; ctr1++)
    {
      fscanf(fptr,"%d %d %d",&i,&vertices[ctr1].x,&vertices[ctr1].y);
      vertices[ctr1].distance = 100000;
      vertices[ctr1].parent = -1;
      vertices[ctr1].index = ctr1;
      vertices[ctr1].visited = false;
    }

/*
  Initializing the adjacency list and adding edges
*/
  while(fscanf(fptr,"%d %d",&i,&j) != EOF)
    {
      adj_weight = calc_dist(vertices[i].x,vertices[i].y,vertices[j].x,vertices[j].y);

      Adj_Node* newNode = create_adj_node(j,adj_weight);
      newNode->next = adj_list[i].head;
      adj_list[i].head = newNode;
 
      // Since graph is undirected, add an edge from dest to src also
      newNode = create_adj_node(i,adj_weight);
      newNode->next = adj_list[j].head;
      adj_list[j].head = newNode;
    }

/*
  closing the first file opened
*/
  fclose(fptr);
  fptr = fopen(argv[2],"r");
  fscanf(fptr,"%d",&nquery);

  while(fscanf(fptr,"%d %d",&src,&dest) != EOF)
    {
      Dijkstra_res = Dijkstra(vertices,adj_list,src,dest,nvert);
      if(Dijkstra_res == 1)
	{
	  trace_path(vertices,src,dest); //This if statement checks if a path between the given 2 vertices was found
	}
      reinit(vertices,nvert);
    }

  fclose(fptr);

/*
Freeing memory
*/
  free(filename); 
  Destroy_adj_list(adj_list,nvert);

  return 0;
}


