#include <bits/stdc++.h>
using namespace std;

int main() {
    long long count = 0;
	long long n; cin>>n;
	long long a; cin>>a;
	for(long long i=1;i<n;i++)
	{
	    long long b; cin>>b;
	    if(a>b)
	    {
	        count+=a-b;
	    }
	    a = b;
	}
	cout << count <<endl;
	return 0;
}
