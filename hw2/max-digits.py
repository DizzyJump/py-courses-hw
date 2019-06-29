input_str = input('Please write number: ')
one = input_str.count('1')
two = input_str.count('2')
zero = input_str.count('0')
max_num = max(one, max(zero, two))
result_string = ''
if zero == max_num:
	result_string += '0'
if one == max_num:
	result_string += '1'
if two == max_num:
	result_string += '2'
print(result_string)
