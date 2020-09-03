#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int n,max_,min_;
	float mid;
	cin>>n;
	vector<int> v(n);
	for(int i=0;i<n;i++)
		cin>>v[i];
	if(n%2==0){
        mid = (v[n/2-1]+v[n/2])/2.0;
    }
    else
        mid = v[(n+1)/2-1];
    max_ = v[0]>=v[n-1]?v[0]:v[n-1];
    min_ = v[0]<=v[n-1]?v[0]:v[n-1];

    if (mid-int(mid)==0)
        cout<<max_<<" "<<int(mid)<<" "<<min_;
    else
        cout<<max_<<" "<<mid<<" "<<min_;
	return 0;
    
}

