
rows = [['水果', '颜色', '价格（美元）'], ['苹果', '红色', '1.20'], ['香蕉', '黄色', '0.50'], ['橙子', '橙色', '0.80'], ['草莓', '红色', '2.50'], ['蓝莓', '蓝色', '3.00'], ['猕猴桃', '绿色', '1.00'], ['芒果', '橙色', '1.50'], ['葡萄', '紫色', '2.00']]

header_row = rows[0]
body_row = rows[1:]
# print(body_row)
# 组装md格式
header = " | ".join(cell for cell in header_row)
# print(header)

tr = " | ".join(['----']*len(header_row))
# print(tr)

t_body = ''
for row in body_row:
    # print(row)
    r = [" | ".join(row)]
    t_body += '| ' + " | ".join(r) + ' | ' + '\n'
print(t_body)

