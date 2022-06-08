# 神经网络的原理,数学方法,构建,训练
# 应用 图像识别，
import random
import torch
import numpy as np
import copy

# 两者切换
np_data = np.arange(6).reshape((2, 3))
torch_data = torch.from_numpy(np_data)
tensor2array = torch_data.numpy()
#
data = [1, -2, -4, -2]
tesor_alpha = torch.from_numpy(np.array(data))
nump_data = np.abs(data)
tensor_data = torch.abs(tesor_alpha)

# 矩阵相乘
data = [[1, 2], [3, 4]]
res_data = np.array(copy.deepcopy(data))
tensor = torch.from_numpy(copy.deepcopy(np.array(data)))
res_data = np.dot(res_data, res_data)
tesor_data = torch.matmul(tensor, tensor)
