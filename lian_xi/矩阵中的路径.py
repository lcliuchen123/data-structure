
# 递归寻找矩阵路径

# 解法一：只能AC 80%。存在问题
# def hasPath(matrix, rows, cols, path):
#     # write code here
#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i*cols+j] == path[0]:
#                 print("%d, %d" %(i,j))
#                 if find(list(matrix),rows,cols,path[1:],i,j):
#                     return True
#     return False
# 
# 
# def find(matrix,rows,cols,path,i,j):
#     if not path:
#         return True
#     print("path: ", path)
#     matrix[i*cols+j]='0'
#     if j+1<cols and matrix[i*cols+j+1]==path[0]:
#         print("right")
#         return find(matrix,rows,cols,path[1:],i,j+1)
#     elif j-1>=0 and matrix[i*cols+j-1]==path[0]:
#         print("left")
#         return find(matrix,rows,cols,path[1:],i,j-1)
#     elif i+1<rows and matrix[(i+1)*cols+j]==path[0]:
#         print("low")
#         return find(matrix,rows,cols,path[1:],i+1,j)
#     elif i-1>=0 and matrix[(i-1)*cols+j]==path[0]:
#         print("high")
#         return find(matrix,rows,cols,path[1:],i-1,j)
#     else:
#         return False


# 解法二
def hasPath(matrix, rows, cols, path):
    # write code here
    if not matrix:
        return False
    if not path:
        return True

    x = [list(matrix[cols*i:cols*i+cols]) for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            print("%d, %d" % (i, j))
            if exist_helper(x, i, j, path):
                return True
    return False


def exist_helper(matrix, i, j, p):
    print("path: ", p)
    if matrix[i][j] == p[0]:
        if not p[1:]:
            return True
        matrix[i][j] = ''
        if i > 0 and exist_helper(matrix, i-1, j, p[1:]):
            print("high")
            return True
        if i < len(matrix)-1 and  exist_helper(matrix, i+1, j ,p[1:]):
            print("low")
            return True
        if j > 0 and  exist_helper(matrix, i, j-1, p[1:]):
            print("left")
            return True
        if j < len(matrix[0])-1 and  exist_helper(matrix, i, j+1, p[1:]):
            print("right")
            return True
        matrix[i][j] = p[0]
        return False
    else:
        return False
    
    
if __name__ == "__main__":
    #解法一： S先往上再往左可以得到path，但是如果往下就无法得到path。
    matrix = "ABCE" \
             "SFCS" \
             "ADEE"
    rows = 3
    cols = 4
    path = "SEC"
    res = hasPath(matrix,rows,cols,path)
    print(res)

