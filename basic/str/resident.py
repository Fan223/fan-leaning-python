s1 = '%'
s2 = '%'
print(s1 is s2)

s3 = 'abc%'
s4 = 'abc%'
print(s3 is s4)
print(s3 == s4)

s5 = 'abcx'
s6 = 'abcx'
print(s5 is s6)

s7 = 'abc'
s8 = 'ab' + 'c'
s9 = ''.join(['ab', 'c'])
print(s7 is s8)
print(s7 is s9)

s10 = -5
s11 = -5
print(s10 is s11)

s12 = -6
s13 = -6
print(s12 is s13)
print(type(s13))

print(s3 is s4)
import sys

s3 = sys.intern(s4)
print(s3 is s4)
