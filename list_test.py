a_list = ['a', 'b', 'c', 'hello']

print('a' in a_list)
# True
print('a' not in a_list)
# False
print(a_list.count('d'))
# 0
print(a_list.index('b'))  # 如果找到返回索引，如果没有找到报错，抛异常
# 1

