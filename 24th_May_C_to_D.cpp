//B
#include <bits/stdc++.h>
#include<algorithm>
using namespace std;

int main() {
    long long t;
    cin >> t;
    while (t--)
    {
        long long n;cin>>n;vector<long long>s(n);
        for(long long i=0;i<n;i++){
            cin>>s[i];
        }
        sort(s.begin(),s.end());
        long long min=1000000;
        for(long long i=0;i<n-1;i++){
           long long diff;
            diff=s[i+1]-s[i];
            if(diff<min)min=diff;
        }
        cout<<min<<endl;
    }
	return 0;
}

//C
#include <bits/stdc++.h>
#include<algorithm>
using namespace std;
int main() {
    long long t;
    cin >> t;
    while (t--)
    {
        long long n;cin>>n;vector<long long>s(n);
        long long max_p = n/2;
        long long count = 0;
        for(long long i=0;i<n;i++){
            cin>>s[i];
        }
        long long even_c=0;
        long long odd_c=0;
        int flag = 0;
        for(long long j=0;j<n;j++)
        {
            if(s[j]%2!=0)
            {
                odd_c+=1;
            }
            else even_c+=1;
        }
        
        if((even_c%2==0) && (odd_c%2==0))
        {
            printf("YES\n");
        }
        
        else{
            sort(s.begin(),s.end());
            for(long long i=0;i<n-1;i++)
                {
                    if(abs(s[i]-s[i+1])==1)
                    {
                        flag = 1;
                        break;
                    }
                    else flag = 0;
                }
        
            if(flag==1)
                {
                      printf("YES\n");
                }
            else printf("NO\n");
            }
    }
	return 0;
}

//D

#include <bits/stdc++.h>
using namespace std;
 
#define ll long long
 int power(long long a, long long n, long long p) 
{ 
    long long res = 1;      // Initialize result 
    a = a % p;  // Update 'a' if 'a' >= p 
  
    while (n > 0) 
    { 
        // If n is odd, multiply 'a' with result 
        if (n & 1) 
            res = (res*a) % p; 
  
        // n must be even now 
        n = n>>1; // n = n/2 
        a = (a*a) % p; 
    } 
    return res; 
} 
  
/*Recursive function to calculate gcd of 2 numbers*/
int gcd(long long a, long long b) 
{ 
    if(a < b) 
        return gcd(b, a); 
    else if(a%b == 0) 
        return b; 
    else return gcd(b, a%b);   
} 
  
// If n is prime, then always returns true, If n is 
// composite than returns false with high probability 
// Higher value of k increases probability of correct 
// result. 
bool isPrime(long long int n, long long k) 
{ 
   // Corner cases 
   if (n <= 1 || n == 4)  return false; 
   if (n <= 3) return true; 
  
   // Try k times 
   while (k>0) 
   { 
       // Pick a random number in [2..n-2]         
       // Above corner cases make sure that n > 4 
       long long a = 2 + rand()%(n-4);   
  
       // Checking if a and n are co-prime 
       if (gcd(n, a) != 1) 
          return false; 
   
       // Fermat's little theorem 
       if (power(a, n-1, n) != 1) 
          return false; 
  
       k--; 
    } 
  
    return true; 
} 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
 
    ll t;
    cin >> t;
    //t = 1;
    while (t--)
    {
        ll n,k;cin>>n>>k;
        if(n<=k)cout<<1<<endl;
        else{//n>k
                 if(isPrime(n,3))
                 {
                     cout<<n<<endl;
                 }
                 else{
                 for(ll i=1;i<=n;i++){//all factors of n
                            if(n%i==0){
                                if(k>=(ll)n/i){cout<<i<<endl;break;}
                            }
                    }}
        }
    }
    cerr << endl
         << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
    return 0;
}
