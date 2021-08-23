def main():
    #escribe tu código abajo de esta línea
    w=0
print("Dame un numero")
numero=str(input())
a= int(numero[0])%2
b= int(numero[1])%2
c= int(numero[2])%2
d= int(numero[3])%2
if a==0:
    w1= int(w)+1
else:
    w1= w
if b==0:
    w2= int(w)+1
else:
    w2= w
if c==0:
    w3= int(w)+1
else:
    w3= w
if d==0:
    w4= int(w)+1
else:
    w4= w
print("El numero de digitos pares es:"+str(int(w4)+int(w1)+int(w2)+int(w3)))



    

    pass


if __name__ == '__main__':
    main()
