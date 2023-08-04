import basic

basic.fun()
stu1 = basic.Student('张三', 18)
stu1.info()

import basic as bas

bas.fun()
stu1 = bas.Student('张三', 18)
stu1.info()

from basic import fun

fun()
