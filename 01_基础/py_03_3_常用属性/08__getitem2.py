"""
https://www.jianshu.com/p/c48e6e903c38

把类当做列表用

类实现了__getitem,__setitem__,__delitem__也可以当列表用

python2使用slice实现,python3使用__getitem__实现

"""


class Demo(object):

    def __getitem__(self, index):
        if isinstance(index, slice):
            print("Get slice---------> start: %s, stop: %s, step: %s." \
                  % (str(index.start), str(index.stop), str(index.step)))

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            print("Set slice---------> start: %s, stop: %s, step: %s." \
                  % (str(index.start), str(index.stop), str(index.step)))
            print("\tThe value is:", value)

    def __delitem__(self, index):
        if isinstance(index, slice):
            print("Delete slice------> start: %s, stop: %s, step: %s." \
                  % (str(index.start), str(index.stop), str(index.step)))


obj = Demo()
obj[-1:10]
obj[-1:10:1] = [2, 3, 4, 5]
del obj[-1:10:2]
