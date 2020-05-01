"""
hash(param) 参数只能接收不可变类型
"""
print("hash((1,))%s" % hash((1,)))  # 元组是不可变类型,可进行hash
