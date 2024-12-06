import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(12, 10))

# 添加矩形框来表示每个操作
rects = [
    mpatches.FancyBboxPatch((0.1, 0.85), 0.8, 0.1, boxstyle="round,pad=0.05", ec="black", fc="lightblue", lw=1),
    mpatches.FancyBboxPatch((0.1, 0.7), 0.8, 0.1, boxstyle="round,pad=0.05", ec="black", fc="lightgreen", lw=1),
    mpatches.FancyBboxPatch((0.1, 0.55), 0.8, 0.1, boxstyle="round,pad=0.05", ec="black", fc="lightyellow", lw=1),
    mpatches.FancyBboxPatch((0.1, 0.4), 0.8, 0.1, boxstyle="round,pad=0.05", ec="black", fc="lightpink", lw=1),
    mpatches.FancyBboxPatch((0.1, 0.25), 0.8, 0.1, boxstyle="round,pad=0.05", ec="black", fc="lightcoral", lw=1),
    mpatches.FancyBboxPatch((0.1, 0.1), 0.8, 0.1, boxstyle="round,pad=0.05", ec="black", fc="lightseagreen", lw=1)
]

# 将矩形框添加到图中
for rect in rects:
    ax.add_patch(rect)

# 添加文本
ax.text(0.5, 0.92, "输入特征矩阵 X (B x N x F)", ha="center", va="center", fontsize=12)
ax.text(0.5, 0.77, "线性变换 (Wh)", ha="center", va="center", fontsize=12)
ax.text(0.5, 0.62, "Wh 重塑 (B x N x heads x F)", ha="center", va="center", fontsize=12)
ax.text(0.5, 0.47, "Wh 重复计算注意力系数 (B x N x heads x N x F)", ha="center", va="center", fontsize=12)
ax.text(0.5, 0.32, "Softmax 归一化注意力系数 (B x N x heads x N)", ha="center", va="center", fontsize=12)
ax.text(0.5, 0.17, "加权聚合后的特征 (B x N x heads * F)", ha="center", va="center", fontsize=12)

# 绘制箭头
ax.annotate("", xy=(0.5, 0.85), xytext=(0.5, 0.77), arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(0.5, 0.7), xytext=(0.5, 0.62), arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(0.5, 0.55), xytext=(0.5, 0.47), arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(0.5, 0.4), xytext=(0.5, 0.32), arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(0.5, 0.25), xytext=(0.5, 0.17), arrowprops=dict(arrowstyle="->", lw=2))

# 设置图形样式
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
