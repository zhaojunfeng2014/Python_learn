def a():
    param = 'b'
    print(param)


if __name__ == '__main__':
    param = 'a'  # 这里使用param,导致line 2报shadows_name警告
    a()
