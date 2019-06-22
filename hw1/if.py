input_value = int(input('Please input number: ').strip())
yes = input_value > 1000
reference_string = 'No Yes'
result_str = reference_string[int(yes)*3:int(yes)*3+3].strip()
print(result_str)