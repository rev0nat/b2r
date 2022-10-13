#Phase 4 of laurie's bomb. We want the return value to be equal to 55 decimal.
import sys


def func4(param_1):
    var1=0
    var2=0

    if param_1 < 2:
        var2 = 1
    else:
        var1 = func4(param_1 + -1)
        var2 = func4(param_1 + -2)
        var2 = var2 + var1
    
    return var2

print(func4(int(sys.argv[1])))
