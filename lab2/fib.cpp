
#include <iostream>
#include <vector>
using namespace std;

// function to calculate the fib nth term using dynamic prog.
long nth_fib(int n, vector<long> &dp)
{
    if(dp[n] != 0) 
        return dp[n];
    // Check if Nth term is computed 
    
     if(n == 1 )
        return 0;
    if(n == 2 || n == 3)
        return 1;
   // return 0 if the first element & 1 for second and third element 
   
    
    return dp[n] = nth_fib(n-2, dp) + nth_fib(n-1, dp); 
    // Store the already computed terms for the next use 
}

int main()
{
    int n;
    // vector for storing fib terms
    vector<long> dp(50); 

    cin >> n;
    cout << nth_fib(n, dp);
}
