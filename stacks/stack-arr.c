#include <stdio.h>
#include "stack.h"


void Display(StackEntry e)
{
    printf("e is %d\n", e);
}

int main()
{
    StackEntry e;
    Stack s;
    int x;

    CreatStack(&s);

    if (!StackFull(&s))
        Push(10, &s);
    Push(20, &s);
    Push(30, &s);
    x = StackSize(&s);
    printf("stacksize = %d\n", x);
    Display(e);

    return 0;
}
