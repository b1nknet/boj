SHORT_MIN = -32768
SHORT_MAX = 32767

INT_MIN = -2147483648
INT_MAX = 2147483647

LONGLONG_MIN = -9223372036854775808
LONGLONG_MAX = 9223372036854775807

number = int(input())

if SHORT_MIN <= number <= SHORT_MAX:
    print("short")
elif INT_MIN <= number <= INT_MAX:
    print("int")
elif LONGLONG_MIN <= number <= LONGLONG_MAX:
    print("long long")