#include <bits/stdc++.h>
#include <algorithm> 
using namespace std;
int nPr(int n, int k)
{
    int P[n+1][k+1];
    for(int i=0;i<n+1;i++)
    {
        for(int j=0;j<=std::min(i,k);j++)
        {
            if(j==0)
            {
                P[i][j]=1;
            }
            else
            {
                P[i][j] = P[i-1][j]+j*P[i-1][j-1];
            }
            P[i][j+1]=0; /* 0 when j>i */
        }
    }
    return P[n][k];
}
int main() 
{ 
    int n = 10, k = 2; 
    printf("Value of P(%d, %d) is %d ", 
            n, k, nPr(n, k)); 
    return 0; 
} 

/* O(n*k) space complexity: O(n*k) */
