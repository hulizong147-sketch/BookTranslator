import pdfplumber


# 加载一个PDF文件
pdf = pdfplumber.open("./test.pdf")

# print(pdf)
# print(dir(pdf))
# print(pdf.metadata)
# 页数
print(pdf.pages)

page1 = pdf.pages[0]
page2 = pdf.pages[1]

# print(page1.page_number)
# 提取内容
print(page1.extract_text())

# print("=="*50)
# print(page2.images)
print("=="*50)
print(page1.extract_tables())

# img = page2.images[0]
# 左 上 右 下
# page2.crop((img['x0'], img['top'], img['x1'], img['bottom'])).to_image(antialias=True, resolution=1080).save('img1.png')


