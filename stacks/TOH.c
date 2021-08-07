#include <stdio.h>
/*	************* stack with recursion **************
Pre:
	- There are at least count disks on the tower start.
	- The top disk on each of towers temp and finish is larger than any of the top count disks on tower start.

Post:
	- The top count disks on start have been moved to finish;
	- temp (used for temporary storage) has been returned to its starting position.
*/
/* space complixity == the largest stack size*/
/*time     ,,       ==  2**count */
// move count disks from start to finish with the help of temp
void MoveDisks(int count, int start, int finish, int temp)

{
    if (count > 0)
    {
        MoveDisks(count - 1, start, temp, finish);
        printf("Move disk % d from % d to % d\n", count, start, finish);
        //This step of printf is the base condition.
        MoveDisks(count - 1, temp, finish, start);
    }
}
void main()
{
    MoveDisks(3, 1, 3, 2);
}