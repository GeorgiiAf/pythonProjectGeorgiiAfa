
"""def ero(a,b):
    c=a-b
    return(c)
a=float(input('kirjoita luku '))
b=float(input('kirjoita luku '))

c=ero(a,b)
print(f"erotus on {c}") """

def listtt(list):
    return list[1]
list=[0,'Kissa',2,3,4,5,6]
print(listtt(list))


#def dictionary1(sanak):
    #return sanak['nimi']
#sanak1={'nimi':'John','age':30}
#print(dictionary1(sanak1))
#sanak2={'nimi':'Stan','age':30}
#print(dictionary1(sanak2))

#def parittomat(list):
    #list1=[]
    #for i in range(len(list)):
       # if i%2==0:
        #    list1.append(i)
   # return (list1)
#luvut=[1,2,3,4,5,6,7,8,9,10]
#patittomat12 = parittomat((luvut))
#print(patittomat12)

#def double(list):
    #list2=[]
    #for i in list:
      #  list2.append(i*2)
    #return(list2)
#numbers=[12,5,21,4,8,0,11]
#doubled=double(numbers)
#print(' Vanha lista ',  numbers )
#print('Uusi lista ', doubled)

def operate(list,borders):
    list1=[]
    for item in list:
        if borders[0]< item <borders[1]:
            list1.append(item)
            summa=sum(list1)
    return summa

list=[15,1,8,18,33,1,2,3,5,6,7,8]
borders=(0,9)
result=operate(list,borders)
print(result)








#lista1= [1,5,'Juha',3.14,[2,5],(1,2,8),{'eka':4,'Toka':False}]print(lista1[5][2])
#print(lista1[6]['eka'])
#print(lista1[3::-1])
#print('Juha' in lista1)
#lista1.append(100)
#print(lista1)

#for i in range(21):
    #if i%2==0:
      #  print(i)

# for i in range(50,29,-1): print(i)
#print(8*"   moi")
#for i in range(8): print('moi')







import math
print(f'{math.pi:.3f}')

"""
name = input("Enter your name: ")
if name == "James" or name == "james":
    print("Hello " + name + "!")
else:
    while name != "James" or name != "james":
        name = input("Enter yorur name: ")
        break
    print("Hello " + name + "!")
    """