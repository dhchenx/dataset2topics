# 需要安装 pip install quick-csv
from quickcsv.file import *
import os

list_all_item=read_csv('datasets/list_g20_news.csv')

for item in list_all_item:
    file_id=item['fileId']
    year=item['year']
    #if year=="":
    #    print("year is empty: ",item['area'])
    # 国家
    country = item['area']
    # 全文txt的路径
    text_path=f"datasets/raw_text/text_{file_id}.txt"
    #if not os.path.exists(text_path):
    #    continue
    if not os.path.exists(text_path):
        print(item['area'])
    # 读取全文用作后序处理
    #text=open(text_path,'r',encoding='utf-8').read()
    #print(text_path)
    #print(year)
    #print("TEXT: ",text) # 全文
    print()

