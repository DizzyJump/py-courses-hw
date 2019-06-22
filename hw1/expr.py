input_str = input('Please input two floats delimited by space: ').strip()
space_index = input_str.find(' ')
x = float(input_str[:space_index])
y = float(input_str[space_index+1:])
tmp_expr1 = x * (y ** 0.5)
tmp_expr2 = (x * x + 0.8 * y * x) ** 0.5
tmp_expr3 = (x * x - 0.8 * y * x) ** 0.5
result = (tmp_expr1/tmp_expr2) / tmp_expr3
print(result)