import os
from quickcsv.file import *

root_path="datasets/csv_files"
list_all_item=[]

for csv_file in os.listdir(root_path):
    print(csv_file)
    encoding='utf-8'
    #if '德国' in csv_file: # 由于预处理数据有问题，缺德国、意大利
    #    encoding='utf-8'
     #   continue # 略过
    list_item=quick_read_csv_model(f"datasets/csv_files/{csv_file}",encoding=encoding)
    for idx in range(0,len(list_item)):
        list_item[idx]['area']=list_item[idx]['area'].strip()
    print(list_item[0])
    list_all_item+=list_item
    print("Len = ",len(list_item))
    print()

write_csv("datasets/list_g20_news.csv",list_all_item)

countries=[]
empty_count=0
for item in list_all_item:
    if item['area']=='':
        empty_count+=1
        continue
    if item['area'] not in countries:
        countries.append(item['area'])
print("empty count = ",empty_count)

print(len(countries))
print(countries)


