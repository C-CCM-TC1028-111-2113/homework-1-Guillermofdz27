def main():
    #escribe tu código abajo de esta línea
    print("Dame Los minutos:")
    minutos= float(input())
    segundos= (60)*(minutos)
    milimetros_avanzados= (5.7)*float(segundos)
    centimetros_avanzados= float(milimetros_avanzados)/(10)
    print("Centimetros Recorridos: "+str(centimetros_avanzados))
    pass

if __name__ == '__main__':
    main()
