import sys

print(sys.getsizeof('张三'))
print(sys.getsizeof(20))
print(sys.getsizeof(False))
print(sys.getsizeof(2011.233332))
print(sys.getsizeof([11, 22, 33, 44, 77]))

import time

print(time.time())
print(time.localtime())
print(time.localtime(time.time()))

import urllib.request

print(urllib.request.urlopen('http://www.baidu.com').read())

import math

print(math.pi)
