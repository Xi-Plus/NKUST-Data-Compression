#include <bits/stdc++.h>
using namespace std;
struct encodeobj{
	map<char, pair<double, double> > table;
	double value;
};
encodeobj encode(string s) {
	int arr[s.length()];
	for(int q=0; q<s.length(); q++) {
		arr[q] = s[q];
	}
	sort(arr, arr+s.length());
	encodeobj res;
	for(int q=0; q<s.length(); q++) {
		res.table[s[q]] = make_pair(1.0 * (lower_bound(arr, arr+s.length(), s[q])-arr) / s.length(), 1.0 * (upper_bound(arr, arr+s.length(), s[q])-arr) / s.length());
	}
	double low = 0, high = 1;
	for(int q=0; q<s.length(); q++) {
		double range = high - low;
		high = low + range * (upper_bound(arr, arr+s.length(), s[q])-arr) / s.length();
		low = low + range * (lower_bound(arr, arr+s.length(), s[q])-arr) / s.length();
	}
	res.value = low;
	return res;
}
string decode(map<char, pair<double, double> > table, double value) {
	string res = "";
	while(value > 1e-7) {
		for(map<char, pair<double, double> >::iterator it=table.begin(); it!=table.end(); ++it) {
			if(value >= it->second.first && value < it->second.second) {
				res += it->first;
				value -= it->second.first;
				value /= (it->second.second - it->second.first);
				break;
			}
		}
	}
	return res;
}
int main() {
	cout<<fixed<<setprecision(17);
	encodeobj res = encode("BILL GATES");
	cout<<res.value<<endl;
	
	cout<<decode(res.table, res.value)<<endl;
}
