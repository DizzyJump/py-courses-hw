input_str = input('Input even numbered string: ')
str_len = len(input_str)
result_str = input_str[int(str_len/2):] + input_str[:int(str_len/2)]
print(result_str)