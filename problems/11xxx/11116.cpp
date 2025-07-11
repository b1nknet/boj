#include <iostream>

using namespace std;

int arr_right[201];
int arr_left[201];

int main() {
	int n;
	cin >> n;

	for (int j = 0; j < n; ++j) {
		int left_car = 0;
		int m; 
		cin >> m;

		for (int i = 0; i < m; ++i) {
			cin >> arr_left[i];
		}
        
		for (int i = 0; i < m; ++i) {
			cin >> arr_right[i];
		}

		for (int i = 0; i < m-1; ++i) {
			for (int j = i+1; j < m; ++j) {
				if (arr_left[i] + 500 == arr_left[j]) {
					for (int k = 0; k < m; ++k) {
						if (arr_left[j] + 500 == arr_right[k]) {
							left_car += 1;
							break;
						}
					}
				}
			}
		}
		cout << left_car << '\n';
	}
	
	return 0;
}