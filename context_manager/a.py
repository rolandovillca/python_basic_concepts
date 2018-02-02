class A:
    def __enter__(self):
        print '11111'
        return '22222'

    def __exit__(self, type, value, traceback):
        print '33333'
        return False

with A() as s:
    a = '44444'
    print '55555:', s

print '66666:', a
print '77777:', s


# 11111
# 55555: 22222
# 33333
# 66666: 44444
# 77777: 22222

