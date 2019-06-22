input_str = input('Input oven numbered string: ')
input_num = int(input('Input oven number').strip())
str_center = len(input_str)//2
center_offset = input_num // 2
left_substring = input_str[:str_center-center_offset]
right_substring = input_str[str_center+center_offset+1:]
center_substring = input_str[str_center-center_offset:str_center+center_offset+1][::-1]
print(left_substring+center_substring+right_substring)