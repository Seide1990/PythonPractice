numbers=[1,2,3,6,7,8,23,78,34,12]
#---Ədədlərin cəmini tapan metod -----
summa=0
for i in numbers:
    summa+=i

#-----Ədədləri böyükdən kiçiyə doğru sıralamaq---
new_numbers=[]
new_numbers=[new for new in numbers]
second_numbers=[]
maximum=0
count=len(new_numbers)
for i in range(0,count):
    maxs=max(new_numbers)
    second_numbers.append(maxs)
    new_numbers.remove(maxs)
#--------Ədədlər arasında rəqəmlərinin cəmi ən böyük olan ədədin tapilmasi
numbers=[1,2,3,6,7,8,23,78,34,12]
cemi=[]
topla=0
max_numbers=0
for i in numbers:
    topla=0
    for a in str(i):
        topla+=int(a)
    cemi.append(topla)
    maxs=max(cemi)
    if maxs>max_numbers:
        max_eded=i
        max_numbers=maxs
#----- Ədədlərin kvadratlarının olduğu yeni bir massiv yaradan metod yazın---
numbers_kv=[]
for i in numbers:
    numbers_kv.append(i*i)
#-----Tək ədədlərin cəmini tapan ve tek ededleri massive yigan proqram---
tek_eded=0
tek_ededler=[]
for i in numbers:
    if i%2!=0:
        tek_eded+=i
        tek_ededler.append(i)
#----Daxilində 3 rəqəmi olan neçə ədəd olduğunu ekrana çap edən metod yazın---
numbers=[1,2,3,6,7,8,23,78,34,12]
count=0
for i in numbers:
    for a in str(i):
        if a=='3':
            count+=1
            break




print('verilen massiv=   ',numbers)
print('massivin elelmentlerinin cemi=  ',summa)        
print('massivin boyukden kiciye duzulmesi =  ',second_numbers)
print('massiv elm req cemi en boyuk olan eded =  ',max_eded,'  reqemlerinin cemi ise  = ',max_numbers)
print('massivin elementlerinin kvadratlari massivi =  ',numbers_kv)
print('massivdeki tek ededlerin cemi =  ',tek_eded)
print('massivde 3 reqemi istifade edilmis reqemlerin sayi =  ',count)
print('massivin tek ededlerinde yigilmis yeni massiv =   ',tek_ededler)