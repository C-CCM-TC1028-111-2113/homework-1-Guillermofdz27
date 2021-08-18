def main():
    #escribe tu código abajo de esta línea
    print("Dame el saldo del mes anterior")
    s=float(input())
    print("Dame los ingresos")
    i= float(input())
    print("Dame los egresos")
    e= float(input())
    print("Dame el numero de cheques")
    c= float(input())
    x= (s)+(i)-(e)-(13*c)
    x1= x-(.075*x)
    print("El saldo final de la cuenta es: "+str(x1)
          
    pass

if __name__ == '__main__':
    main()
