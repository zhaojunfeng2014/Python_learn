import os

my_list = os.listdir(r"H:\Glodon\Data\xinhangcheng_proj\xinhangcheng_bim\TRANSFER\test\LX_0107_1_indoor")

print(my_list)

path = 'H:/Glodon/Data/xinhangcheng_proj/xinhangcheng_bim/TRANSFER/test/LX_0107_1_indoor'

file_path = os.path.join(path, "bimMaterial.json")

print(file_path)

exists = os.path.exists(file_path)

print(exists)

splits = os.path.splitext("c:\\1\\a.txt")
print(splits)
