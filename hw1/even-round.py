input_str = input('Please input float: ').strip()
number = float(input_str)
floor = int(number)
even_rounded = floor - floor%2
print(even_rounded)