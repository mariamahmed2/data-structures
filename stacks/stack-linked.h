#include <stdio.h>
#include <stdlib.h>

#define StackEntry int
//#define stacknode int
// type of stacknode is a struct cause it is not homo
typedef struct stacknode
{
    StackEntry entry;
    struct stacknode *next;

} StackNode;
/******************************************************/
typedef struct stack
{
    StackNode *top;
    int size;
} Stack;
/*********Why not **********
  typedef StackNode *Stack
  1- To make logical distinction  between the stack itself 
  and its top, which points to a node.

2- To be consistent with the definitions of other DS.

3- For upgradability (adding more functions) that may need
 other pieces of information to be saved than top. (we will see).
*/

/***************************************************/
void CreatStack(Stack *ps)
{
    ps->top = NULL;
    ps->size = 0;
}
/******************************************************/
void Push(StackEntry e, Stack *ps)
{
    StackNode *pn = (StackNode *)malloc(sizeof(StackNode));
    pn->entry = e;
    pn->next = ps->top;
    ps->top = pn;
    ps->size++;
}
/******************************************************/
void Pop(StackEntry *pe, Stack *ps)
{
    StackNode *pn;
    *pe = ps->top->entry; //StackTop
    pn = ps->top;         // temporary pointer to free
    ps->top = ps->top->next;
    free(pn); // data still exists but canot be used
    // pn points to the same freed location
    ps->size--;
}
/************************************************/
int StackEmpty(Stack *ps)
{
    return ps->top == NULL;
}
/***************************************************/
int StackFull(Stack *ps) // never full
{
    return 0;
}
/****************************************************/
void ClearStack(Stack *ps)
{
    StackNode *pn = ps->top;
    while (pn)
    {
        pn = pn->next;
        free(ps->top);
        ps->top = pn;
    }
    ps->size = 0;
}
/*************************************************/
void Traversestack(Stack *ps, void (*pf)(StackEntry))
{
    StackNode *pn = ps->top;
    while (pn)
    {
        (*pf)(pn->entry); //passing pn->entry to the fuction
        pn = pn->next;
    }

    /////// same code//////////
    /* for(StackNode *pn = ps->top; pn; pn = pn->next)
    (*pf) (pn->entry);
    */
}

/*********************************************/
int StackSize(Stack *ps)
{
    /* int x;
    StackNode *pn = ps->top;
    for(x=0; pn; pn = pn->next)
    x++;
    return x;*/
    //thta(N)
    ps->size; // theta(1)
}
