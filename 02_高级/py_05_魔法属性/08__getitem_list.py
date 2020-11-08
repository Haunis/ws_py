"""
https://www.jianshu.com/p/c48e6e903c38

把类当做列表用

类实现了__getitem,__setitem__,__delitem__也可以当列表用

python2使用slice实现,python3使用__getitem__实现

"""


class Demo(object):

    def __getitem__(self, index):
        print("getitem index:", index)  # slice(-1, 10, None);index是个slice类
        if isinstance(index, slice):
            print("__getitem__ slice---------> start: %s, stop: %s, step: %s." \
                  % (str(index.start), str(index.stop), str(index.step)))

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            print("__setitem__ slice---------> start: %s, stop: %s, step: %s." \
                  % (str(index.start), str(index.stop), str(index.step)))
            print("\tThe value is:", value)

    def __delitem__(self, index):
        if isinstance(index, slice):
            print("__delitem__ slice------> start: %s, stop: %s, step: %s." \
                  % (str(index.start), str(index.stop), str(index.step)))


obj = Demo()
obj[-1:10]  # 调用__getitem__
obj[-1:10:1] = [2, 3, 4, 5]  # 调用__setitem__
del obj[-1:10:2]  # 调用__delitem__
