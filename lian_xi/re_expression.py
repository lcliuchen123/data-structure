

import re
# \D = '[^0-9] 非数字

s = "我手机号815107103269,他手机号151072232690"
re_cell = re.compile("(?:^|\D)(1[3|4|5|6|7|8|9][0-9]\d{8})(?:$|\D)")
print(re_cell.findall(s))

for cell in re_cell.finditer(s):
    print(cell.group(1))

# 数据格式
l=[
    {""}
]