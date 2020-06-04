vector<int> Solution::repeatedNumber(const vector<int> &A) {
long long int square = 0;
long long int linear = 0;
for(int i =0; i < A.size(); i++)
{
linear = linear + A[i];
square = square + (long) A[i]*A[i];
}
long long int expected_square = ((A.size())*(A.size()+1)*(2*A.size() + 1))/6;
long long int linear_expected = ((A.size())*(A.size()+ 1))/2;
long long int linear_difference = linear - linear_expected;
long long int square_difference = square - expected_square;
long long int sum = square_difference / linear_difference;
long long int a = (sum + linear_difference)/2;
long long int b = sum - a;
vector<int> v;
v.push_back(a);
v.push_back(b);
return v;
}
