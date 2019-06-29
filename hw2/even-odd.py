a, b = input('Please type two integers delimeted by 1 space: ').split()
a = int(a)
b = int(b)
if a * b == 0:
	print('Error: zero is not allowed')
elif (a + b) % 2 == 0:
	print('Error: one shoukd be odd' if a % 2 == 0 else 'Error: one should be even')
else:
	print('OK')