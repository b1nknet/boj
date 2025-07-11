#include <stdio.h>
 
int main()
{
    int seats[4] = { 0, };
    int result = 0;
    for (int i = 0; i < 4; i++) {
        scanf("%d", &seats[i]);
    }
    result = seats[0] * seats[1] + seats[2] * seats[3];
    printf("%d", result);
}
