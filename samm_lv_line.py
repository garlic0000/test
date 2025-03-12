import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.ticker import MaxNLocator  # 导入 MaxNLocator

# 定义数据
x = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])  # X轴（表头）
y_values = {
    0.01: [0.3756, 0.3815, 0.3986, 0.3821, 0.3841, 0.3859, 0.3863, 0.3857, 0.3811],
    0.03: [0.3767, 0.3815, 0.3940, 0.3822, 0.3804, 0.3846, 0.3818, 0.3799, 0.3792],
    0.05: [0.3756, 0.3811, 0.3943, 0.3805, 0.3813, 0.3871, 0.3863, 0.3814, 0.3789],
    0.07: [0.3707, 0.3843, 0.3986, 0.3782, 0.3774, 0.3894, 0.3884, 0.3792, 0.3792],
    0.09: [0.3733, 0.3800, 0.3943, 0.3807, 0.3839, 0.3879, 0.3796, 0.3770, 0.3803]
}

# 生成易于区分的灰阶颜色（增加颜色间对比度）
num_lines = len(y_values)
gray_colors = [cm.Greys(0.15 + 0.85 * i / (num_lines - 1)) for i in range(num_lines)]  # 从深灰到浅灰

# 绘制折线图
plt.figure(figsize=(10, 6), facecolor='white')  # 调整尺寸以填满空间

for (key, y), color in zip(y_values.items(), gray_colors):
    plt.plot(x, y, marker='o', markersize=5, linewidth=2, color=color, markerfacecolor=color, markeredgecolor=color, label=f'{key}')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimSun']  # 适用于Windows
plt.rcParams["mathtext.fontset"] = "stix"  # 使用 STIX 字体集（包含 Times New Roman）
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# 设置轴标签并加大字号
plt.xlabel(r'初始丢弃率$\mathit{p}_{\mathrm{0}}$', fontsize=22)

plt.ylabel('F1分数', fontsize=22)

# 调整刻度大小
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

# 使用 MaxNLocator 控制刻度间隔，使其更紧密
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True, prune='both', nbins=10))
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6))

# 设置刻度朝内，四边都有刻度
plt.tick_params(axis='both', direction='in', top=True, right=True, length=8, width=2, labelsize=20)

# 设置图例并加大字号
plt.legend(title=r'最小丢弃率$\mathit{p}_{\mathrm{min}}$', title_fontsize=20, fontsize=18, loc='upper right')

# 关闭网格
plt.grid(False)

# 调整图像边距以填满整个画布
plt.tight_layout()

# 显示图表
plt.show()
