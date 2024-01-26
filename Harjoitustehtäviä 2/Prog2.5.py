print('Anna leiviskät.')
x=20
y=32
z=13.3
a=float(input())
a=a*x*y*z
print('Anna naulat.')
b=float(input())
b=b*y*z
print('Anna luodit.')
c=float(input())
c=c*z
m=c+b+a
#koko massa grammoina
print('Massa nykymittojen mukaan:\n' , m//1000,'kilogrammaa ja ', round(m % 1000,2),' grammaa.')


