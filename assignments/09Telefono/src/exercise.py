def main():
    #escribe tu código abajo de esta línea
    print("Dame el numero de mensajes")
    nm=float(input())
    print("Dame el numero de megas")
    nmg=float(input())
    print("Dame el numero de minuto")
    nmn=float(input())
    price=float(0.80)*(nm+nmg+nmn)
    print("El costo mensual es:" +str(price))
    
    #Leer los datos
    pass


if __name__ == '__main__':
    main()
