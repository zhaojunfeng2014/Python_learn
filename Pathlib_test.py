from pathlib import Path

p = Path()

print(p.resolve())  # 获得绝对路径

p = Path(r"Z:\bin\batch_rvt_preprocess\simplify_model_cfg\yongxinghe_6_outdoor_s_simplify_model.conf.txt")
print(p.name)  # 完整文件名

print(p.stem)  # 去掉后缀的文件名

print(p.suffix)  # 获得后缀

print(p.suffixes)  # 获得多个后缀

print(p.parent)  # 获得父目录

for i in p.parents:  # 返回一个iterable, 每一级的父目录
    print(i)

print(p.parts)  # 把路径分割为一个元组

p = Path(r"H:\Glodon\Data\xinhangcheng_proj\xinhangcheng_max\EXPORT\test\an_zhi_fang_2\obj")
p = Path(p, "JZ0205010701zhongxiaoxue")
print(p.exists())  # 判断文件是否存在
print(p.is_file())  # 判断是否是文件
print(p.is_dir())  # 判断是否是目录

p = Path(r"H:\Glodon\Data\xinhangcheng_proj\xinhangcheng_max\EXPORT\test\an_zhi_fang_2")
for i in p.iterdir():  # 返回一个迭代器，此目录包含的所有子目录或文件
    print(i)

for item in p.glob('*'):
    print(item)

print("rglob test")
for item in p.rglob('*'):  # 相当于os.walk, 会递归找到所有的子目录和文件
    print(item)

p = Path(r"H:\Glodon\Data\xinhangcheng_proj\xinhangcheng_max\EXPORT\test\1")
p.mkdir(exist_ok=True)  # 创建文件目录，前提是父目录存在 当目录已存在时，如果exist_ok=True,不会报错，如果exist_ok=False，则会报错



