print('标识符')
s1 = 'python'
s2 = 'python%'
print(s1.isidentifier())
print(s2.isidentifier())

print('空白符')
s3 = '  '
print(s3.isspace())
print(s1.isspace())

print('字母')
print(s1.isalpha())
print(s2.isalpha())

print('十进制数字')
s4 = '123四'
s5 = '123'
print(s4.isdecimal())
print(s5.isdecimal())

print('数字')
print(s4.isnumeric())

print('字母和数字')
s6 = 'ab123四%'
s7 = 'ab123四'
print(s6.isalnum())
print(s7.isalnum())
