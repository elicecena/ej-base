
import os
def main():
    #escribe tu código abajo de esta línea
    os.system("clear")
    a=float(input("dame el vaor de a:"))
    b=float(input("dame el vaor de b:"))
    c=float(input("dame el vaor de c:"))

    d=float(input("dame el vaor de d:"))
    e=float(input("dame el vaor de e:"))
    f=float(input("dame el vaor de f:"))

    determinante=a*e-b*d

    if determinante == 0:
        print("El sistema no tiene solución...")
    else:
        x=(c*e-b*f)/determinante
        y=(a*f-c*d)/determinante

        print("La solución al sistema de ecuaciones es:")
        print (f"x={x}")
        print (f"y={y}")


if __name__=='__main__':
    main()
