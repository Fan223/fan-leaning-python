import traceback

try:
    print('1.-----------')
    num = 10 / 0
except ZeroDivisionError as e:
    traceback.print_exc()
