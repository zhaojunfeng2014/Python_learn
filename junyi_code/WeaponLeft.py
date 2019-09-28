from pathlib import Path
import pandas as pd
import numpy as np

p = Path()
list1 = list(p.glob("*/*/*/*.csv"))
print(list1)

# 获取包含 'UnitMountWeapons' 的csv 文件
target = []
for file_name in list1:
    if file_name.name.find('UnitMountWeapons') != -1:
        target.append(file_name)
print(target)


# 如果‘state’=0， 那么WeaponRecCurrentLoadCount设置为0
def WeaponLeft(target):
    for file in target[:2]:
        data = pd.read_csv(file, encoding='utf-8-sig')
        data['state'] = np.random.randint(0, 2, data.shape[0])
        for i in data.index:
            if data['state'][i] == 0:
                data.at[i, 'WeaponRecCurrentLoadCount'] = 0
            else:
                if data['WeaponFireState'][i] != '就绪':
                    data.at[i, 'WeaponRecCurrentLoadCount'] = 0
        data.to_csv(file)
