#1
import random
print("B  I  N  G  O")
for i in range(5):
    loto=*{random.randint(16, 30)}, *{random.randint(31,45)}, *{random.randint(46,60)}, *{random.randint(62,75)}
    loto_2=''+str(random.randint(1,15))
    print(loto_2.zfill(2),*loto,sep=' ')


#2
workers=int(input("Скільки праціників заповнюватимуть анкету?"))
for iii in range(workers):
    dicct={}
    dicct['usd']=36.92
    dicct['ПІБ']=input("Введіть ПІБ: ")
    dicct['дата народження']=input("Введіть дату народження: ")
    dicct['адреса проживання']=input("Введіть адресу проживання: ")
    dicct['контактний номер']=input("Введіть контактний номер: ")
    dicct['посада']=input("Введіть посаду: ")
    dicct['стаж']=int(input("Введіть стаж: "))
    dicct['мінімальна зарплата']=600
    dicct['індексація за рік стажу']=int(input("Введіть індексацію за рік часу: "))
    dicct['зарплата'] = (dicct["мінімальна зарплата"] + dicct['індексація за рік стажу'] * dicct["usd"])
    print(f"ПІБ: {dicct['ПІБ']}; дата народження: {dicct['дата народження']}; адреса проживання: {dicct['адреса проживання']};"
          f" контактний номер: {dicct['контактний номер']} "
          f"посада: {dicct['посада']}; стаж: {dicct['стаж']} р.; зарплата: {dicct['зарплата']}")






















