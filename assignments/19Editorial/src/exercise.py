def main():
    #escribe tu código abajo de esta línea
    print("Dame el numero de paginas")
    n=float(input())
    c= float((n//475)*60)
    x= float(n%475)
    if x>=1:
        w=float(c)+60
        d=float(w)*(.9)
        print("El costo de la publicación es :" + str(d))
    else:
        e=float(c)*(.9)
        print("El costo de la publicación" +str(c))
            
    pass


if __name__ == '__main__':
    main()
