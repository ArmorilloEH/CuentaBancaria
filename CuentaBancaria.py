import os
#clase Persona
#atributos:nombre,apellidos
#clase cliente que hereda de persona
#-------------------------------
#atributos:numero_cuenta,balance
#metodos:imprimir_cliente(),depositar(),retirar()
#-----------------------------------------------
#codigo para elegir retirar,depositar o salir
#No se puede retirar más dinero del que se posee
#------------------------------------------------
#funcion para crear al cliente que devuelve un cliente
#bucle que mantiene al usuario en un loop si quiere seguir o salir
#del programa
Fin_programa=False
class Persona:
    def __init__(self,nombre,apellidos):
        self.nombre=nombre
        self.apellidos=apellidos
class Cliente(Persona):
    def __init__(self,nombre,apellidos,numero_cuenta,balance):
        super().__init__(nombre,apellidos)
        self.numero_cuenta=numero_cuenta
        self.balance=balance
    def __str__(self):
        return f"--DATOS CLIENT@--\nNombre:\n{self.nombre}\nApellidos:\n{self.apellidos}\nNúmero de cuenta:\n{self.numero_cuenta}\nBalance:\n{self.balance}"
    def depositar(self):
        print(f"--Dispones de {self.balance}€ en tu cuenta--")
        cantidad_depositar=float(input("¿Cuanto dinero deseas ingresar a tu cuenta?\n"))
        cantidad_total=cantidad_depositar+float(self.balance)
        self.balance=cantidad_total
        cantidad_final=self.balance
        print(f"Operación realizada con exito, ahora dispones de {self.balance}€ en tu cuenta.")
        return cantidad_final
    def retirar(self):
        print(f"--Dispones de {self.balance}€ en tu cuenta--")
        cantidad_retirar = float(input("¿Cuanto dinero deseas retirar de tu cuenta?\n"))
        while cantidad_retirar>self.balance:
            cantidad_retirar = float(input("No puedes retirar más dinero del que posees,introduce una cantidad menor:\n"))
            pass
        cantidad_total = float(self.balance)-cantidad_retirar
        self.balance=cantidad_total
        cantidad_final=self.balance
        print(f"Operación realizada con exito, ahora dispones de {self.balance}€ en tu cuenta.")
        return cantidad_final
def crear_cliente():
    print("Registraste en el banco Santander--")
    nombre = input("Nombre:\n")
    apellidos = input("Apellidos:\n")
    numero_cuenta = input("Número de cuenta:\nES ")
    while len(numero_cuenta)!=24:
      numero_cuenta=input("Introduce un número de cuenta valido:\n")
    pass
    balance = float(input("Balance:\n"))
    cliente = Cliente(nombre, apellidos, numero_cuenta, balance)
    return cliente
def menu():
    print("[1]-Ingresar dinero.\n[2]-Retirar dinero.\n[3]-Limpiar consola.\n[4]-Finalizar programa.")
def elegir_opcion():
    opciones=[1,2,3,4]
    op=int(input("Elige una opción:\n"))
    if op not in opciones:
        op=int(input("Introduce una opción valida:\nES "))
    return op
cliente=crear_cliente()
while not Fin_programa:

    menu()
    op = elegir_opcion()
    if op==1:
        cliente.depositar()
    elif op==2:
        cliente.retirar()
    elif op==3:
        os.system("cls")
    else:
        os.system("cls")
        print("Programa finalizado con exito.")
        Fin_programa=True




