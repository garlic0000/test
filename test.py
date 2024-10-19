import pandas as pd
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 黑体

# Initialize an empty defaultdict to hold the merged data
merged_data = defaultdict(int)

# 将数据转换为字典
data_dict = {
    'AU1': 23,
    'AU2': 29,
    'AU4': 123,
    'AU5': 15,
    'AU6': 46,
    'AU7': 32,
    'AU9': 10,
    'AU10': 3,
    'AU11': 1,
    'AU12': 130,
    'AU14': 51,
    'AU15': 7,
    'AU17': 6,
    'AU18': 7,
    'AU19': 1,
    'AU20': 2,
    'AU21': 2,
    'AU23': 1,
    'AU24': 25,
    'AU25': 8,
    'AU28': 1,
    'AU30': 2,
    'AU34': 1,
    'AU38': 8,
    'AU39': 4,
    'AU42': 1,
    'AU43': 21,
    'AU45': 4,
    'AU62': 1
}

data_dict1 = {
    'AU1': 24,
    'AU2': 55,
    'AU3': 1,
    'AU4': 75,
    'AU5': 40,
    'AU6': 39,
    'AU7': 123,
    'AU8': 6,
    'AU9': 9,
    'AU10': 38,
    'AU11': 5,
    'AU12': 131,
    'AU13': 6,
    'AU14': 70,
    'AU15': 18,
    'AU16': 1,
    'AU17': 32,
    'AU18': 14,
    'AU19': 5,
    'AU20': 16,
    'AU21': 1,
    'AU23': 13,
    'AU24': 62,
    'AU25': 41,
    'AU26': 36,
    'AU27': 1,
    'AU30': 6,
    'AU31': 12,
    'AU33': 1,
    'AU37': 1,
    'AU38': 12,
    'AU39': 10,
    'AU42': 1,
    'AU43': 17,
    'AU45': 2,
    'AU50': 1,
    'AU51': 1,
    'AU52': 1,
    'AU53': 1,
    'AU54': 5,
    'AU55': 2,
    'AU56': 4,
    'AU58': 2,
    'AU61': 8,
    'AU62': 7,
    'AU63': 1,
    'AU64': 2,
    'AU80': 4,
    'AU81': 2,
    'AU85': 2
}
all_data_dict = {'AU1': 47, 'AU2': 84, 'AU4': 198, 'AU5': 55, 'AU6': 85, 'AU7': 155, 'AU9': 19, 'AU10': 41,
                 'AU11': 6, 'AU12': 261, 'AU14': 121, 'AU15': 25, 'AU17': 38, 'AU18': 21, 'AU19': 6, 'AU20': 18,
                 'AU21': 3, 'AU23': 14, 'AU24': 87, 'AU25': 49, 'AU28': 1, 'AU30': 8, 'AU34': 1, 'AU38': 20,
                 'AU39': 14, 'AU42': 2, 'AU43': 38, 'AU45': 6, 'AU62': 8, 'AU3': 1, 'AU8': 6, 'AU13': 6,
                 'AU16': 1, 'AU26': 36, 'AU27': 1, 'AU31': 12, 'AU33': 1, 'AU37': 1, 'AU50': 1, 'AU51': 1,
                 'AU52': 1, 'AU53': 1, 'AU54': 5, 'AU55': 2, 'AU56': 4, 'AU58': 2, 'AU61': 8, 'AU63': 1,
                 'AU64': 2, 'AU80': 4, 'AU81': 2, 'AU85': 2}

import matplotlib.pyplot as plt

# 原始数据字典
all_data_dict = {
    'AU1': 47, 'AU2': 84, 'AU4': 198, 'AU5': 55, 'AU6': 85,
    'AU7': 155, 'AU9': 19, 'AU10': 41, 'AU11': 6, 'AU12': 261,
    'AU14': 121, 'AU15': 25, 'AU17': 38, 'AU18': 21, 'AU19': 6,
    'AU20': 18, 'AU21': 3, 'AU23': 14, 'AU24': 87, 'AU25': 49,
    'AU28': 1, 'AU30': 8, 'AU34': 1, 'AU38': 20, 'AU39': 14,
    'AU42': 2, 'AU43': 38, 'AU45': 6, 'AU62': 8, 'AU3': 1,
    'AU8': 6, 'AU13': 6, 'AU16': 1, 'AU26': 36, 'AU27': 1,
    'AU31': 12, 'AU33': 1, 'AU37': 1, 'AU50': 1, 'AU51': 1,
    'AU52': 1, 'AU53': 1, 'AU54': 5, 'AU55': 2, 'AU56': 4,
    'AU58': 2, 'AU61': 8, 'AU63': 1, 'AU64': 2, 'AU80': 4,
    'AU81': 2, 'AU85': 2
}

# 将字典按值降序排序
sorted_items = sorted(all_data_dict.items(), key=lambda x: x[1], reverse=True)

# 提取前50个（如果字典中项少于50个，就提取所有项）
top_50_items = sorted_items[:26]

# 解包数据
keys, values = zip(*top_50_items)

# 绘制柱状图
plt.figure(figsize=(12, 8))
plt.bar(keys, values, color='#3D64AC')
plt.xlabel('动作单元 (AU)', fontsize=14)
plt.ylabel('计数', fontsize=14)
plt.title('前50个动作单元计数', fontsize=16)
plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()

