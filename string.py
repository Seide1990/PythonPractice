string='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox , bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'
metnin_sayi=len(string)

simvollarin_sayi=0
herflerin_sayi=0
reqemlerin_sayi=0
bosluqlarin_sayi=0
saitlerin_sayi=0
samitlerin_sayi=0
for i in string:
    if ord(i)==32:
        bosluqlarin_sayi+=1
    elif ((ord(i)>=32 and ord(i)<=47) or (ord(i)>=58 and ord(i)<=64) or (ord(i)>=91 and ord(i)<=96) or (ord(i)>=123 and ord(i)<=127 ) ):
        simvollarin_sayi+=1
    elif(ord(i)>=48 and ord(i)<=57):
        reqemlerin_sayi+=1
    else:
        
        herflerin_sayi+=1
#------------metndeki saitlerin ve samitlerin tapilmasi 1-ci usul-------
for i in string:
    if i=='a' or i=='ı'  or i=='o'  or i=='u' or i=='e' or i=='ə' or i=='i'or i=='ö' or i=='ü' or i=='A' or i=='I'  or i=='O'  or i=='U' or i=='E' or i=='Ə' or i=='İ'or i=='Ö' or i=='Ü' :
  
        saitlerin_sayi+=1
    else:
        samitlerin_sayi+=1

samitlerin_sayi=samitlerin_sayi-bosluqlarin_sayi-reqemlerin_sayi-simvollarin_sayi
#------------metndeki saitlerin ve samitlerin tapilmasi 2-ci usul------------
saitlerin_sayi1=0
samitlerin_sayi1=0
massiv=['a','ı','o','u','e','ə','i','ö','ü','A','I','O','U','E','Ə','İ','Ö','Ü']
for a in  range(0,18):
     for i in string:
         if i==massiv[a]:
             saitlerin_sayi1+=1

samitlerin_sayi1=metnin_sayi-saitlerin_sayi1-bosluqlarin_sayi-reqemlerin_sayi-simvollarin_sayi
#--------------metni sozlere ayirib massiv yaradan proqram-----
sozler=[]
sozler=string.split(' ')
for i in sozler:
    if (i=='.' or i==',' ):
        sozler.remove(i)
#---------------- vergule gore ayirma---------
word=[]
for i in sozler:
    word.append(i)
word=string.split(',')
#----------------son iki sozu silen proqram-----

yeni=[]
for i in sozler:
    yeni.append(i)
yeni.remove(yeni[len(yeni)-1])
yeni.remove(yeni[len(yeni)-1])



   

#--------------neticelerin capi-----------------------------
print('metndeki reqemlerin sayi=  ', reqemlerin_sayi)
print('metndeki herflerin sayi=  ', herflerin_sayi)
print('metndeki simvollarin sayi= ', simvollarin_sayi)
print('metndeki bosluqlarin sayi= ', bosluqlarin_sayi)
print('metndeki saitlerin sayi 1-ci usul= ', saitlerin_sayi)
print('metndeki samitlerin sayi 1-ci usul= ', samitlerin_sayi)
print('metndeki saitlerin sayi 2-ci usul= ', saitlerin_sayi1)
print('metndeki samitlerin sayi 2-ci usul= ', samitlerin_sayi1)
print('sozler massivi =  ',sozler)
print('vergule gore ayirma =  ',word)
print('son ikisi silinmis massiv =  ',yeni)
#-------------------------------axtaris------------------------
while True:
    search=input('tapmaq istediyiniz sozu daxil edin  ')
    find=1
    for i in sozler:
        if search==i: 
            find=2
        elif search==i.upper():
            find=3
            
    if find==2:
         print('metnin icerisinde', search ,' kelimesine rast gelindi')
    elif find==3:
         print(search,' kelimesini axtarirsiniz???')
    else:
         print('metnin icerisinde',search ,'kelimesine rast gelinmedi')

    davam=input('yeni axtaris etmek isteyirsiniz? BELI   /   XEYR  ')
    if davam=='BELI':
        continue
    else:
        break

