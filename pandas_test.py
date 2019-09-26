# -*- coding: utf-8 -*-
import pandas as pd
import os


# 获取文件路径
def get_file(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_name = os.path.join(root, file)
            file_list.append(file_name)
    return file_list


# 处理并保存数据
def data_chu(file_path, out_path):
    data = pd.read_csv(file_path)
    data['MissionID']=data['MissionID'].apply(str)
    data['Escort']=data['Escort'].apply(str)
    data['Tag']= data['MissionID']+ data['Escort']
    word_list1=[]
    word2num=[]
    for word in data['Tag']:
        if word not in word_list1:
            word_list1.append(word)
            word2num.append(word_list1.index(word)) # 如果word 不在列表中，添加进列表，并在一个新列表中添加 对应的索引
        else:
            word2num.append(word_list1.index(word))
    data['new_colu']= word2num # 这个生成的索引 变成csv 文件的一个新的列
    del data['Tag']
    data.to_csv(out_path)


if __name__ == '__main__':
    dest_path = r'C:\Users\Lenovo\Desktop\2'
    file_list = get_file(r'C:\Users\Lenovo\Desktop\1')
    for file_path in file_list:
        file_name = file_path.split("\\")[-1]  # 取得文件名称
        out_path = os.path.join(dest_path, file_name)
        data_chu(file_path, out_path)
