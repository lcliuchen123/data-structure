
import numpy as np

def max_common_str(str1,str2):
    if str1 == '' or str2 == '':
        return
    length1= len(str1)
    length2=len(str2)
    result = np.zeros((length1,length2))
    max_len=0
    max_end=0
    for i in range(length1):
        for j in range(length2):
            if str1[i] == str2[j]:
                if i==0 or j==0:
                    result[i][j] = 1
                else:
                    result[i][j]=result[i-1][j-1]+1
            else:
                result[i][j]=0
            if result[i][j]>max_len:
                max_len=result[i][j]
                max_end=i
    print(int(max_end-max_len+1))

    return max_len,max_end,str1[int(max_end-max_len+1):max_end+1]


if __name__=="__main__":
    str1 = 'acbcbcef'
    str2 = 'abcbced'
    print(max_common_str(str1,str2))
