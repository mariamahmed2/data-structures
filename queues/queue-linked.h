#include<stdlib.h>
#include<stdio.h>


#define QueueEntry int
typedef struct queuenode
{
	QueueEntry entry;
	struct queuenode *next;
}QueueNode;

typedef struct queue
{
	QueueNode *front;
	QueueNode *rear;
	int size;
}Queue;

void CreateQueue(Queue *pq){
   pq->front=NULL;
   pq->rear=NULL;
   pq->size=0;
}

int Append(QueueEntry e, Queue* pq){
  QueueNode*pn=(QueueNode*)malloc(sizeof(QueueNode));
  if (!pn)
  {
	  return 0;
  }
  else
  {
  pn->next=NULL;
  pn->entry=e;
  if (!pq->rear)
  {
    pq->front=pn;
  } 
  else
  {
    pq->rear->next=pn;
    pq->rear=pn;
    pq->size++;
  }
  return 1;
}

void Serve(QueueEntry *pe, Queue* pq)
{
	QueueNode *pn=pq->front;
	*pe=pn->entry;
	pq->front=pn->next;
	free(pn);

     if (!pq->front)
     {
        pq->rear=NULL;
	pq->size--;
     }
}

int QueueEmpty(Queue* pq)
{
	return !pq->front;
}

int QueueFull(Queue* pq)
{
	return 0;
}

int QueueSize(Queue* pq)
{
	return pq->size;
}

void ClearQueue(Queue* pq)
{
	while(pq->front)
	{
		pq->rear=pq->front->next;
		free(pq->front);
		pq->front=pq->rear;
	}
	pq->size  = 0; 
}/*Moving with two pointers,
   Exactly as in LinkedStacks*/

   void TraverseQueue(Queue* pq, void(*pf)(QueueEntry))
   {
	for(QueueNode *pn=pq->front; pn; pn=pn->next)
		(*pf)(pn->entry);
}

/*In Push and Append we have to check for exhausted memory.
 The code can be modified to:*/

/*int Append(QueueEntry e, Queue* pq)
{
  QueueNode*pn=(QueueNode*)malloc(sizeof(QueueNode));
  if (!pn)
  {
    return 0;
  }
    /*This is much better than the Error message of  	
    the book because this is more flexible. Also, 	
    the same function for contiguous implementation 
    has to return 1 always to have consistent interface*/
 /* else
  {
    //Put here exactly all of the remaining code
    return 1;
  }
}

/***** user *****/
/*

If (!Append(e, &q)){
	
}
*/


