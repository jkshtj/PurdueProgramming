#define true 1
#define false 0 


/*
  Structures used in the program
*/

/*
This struct represent a single vertex of a map.
*/
typedef struct vnode
{
  int x; //x coordinate
  int y; //y coordinate
  int distance; //distance of current node from source node
  int index; 
  int parent; //current vertex's parent
  int visited;
}Vertex;


/*
This struct represents a single node in an adjacency list
*/
typedef struct Adj_Node
{
  struct Adj_Node* next;
  int weight;
  int index;
}Adj_Node;


/*
This struct helps us build a set of adjacency lists, i.e., an adjacency list for all the nodes of the map
*/
typedef struct Adj_List
{
  struct Adj_Node *head;  // pointer to head node of list
}Adj_List;


/*
Global function declarations
 */
int calc_dist(int x1, int y1, int x2, int y2);
int Dijkstra(Vertex v[], Adj_List *adj_list, int src, int dest, int nvert);
int extract_min(Vertex v[], int n);
void relax(Vertex v[],int curr_node_dist, int edge, int neighbor, int parent);
void trace_path(Vertex v[], int src, int dest);
void reinit(Vertex v[], int nvert);
void call_relax(Vertex v[], Adj_List *adj_list, int curr);
Adj_Node* create_adj_node(int index, int weight);
void Destroy_adj_list(Adj_List* adj_list, int n);
void Destroy_list(Adj_Node *adj_node);



/*
Frees the memory allocated for the adjacency list
*/
void Destroy_adj_list(Adj_List* adj_list, int n)
{
  int i = 0;
  // Adj_List *ptr = adj_list;

  for(i=0;i<n;i++)
    {
      if(adj_list[i].head != NULL)
	{
	  Destroy_list(adj_list[i].head);
	} 
    }
  free(adj_list);
}

/*
  Assists Destroy_adj_list in freeing memory
*/
void Destroy_list(Adj_Node *adj_node)
{
  Adj_Node *ptr = adj_node;
  if(ptr != NULL)
    {
      Destroy_list(ptr->next);
      free(ptr);
    }
}

/*
  Creates adjacent nodes 
*/
Adj_Node* create_adj_node(int index, int weight)
  {
    Adj_Node* node = malloc(sizeof(Adj_Node));
    node->next  = NULL;
    node->index = index;
    node->weight = weight;
    return node;
  }


/*
Re-initialize vertices array
*/
void reinit(Vertex vertices[], int nvert)
{
  int ctr1 = 0;
  for(ctr1 = 0; ctr1 < nvert; ctr1++)
    {
      vertices[ctr1].distance = 100000;
      vertices[ctr1].parent = -1;
      vertices[ctr1].index = ctr1;
      vertices[ctr1].visited = false;
    }
}


/*
This function calculates the distance between 2 nodes. It takes the x and the y coordinates of the two nodes to do so.
 */
int calc_dist(int x1, int y1, int x2, int y2)
{
  return (sqrt((pow((x2 - x1),2) + pow((y2 - y1),2))));
}


/*
Relaxes the neighbors of the current vertex in the graph traversal;
 */
void relax(Vertex v[],int curr_node_dist, int edge, int neighbor, int parent)
{
  if(v[neighbor].distance > curr_node_dist + edge)
    {
      v[neighbor].distance = curr_node_dist + edge;
    }

  v[neighbor].parent = parent; 
}

/*
Calls relax- just for testing purposes
*/
void call_relax(Vertex v[], Adj_List *adj_list, int curr)
{
  int index = 0;
  int weight = 0;
  Adj_Node *list_ptr = adj_list[curr].head;

  while(list_ptr != NULL)
    {
      index = list_ptr->index;
      weight = list_ptr->weight;

      if(v[index].visited == false )
	{
	  relax(v,v[curr].distance,weight,index,curr);
	}
      list_ptr = list_ptr->next;
    }
}


/*
  Extracts closest vertex to the source node from the heap
*/
int extract_min(Vertex v[], int n)
{
  int min = 100000;
  int min_index = 0;
  int ctr = 0;

  for(ctr=0;ctr<n;ctr++)
    {
      if (v[ctr].visited == false && v[ctr].distance < min)
	{
	  min = v[ctr].distance;
	  min_index = v[ctr].index;
	}
    }
  return min_index;
}


/*
Dijkstra's algorithm
*/
int Dijkstra(Vertex v[], Adj_List *adj_list, int src, int dest, int nvert)
{
  int curr = src; //most recent node extracted
  int n = nvert;

  v[src].distance = 0;
  v[curr].visited = true;

  while(curr != dest)
    {
      call_relax(v,adj_list,curr);
      curr = extract_min(v,nvert);
      v[curr].visited = true;
      n--;
   }
  if(n==0)
    {
      printf("There is no path between the given source and destination.\n");
      return 0;
    }
  return 1;
}


/*
  Trace shortest path
*/
void trace_path(Vertex v[], int src, int dest)
{
  int i = dest; //ctr
  int j = 0; //ctr
  int path[10000] = {0}; 

  printf("%d\n",v[dest].distance);

  path[j] = dest;
  j++;

  while(i != src)
    {
      path[j] = v[i].parent;
      i = v[i].parent;
      j++;
    }

  j--; //to account for the extra increment of j done in the previous while loop at the end

  while(j >= 0)
    {
      printf("%d ",path[j]);
      j--;
    }
  printf("\n");
}

