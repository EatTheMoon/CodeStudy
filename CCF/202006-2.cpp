#include <iostream>
#include <vector>
using namespace std;
//用python只能拿到60分...太菜了，从网上找了一下C++可以拿满分=.=

int main()
{
	int n,a,b,x,y;
	long long ans=0;
	cin>>n>>a>>b;
	vector<pair<int,int>>v1;

	for(int i=0;i<a;i++){
		cin>>x>>y;
		v1.emplace_back(make_pair(x,y));
	}
	int i=0,x1,y1;
	for(int j=0;j<b;j++){
		cin>>x1>>y1;
		while(i<a){
			if(x1<v1[i].first){
				break;
			}
			else if(x1>v1[i].first){
				i += 1;
			}
			else{
				ans += y1*v1[i].second;
				i += 1;
			}
		}
	}

	cout<<ans<<endl;
	return 0;
}
