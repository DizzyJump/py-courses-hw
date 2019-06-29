s = input('Plaese input string: ')
s = s.replace(' ','').lower()
print(s==s[::-1])