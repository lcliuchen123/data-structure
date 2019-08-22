
# 链接：https://www.nowcoder.com/questionTerminal/9b4c81a02cd34f76be2659fa0d54342a
# 来源：牛客网
# 思路：一圈一圈的循环


def printMatrix(matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            print("matrix: ", matrix)
            print("res: ", res)
            if matrix and matrix[0]: #防止matrix = [[],[]]，即matrix不为空，但是matrix[0]为空
            # if matrix:
                for row in matrix:
                    res.append(row.pop())
                    print("res_2: ", res)
            if matrix:
                res += matrix.pop()[::-1]  # 最下面一行，倒序输出
                print("res_3: ",res)
            if matrix and matrix[0]:
                print("matrix: ",matrix)
            # if matrix:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
                    print("res_4: ", res)
        return res


# array = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
array = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
print(printMatrix(array))