#奇异值分解
#用于高阶矩阵的降维
import numpy as np
import matplotlib.pyplot as plt
la=np.linalg
words=["I","like","enjoy","deep","learning","NLP","flying","."]
X=np.array([[0,2,1,0,0,0,0,0],
           [2,0,0,1,0,1,0,0],
           [1,0,0,0,0,0,1,0],
           [0,1,0,0,1,0,0,0],
           [0,0,0,1,0,0,0,1],
           [0,1,0,0,0,0,0,1],
           [0,0,1,0,0,0,0,1],
           [0,0,0,0,1,1,1,0]])
U,s,Vh=la.svd(X,full_matrices=False)

#可视化处理
for i in range(len(words)):
    plt.text(U[i,0],U[i,1],words[i])
plt.show()
