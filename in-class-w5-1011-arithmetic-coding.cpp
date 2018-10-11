#include <bits/stdc++.h>
using namespace std;
double encode(string s) {
	int arr[s.length()];
	for(int q=0; q<s.length(); q++) {
		arr[q] = s[q];
	}
	sort(arr, arr+s.length());
	double low = 0, high = 1;
	for(int q=0; q<s.length(); q++) {
		double range = high - low;
		high = low + range * (upper_bound(arr, arr+s.length(), s[q])-arr) / s.length();
		low = low + range * (lower_bound(arr, arr+s.length(), s[q])-arr) / s.length();
	}
	return low;
}
int main() {
	cout<<fixed<<setprecision(17);
	cout<<encode("BILL GATES")<<endl;
}
