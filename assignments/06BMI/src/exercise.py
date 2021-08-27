def main():
    # Escribe el código adecuado para completar el programa
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    if(peso <=0 ) or (altura <= 0):
        print("Revisa tus datos, alguno de ellos es erróneo.")
    else:
        
        i= peso/(altura**2)
        if(i >= 0 and i <20):
            print("PESO BAJO")
        elif(i >= 20 and i < 25):
            print("NORMAL")
        elif(i >= 25 and i < 30):
            print("SOBREPESO")
        elif(i >= 30 and i < 40):
            print("OBESIDAD")
        elif(i >= 40):
            print("OBESIDAD MORBIDA")
            

if __name__ == '__main__':
    main()