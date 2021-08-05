#include <stdio.h>

#define Max 100
#define StackEntry int

typedef struct stack
{
    int top;
    StackEntry entry[10];
} Stack;

void CreatStack(Stack *ps) //pointer due to effeincy
{
    ps->top = 0;
}

/*Pre: The stack is initialized and not full
Post: The element e has been stored at the top of the stack; 
     and e does not change*/
void Push(StackEntry e, Stack *ps)
{
    ps->entry[ps->top] = e;
    ps->top++; //OR -- ps->entry[ps->top++] = e;
}

int StackFull(Stack *ps) //pointer due to effeincy
{
    if (ps->top == 10)
        return 1;
    else
        return 0;
}

/*Pre: The stack is initialized and not empty
  Post: The last element entered is returned*/
void Pop(StackEntry *pe, Stack *ps)
{
    ps->top--;
    *pe = ps->entry[ps->top];
}

int StackEmpty(Stack *ps)
{
    if (ps->top == 0)
        return 1;
    else
        return 0;
}

/*Pre: Stack is initialized.
Post: returns how many elements exist.*/
int StackSize(Stack *ps)
{
    return ps->top;
}

/*Pre: Stack is initialized.
Post: destroy all elements; stack looks initialized.*/
void ClearStack(Stack *ps)
{
    ps->top = 0;
}

//Same preconditions of Pop.
/*void StackTop(StackEntry *pe, Stack *ps)
{
    printf("e is: %d \n", e);
}*/

void TraverseStack(Stack *ps, void (*pf)(StackEntry)) //(&s, &Display)
{
    for (int i = ps->top; i > 0; i--)
        (*pf)(ps->entry[i - 1]);
}