//1

#include <iostream>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int A[5],p,sum=0;
        for(int i=0;i<5;i++)
        {
            cin>>A[i];
        }
        cin>>p;
        for(int j=0;j<5;j++)
        {
            sum+=A[j]*p;
        }
        if(sum<=144){ printf("NO\n");}
        else { printf("YES\n");}
    }
    return 0;
}

//2

#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main() {
    int t;
    cin>>t;
    while(t--)
    {   ll wd=0;
        ll n;
        cin>>n;
        ll a[n],b[n];
        a[0]=0;
        b[0]=0;
        ll sum1[n+1],sum2[n+1];
        for(ll i = 1;i<n+1;i++)
        {
            cin>>a[i];
        }
        for(ll j=1;j<n+1;j++)
        {
            cin>>b[j];
        }
        sum1[0] = 0;
        sum2[0] = 0;
        for(ll k=1;k<n+1;k++)
        {
            sum1[k]=sum1[k-1]+a[k];
            sum2[k]=sum2[k-1]+b[k];
        }
        for(ll x=0;x<n;x++)
        {
            if(sum1[x]==sum2[x])
            {
                if(a[x+1]==b[x+1])
                {
                    wd+=a[x+1];
                }
            }
        }
        cout<<wd<<endl;
    }
    return 0;
}
