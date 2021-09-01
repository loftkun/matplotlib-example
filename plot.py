# tsvを読み込む
import sys
import enum
f = open("test.tsv", 'r')
lines = f.readlines()
f.close()
print("getsizeof : {}".format(sys.getsizeof(lines))) # 2857936 = 2.7MBくらい

# ヘッダ行を取り除く
lines.pop(0)

# インデックスの定義
class I(enum.IntEnum):
    phi1       = 0
    PHI        = 1
    phi2       = 2
    x          = 3
    y          = 4
    IQ         = 5
    CI         = 6
    Fit        = 7
    Grain_ID   = 8
    edge       = 9
    phase_name = 10

# tsvからグラフ描画に必要なデータのみ抽出
import numpy as np
X0 , Y0 , Z0 = np.empty(0), np.empty(0) ,np.empty(0)
X1 , Y1 , Z1 = np.empty(0), np.empty(0) ,np.empty(0)
X2 , Y2 , Z2 = np.empty(0), np.empty(0) ,np.empty(0)
n = 0
for line in lines:
    n = n + 1
    if n % 1000 != 1:
        continue # 1/1000にサンプリング
    columns = line.strip().split(sep="\t")

    x = columns[I.x]
    y = columns[I.y]
    grain_id = columns[I.Grain_ID]

    # 本来は Grain_ID の数に合わせて Xn を用意するべき
    if grain_id == "0":
        X0 = np.append(X0, float(x))
        Y0 = np.append(Y0, float(y))
        Z0 = np.append(Z0, float(grain_id))
    elif grain_id == "1":
        X1 = np.append(X1, float(x))
        Y1 = np.append(Y1, float(y))
        Z1 = np.append(Z1, float(grain_id))
    elif grain_id == "2":
        X2 = np.append(X2, float(x))
        Y2 = np.append(Y2, float(y))
        Z2 = np.append(Z2, float(grain_id))

import matplotlib.pyplot as plt

# 2D scatterplot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.scatter(X0, Y0, c='blue', label='Grain_ID 0')
ax.scatter(X1, Y1, c='green', label='Grain_ID 1')
ax.scatter(X2, Y2, c='red', label='Grain_ID 2')

ax.set_title('2d scatter plot')
ax.set_xlabel('x')
ax.set_ylabel('y')

ax.grid(True)
ax.legend(loc='upper left')
plt.show()

# 3D scatterplot
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# label
ax.set_xlabel("x [microns]")
ax.set_ylabel("y [microns]")
ax.set_zlabel("Grain ID")

# show
ax.scatter(X0, Y0, Z0, c='blue')
ax.scatter(X1, Y1, Z1, c='green')
ax.scatter(X2, Y2, Z2, c='red')
plt.show()