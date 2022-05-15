import os
from functools import reduce
from string import ascii_lowercase
from string import digits


class Solution(object):
    
    def temp(slef,str_data):
        dict_str={}
        for i in str_data:
            dict_str[i]=dict_str.get(i,0)+1
        return dict_str
    
    
    def main_in(self):
        dict_str=self.temp("AABBCCCADDDDDDDDDDD")
        str_count_data=""
        for k,v in dict_str.items():
            str_count_data+=k+str(v)
        print(str_count_data)


        
        
if __name__ == "__main__":
    s = Solution()
    s.main_in()
    