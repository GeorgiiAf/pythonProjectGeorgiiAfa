def list1(lista):
    list2=[]
    for i in lista:
        if i % 2 == 0:
            list2.append(i)
    return list2
numerot=[1,2,3,4,5,6,7,8,9,10]
print(f'Esimerkiksi lista :  {numerot} ')
l = list1(numerot)
print(f'Uusi lista on: {l}')


