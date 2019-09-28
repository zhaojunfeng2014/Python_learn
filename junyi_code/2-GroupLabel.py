# -*- coding: utf-8 -*-
# 有问题：不同的组合最后打的数字标签不同，但是for 循环只是打了一个文件的标签，但是数据确实要打所有不同结果的标签
import pandas as pd
import os
from pathlib import Path

this_path = Path('.')
csv_file_list = list(this_path.glob("*/*/*/*.csv"))  # 当前目录下所有文件，包括文件夹内的
print(csv_file_list)
Tag = set()
nowpath = os.getcwd()
target_path = []
for file_name in csv_file_list:
    if file_name.name.find('UnitPositions') != -1:
        target_path.append(file_name)
        data = pd.read_csv(file_name, encoding='utf_8_sig', engine='python')
        data['MissionID'] = data['MissionID'].apply(str)
        data['Escort'] = data['Escort'].apply(str)
        data['Tag'] = data['MissionID'] + data['Escort']
        s = set(data['Tag'])
        Tag = Tag.union(s)
        data.to_csv(file_name, index=False, encoding="utf_8_sig")
s = list(Tag)
# word2num = []
for file_name in target_path[2:10]:
    word2num = []
    print('文件{}开始变换'.format(file_name))
    data = pd.read_csv(file_name, encoding='utf_8_sig', engine='python')
    for word in data['Tag']:
        word2num.append(s.index(word))

    data['Group'] = word2num
    del data['Tag']
    print('文件{}变换完成'.format(file_name))
    data.to_csv(file_name, index=False, encoding="utf_8_sig")

    # word_list1 = []
    # word2num = []
    # if file_name.name.find('UnitPositions') != -1:
    #     data = pd.read_csv(file_name, encoding='utf_8_sig', engine='python')

    #     data['Tag'] = data['MissionID'] + data['Escort']
    #     for word in data['Tag']:
    #         if word not in word_list1:
    #             word_list1.append(word)
    #         word2num.append(word_list1.index(word))  # 如果word 不在列表中，添加进列表，并在一个新列表中添加 对应的索引
    #
    #     data['Group'] = word2num  # 这个生成的索引 变成csv 文件的一个新的列
    #     del data['Tag']
    #     data.to_csv(file_name, index=False, encoding="utf_8_sig")

## 获取文件路径
# def get_file(path):
# target_path = []
# for root, dirs, files in os.walk(path):
# for file in files:
# file_name = os.path.join(root, file)
# if 'UnitPositions' in file_name:
# target_path.append(file_name)
# return target_path


# 处理并保存数据
# def data_chu(in_path, out_path):
# print('开始处理文件{}'.format(in_path))
# data = pd.read_csv(in_path)
# data['MissionID'] = data['MissionID'].apply(str)
# data['Escort'] = data['Escort'].apply(str)
# data['Tag'] = data['MissionID'] + data['Escort']


# word_list1 = []
# word2num = []
# for word in data['Tag']:
# if word not in word_list1:
# word_list1.append(word)
# word2num.append(word_list1.index(word))  # 如果word 不在列表中，添加进列表，并在一个新列表中添加 对应的索引

# data['Group'] = word2num  # 这个生成的索引 变成csv 文件的一个新的列
# del data['Tag']
# data.to_csv(out_path, encoding="utf_8_sig")
# print('开始处理文件{}'.format(in_path))

# if __name__ == '__main__':
# target_path = get_file(r'C:\Users\sean\Desktop\1')
# for in_path in target_path:
# out_path = in_path
# data_chu(in_path, out_path)
