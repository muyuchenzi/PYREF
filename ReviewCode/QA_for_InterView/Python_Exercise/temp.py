import os
from functools import reduce
class Solution(object):
    
    @staticmethod
    def reverse(x):
        if -10<x<10:
            return x
        str_x=str(x)
        if str_x[0]!='-':
            res=int(str_x[::-1])
        else:
            str_x=str_x[1:][::-1]
            res=-int(str_x)
        return res if -2147483648<x<2147483647 else 0

    @staticmethod
    def get_pyfiles(dir_path,suffix):
        res=[]
        for root,dir,file_name in os.walk(dir_path):
            res.append(file_name)
        
        file_list=[]
        for r in res:
            for i in r:
                file_list.append(i)
        
        final_res=[]
        for file in file_list:
            if file.endswith(suffix):
                final_res.append(file)
        print(final_res)
    @staticmethod
    def sum(num_list):
        print(sum(num_list))
        print(reduce(lambda x,y :x+y,num_list))
if __name__=="__main__":
    s=Solution()
    result=s.reverse(-120)
    print(result)
    dir_path=r'E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Exercise'
    s.get_pyfiles(dir_path,'.py')
    s.sum([i for i in range(200)])

            
