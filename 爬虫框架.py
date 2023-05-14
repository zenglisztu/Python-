
#爬虫框架

# from urllib.request import urlopen
#
# from bs4 import BeautifulSoup
#
# import xlwings as xw
#
# from datetime import datetime
#
# value_1=[]
#
# r=urlopen('https://www.boc.cn/sourcedb/whpj/')
#
# c=r.read()
#
# bs_obj=BeautifulSoup(c,features='lxml')
#
# t=bs_obj.find_all('table')[1]
#
# all_tr=t.find_all('tr')
#
# all_tr.pop(0)
#
# for r in all_tr :
#     all_td=r.find_all('td')
#     value_1.append(f'{all_td[0].text}卖出:{all_td[4].text}')
#     print(f'{all_td[0].text}卖出:{all_td[4].text}')
#
# tim=datetime.now()
#
# app=xw.App()
#
# app.visible=True
#
# bk=app.books.add()
#
# bk.sheets(1).range('E1').value=tim
#
# bk.sheets(1).range('A1:A300').options(transpose=True).value=value_1
#
# bk.save('d:/dome/外汇牌价.xlsx')
#
# bk.close()
#
# app.quit()
#
# print(tim)


# from urllib import request
# import re

# res=request.urlopen('http://mobile.zol.com.cn/')
# s=res.read().decode('gbk')

# a=re.findall('!--\s*手机图赏\s*-->.*?<!-- end\s*手机图赏\s--',s,re.DOTALL)

# s1=a[0]
# b=re.findall('<img.*?src="(.*?)"',s1)

# for i in b:
#     res=request.urlopen(i)
#     c=res.read()
#     with open(f'd:/dome/中关村手机图赏/{i[-10: ]}','wb') as f:
#         f.write(c)


# from urllib import request
# import re
# import chardet
#
# res=request.urlopen('https://mobile.zol.com.cn/')
# byts=res.read()
# s=byts.decode('gbk')
#
# pic=re.findall(r'<!-- 手机图赏 -->.+?<!-- end 手机图赏 -->',s,re.DOTALL)
#
# li=re.findall(r'<img.*?src="(.*?)"',str(pic))
#
# for i in li :
#     res=request.urlopen(i)
#     c=res.read()
#     with open(f'd:/dome/统计图/{i[-10: ]}','wb') as f :
#         f.write(c)

# import re
# with open('d:/dome/文本文档/客户电话汇编.txt','r',encoding='utf-8') as f :
#     content=f.read()
#
# li=re.findall(r'(\w+)[办，电].+?(\d+)-(\d+)',content)
#
# for s in li :
#
#     s=list(s)
#     if '的' in s[0] :
#         s[0]=s[0].replace('的','')
#     print(s)
#     s.append('\n')
#
#     with open('d:/dome/文本文档/hz.txt','a') as f :
#         f.write(''.join(s))

# import xlwings as xw
# import re
#
# app=xw.App()
# wb=app.books.open('d:/dome/工程概算表格.xlsx')
# content=wb.sheets(1).range('b2:b67').value
# li=[]
# for s in content :
#     su_m=re.findall(r'\d+\.?\d+(?=【)',s)
#
#     for i in su_m :
#         for x in range(len(su_m)) :
#             su_m[x]=float(su_m[x])
#
#     li.append(sum(su_m))
#
# wb.sheets(1).range('c2:c67').options(transpose=True).value=li
#
# wb.save()
# wb.close()
# app.quit()

# import docx
#
# doc=docx.Document('d:/dome/实习总结.docx')
# a=0
# p1=doc.paragraphs
# for s in p1 :
#     s.text=s.text+'\n作者：曾立'
#
# doc.save('d:/dome/实习总结.docx')

# import re
#
# qq=input('请输入QQ号：')
#
# eml=re.sub(r'(\d+)',r'\1@qq.com',qq)
#
# print(eml)
#
# s='Ada13500834532822344332@qq.com'
# import re
# b=re.sub(r'(\D+)(\d{11})(\d+@\w+\.com)',r'姓名：\1 手机：\2 邮箱：\3',s)
# print(b)

# import pandas
# content=pandas.read_excel('d:/dome/2022级班级教材购买发放报表-2022-09-08(1).xlsx','93@22级机械31班')
# print(content)

# import docx
# import re
#
# doc=docx.Document('d:/dome/lx/lx.docx')

# for s in doc.paragraphs :
#     s.text=s.text.replace( u'\xa0' , '' )
#     name=re.findall(r'(\w+)\s*(?=手机)',s.text)
#     print(name)
#     print(s.text)

# import docx
# import re
# import os
#
# root='d:/dome/lx'
# filename=os.listdir(root)
#
# for s in filename :
#     doc=docx.Document(f'{root}/{s}')
#     for i in doc.paragraphs:
#         i.text=i.text+'年龄：保密'
#
#     doc.save(f'{root}/{s}')
#
# import re
# import docx
#
# doc=docx.Document('d:/dome/客户信息文件.docx')
# for s in doc.paragraphs :
#     res=re.sub(r'(?<=-\d)\d+(?=\d)','******',s.text)
#     s.text=res
# doc.save('d:/dome/客户信息文件.docx')

# import re
#
# user_name=input('请输入用户名：')
# p=re.compile(r'^[a-z\d._]+$')
# # tf=re.match(r'^[a-z\d._]+$',user_name)
# tf=p.match(user_name)
# if tf :
#     print('用户名合法')
# else :
#     print('用户名非法！')
#
# print(tf.group(0))

# s=html = '''<title id='ebooksProductTitle' class='a-size-extra-large'>
# Python核心编程（第3版）（异步图书）</title><a class="a-link-normal"
# href="/s/ref=dp_byline_sr_ebooks_1 sort=relevancerank&amp">
# 卫斯理·春(Wesley Chun)</a><span class="a-size-base a-color-price a-color-price">
# ￥29.99</span>'''
# import re
# p=re.compile(r'class.+?>(.+?)<',re.DOTALL)
# cont=p.finditer(s)
# for s in cont :
#     print(s.groups())














































