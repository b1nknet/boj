#include <stdio.h>
#include <string.h>

int main() {
	int n, i = 0, j, cnt;
	scanf("%d", &n);

	char str[51];
	while (i < n) {
		scanf("%s", str);
		j = 0, cnt = 0;

		while (j < strlen(str)) {
			if (str[j] == '(') {
				cnt++;
			}  else {
				cnt--;
			} if (cnt < 0) {
				printf("NO\n");
				break;
			}
			j++;
		}

		if (cnt == 0)
			printf("YES\n");
		else if (cnt > 0)
			printf("NO\n");
		i++;
	}
}