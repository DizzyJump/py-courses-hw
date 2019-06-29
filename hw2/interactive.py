a, b = input('Please type two integers delimeted by 1 space: ').split()
a = int(a)
b = int(b)
print('=' * 20,'Меню','=' * 20)
print('1: Сложить')
print('2: Проверить делится ли одно на другое без остатка')
print('3: Проверить является ли первое число квадратов сторого')
option = int(input('Ваш выбор: '))
if option == 1:
	print(a+b)
elif option == 2:
	print(max(a, b) % min(a, b) == 0)
else:
	print(a == b * b)