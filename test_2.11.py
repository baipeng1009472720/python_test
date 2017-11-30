# utf-8
import numpy as np
import time

# 向量化和普通for的计算比较
a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a, b)

toc = time.time()
print(c)
print("vector :" + str(1000 * (toc - tic)) + "mc")

c = 0
tic = time.time()

for i in range(1000000):
    c += a[i] * b[i]

toc = time.time()
print(c)
print("vector :" + str(1000 * (toc - tic)) + "mc")
# 事实证明快了3~4百倍

# cpu 和 gpu 都有并行化的指令，simd指令，单指令处理多数据流
# numpy 数据并行化的计算