#include "timecard.h"
#include <string>
using namespace std;

void init(int n) {

}

string convert(string s) {
	for (auto &l:s) l = tolower(l);
	return s;
}