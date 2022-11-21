import torch
import numpy as np
from torch.autograd import Variable


def torch_numpy():
    '''# NOTE torch、numpy的对比'''
    np_data = np.arange(1, 5).reshape(2, 2)
    toc = torch.from_numpy(np_data)
    tensor2array = toc.numpy()  # torch 与 numpy 互相转换

    list_alpha = [1, -3, -223, 100]
    np_alpha = np.array(list_alpha)

    tensor = torch.FloatTensor(list_alpha)
    # 矩阵计算

    res = torch.matmul(toc, toc)
    res_2 = torch.mm(toc, toc)
    # assert list(np.array(res == res_2))

    np_data.dot(np_data)

    toc.dot(toc)


def torch_variable():
    '''variable'''
    tensor = torch.FloatTensor([[1, 2], [3, 4]])
    variable = Variable(tensor, requires_grad=True)  # 搭建一个图纸
    t_out = torch.mean(tensor * tensor)
    v_out = torch.mean(variable * variable)
    v_out.backward()  # 反向传播
    # NOTE  v_out=1/4*sum(var*var)
    variable.grad  # 更新后
