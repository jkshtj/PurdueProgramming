int find_num_locations(loc* locations)
{
  int i=0;	
  while(locations!=NULL)
    {
      i++;
      locations=locations->next;
    }
  return i;
}


struct Business* create_business(char* name)
{
  struct Business* retnode=malloc(sizeof(struct Business));
  retnode->name=strdup(name);
  retnode->locations=NULL;
  retnode->num_locations=0;
  return retnode;
}


struct Location create_location(loc* node, FILE* fp, int* len)
{
  char** strArr=NULL;
  char str[6001];
  long offset;
  offset=node->offset_loc;
  fseek(fp,offset,SEEK_SET);
  fgets(str,6001,fp);
  strArr=explode(str,"\t",len);
  struct Location retnode;   //=malloc(sizeof(struct Location));
  retnode.address=strdup(strArr[2]);
  retnode.city=strdup(strArr[3]);
  retnode.state=strdup(strArr[4]);
  retnode.zip_code=strdup(strArr[5]);
  retnode.reviews=NULL;
  retnode.num_reviews=node->locations->num_reviews;
  destroyStringArray(strArr, *len);
  return retnode;
}


struct Review create_review(FILE* fp, long offset_rev, int ctr)
{
  char str[6001];
  char** strArr=NULL;
  long offset;
  int len=0;
  if(ctr==0)
    {
      offset=offset_rev;
      fseek(fp,offset,SEEK_SET);
    }
  fgets(str,6001,fp);
  strArr=explode(str,"\t",&len);
  struct Review retnode;  //=malloc(sizeof(struct Review));
  retnode.text=strdup(strArr[5]);
  retnode.stars=strtol(strArr[1],NULL,10);
  return retnode;
}


char** blast_next_line(loc* node, FILE* fp)
{
  char** strArr=NULL;
  char str[6001];
  int len;
  long offset;
  offset=node->offset_loc;
  fseek(fp,offset,SEEK_SET);
  fgets(str,6001,fp);
  strArr=explode(str,"\t",&len);
  return strArr;
}

long* get_rev_offsets_all_locs(Bus* node)
{
  int ctr=0;
  long offsets[1000];
  loc* locations=node->locations;
  while(locations!=NULL)
    {
      offset[ctr]=locations->offset_rev;
      locations=locations->next;
    }
  return offsets;
}
/* get_business_reviews(...) should return a pointer to a Business struct object
 * on the heap.  That object will include links to the individual locations.
 * For example, if "McDonald's" is the business, then there would be thousands
 * of locations.  Each Location struct object in turn contains links to
 * reviews of that location.
 *
 * bst - the object returned by create_business_bst(..)
 * name - name of the business to search for (e.g., "McDonald's"); search is
 *     case insensitive.
 * state - two-letter (uppercase) state code to filter locations by, or NULL
 *     to include all states.
 * zip_code - five digit ZIP code to filter locations by, or NULL to include
 *     all ZIP codes.
 *
 * Locations must be sorted by state >> city >> address.
 *
 * Reviews must be sorted by star rating (descending) >> text of review.
 *
 * Matching of names, cities, and states must be case-insensitive.  You
 * may use functions from strings.h for that, if you wish.
 */


int loc_cmp(const void *a, const void *b)
{
  struct Location *ia = (struct Location*)a;
  struct Location *ib = (struct Location*)b;

  if(strcasecmp(ia->state,ib->state) < 0) return 1;
  else if(strcasecmp(ia->state,ib->state)!=0) return -1;

  if(strcasecmp(ia->city,ib->city) < 0) return 1;
  else if(strcasecmp(ia->city,ib->city)!=0) return -1;

  if(strcasecmp(ia->address,ib->address) < 0) return 1;
  else if(strcasecmp(ia->address,ib->address)!=0) return -1;

  else return 0;
}

int rev_cmp(const void *a, const void *b)
{
  struct Review *ia = (struct Review*)a;
  struct Review *ib = (struct Review*)b;

  if(strcasecmp(ia->stars,ib->stars) > 0) return 1;
  else if(strcasecmp(ia->stars,ib->stars)!=0) return -1;

  if(strcasecmp(ia->text,ib->text) < 0) return 1;
  else if(strcasecmp(ia->city,ib->city)!=0) return -1;

  else return 0;
}

void sort_loc(struct Location* locations, int len)
{
  //char* str;//string sorted in ascending order alphabetically
  qsort(locations,len ,sizeof(struct Location ) ,loc_cmp);
}



char** explode(char* str, int* len)
{
  int ctr=0;
  char** strArr=NULL;
  char* token=NULL;
  token=strtok(str,"\t");
  while(token!=NULL)
    {
      strArr[ctr]=strdup(token);
      ctr++;
      token=strtok(str,"\t");
    }
  *len=ctr + 1;
  return strArr;
}

void destroyStringArray(char * * strArr, int len)
{
  int i=0;
  for(i=0;i<len;i++)
    {
      free(strArr[i]);
    }
  free(strArr);
}
