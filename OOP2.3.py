with open ('1.txt', 'rt', encoding='utf8') as f:
    result=f.readlines()
 
with open ('2.txt', 'rt', encoding='utf8') as f:
    result2=f.readlines()
 
with open ('3.txt', 'rt', encoding='utf8') as f:
    result3=f.readlines()
 
all_txt=[]
all_txt.append(len(result))
all_txt.append(len(result2))
all_txt.append(len(result3))

all_txt_sorted=sorted(all_txt)
for i in all_txt_sorted:
    print(i)



# print(f 'Строка номер {result2} файла \n Строка номер {result} файла \n Строка номер {result3} файла')        
    
