input_str = input('Please input float: ').strip()
number = float(input_str)
floor = int(number)
even_rounded = floor - floor%2
closer_even_rounded = even_rounded + int(number-even_rounded>=1)*2
print(closer_even_rounded)