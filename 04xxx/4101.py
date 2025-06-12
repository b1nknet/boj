while(True):
	a, b = input().split(' ')
	a = int(a)
	b = int(b)
	if (a == b == 0): break;
	elif (a > b): print('Yes')
	else: print('No')