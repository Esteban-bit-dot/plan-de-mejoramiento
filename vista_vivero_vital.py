
import tkinter as ventana 

class Ventana:
 def __init____(self, datoColor, datoTitulo, datoBuscador):
    self.Color=datocolor
    self.Titulo=datoTitulo
    self.Buscador=datoBuscador
  
   def crear_vivero_vital(self):
     vivero_vital=ventana.Tk()
     self.vivero=ventana.StringVar()
     vivero_vital.title(self.Titulo)
     vivero_vital.geometry(400*500)
     vivero_vital.config(bg=self.color, height=500, width=600)
     return vivero_vital

 def crear_contenedor(self,datoContenedor):
    contenedor=ventana.Frame(datoContenedor)
    contenedor.config(bg="verde",width=500, height=400,padx=20,pady=20)
    contenedor.pack()
    return contenedor
 
 global login_Admi
 global login_contraseña

 def Ventana_login(self,datoAdmi,datocontraseña):
    label(Ventana_login, text="Admi * ").pack()
    entrada_login_Admi=Entry=Ventana_login,textvariable=verifica_Admi
    entrada_login_Admi.pack()
    label=Ventana_login, text="contraseña * ".pack()
    entrada_login_contraceña=Entry(Ventana_login,textvariable="verifica_contraceña", show='*')
    entrada_login_contraceña.pack()
    Button(Ventana_login, text="continuar", width=(10), height=(5));

global verifica_Admi
global verifica_contraseña
global END

def verifica_login(self, datoverificar):
    verifica_Admi=Admi.get()
    contraseña=verifica_contraseña.get()
    login_Admi.delete(0, END)
    login_contraseña.delete(0, END)

Admi=list()
if Admi:
  archivo = (Admi, "r")
  verificar = archivo()
  if verificar():
    print("exito_login")
elif:
   print("error_contraseña")
else:
    print("error_Admi")

for i in range():
        login=login+i
        print(login)

    global ventana_error_Admi
    global Ventana_login
    global borrar_error_Admi

def error_Admi(self):
    ventana_error_Admi=toplevel=Ventana_login()
    ventana_error_Admi.title("ERROR")
    ventana_error_Admi.geometry("500*600")
    Label=ventana_error_Admi, text= "Admi incorrecto".pack()
    Button(ventana_error_Admi, text="Ok", command=borrar_error_Admi())


def Registro_inventario(self,inventario):
    Label(inventario_los_Andes, text="inventario los Andes".pack());
     
    Label(Nombre_del_inventario, text="Nombre del inventario").pack()
    Nombre_del_inventario.Entry(Registro_inventario,textvariable = Nombre_del_inventario);
    Nombre_del_inventario.pack()

    Label(Superficie, text="Superficie ").pack()
    Superficie=Entry(Registro_inventario,textvariable = Superficie);
    Superficie.pack()

    Label(Tipo_de_cultura, text="Tipo de cultura ").pack()
    Tipo_de_cultura=Entry(Registro_inventario,textvariable = Tipo_de_cultura);
    Tipo_de_cultura.pack()

    Label(Fecha_de_creacion, text="Fecha de creacion ").pack()
    Fecha_de_creacion=Entry(Registro_inventario,textvariable = Fecha_de_creacion);
    Fecha_de_creacion.pack()

    Label(Responsable, text="Responsable ".pack())
    Responsable=Entry(Registro_inventario,textvariable = Responsable);
    Responsable.pack()

    Label(Capacidad_de_produccion, text="Capacidad de producion").pack()
    Capacidad_de_produccion=Entry(Registro_inventario,textvariable = Capacidad_de_produccion);
    Capacidad_de_produccion.pack()

    Label(Sistema_de_Riego, text="Sistema de Riego").pack()
    Sistema_de_Riego=Entry(Registro_inventario,textvariable = Sistema_de_Riego);
    Sistema_de_Riego.pack()

    Label(inventario_las_Flores, text="inventario las Flores".pack())

    Label(Nombre_del_inventario, text="Nombre del inventario ").pack
    Nombre_del_inventario=Entry(Registro_inventario, textvariable = Nombre_del_inventario);
    Nombre_del_inventario.pack()   
    
    Label(Superficie, text="Superficie ").pack()
    Superficie=Entry(Registro_inventario, textvariable = Superficie);
    Superficie.pack()

    Label(Tipo_de_cultura, text="Tipo de cultura ").pack()
    Tipo_de_cultura.Entry(Registro_inventario, textvariable = Tipo_de_cultura);
    Tipo_de_cultura.pack()

    Label( Fecha_de_creacion, text="Fecha de creacion ").pack
    Fecha_de_creacion.Entry(Registro_inventario, textvariable = Fecha_de_creacion);
    Fecha_de_creacion.pack()

    Label( Responsable, text="Responsable ").pack()
    Responsable.Entry(Responsable, textvariable = Responsable);
    Responsable.pack()

    Label(Capacidad_de_produccion, text="Capacidad de producion").pack()
    Capacidad_de_produccion=Entry(Registro_inventario, textvariable = Capacidad_de_produccion);
    Capacidad_de_produccion.pack()

    Label(Sistema_de_Riego, text="Sistema de Riego").pack()
    Sistema_de_Riego.Entry(Registro_inventario, textvariable = Sistema_de_Riego);
    Sistema_de_Riego.pack()

def crearMenu(self, datocontenedor):
   Menu=ventana.Menu(datocontenedor)
   inventarioMenu=ventana.menu(Menu, tearoff=0)
   inventarioMenu.add_command.Button(text="Registro de inventario")
   inventarioMenu.add_command.button(text="Control de inventario" )
   inventarioMenu.add_command.Button(text="Control de humendad" )
   inventarioMenu.add_command.Button(text="Control de piso" )
   inventarioMenu.add_command.Button(text="Enfermedad" )
   Menu.add_cascade(label="inventarios",Menu)
   datocontenedor.config(menu)
   
   
   global StringVar
 
def control_de_inventario(self):
    Label(Frame, text = 'Buscar: ').grid(row = 4, column = 1)
    self.Buscador = Entry( Frame,textvariable = StringVar())
    self.Buscador.grid(row = 4, column = 1)

    
    Label(control_de_inventario, text="inventario los Andes").pack()
    Label(control_de_inventario, text="inventario las Flores ").pack()
    Label(control_de_inventario, text="inventario los pinos").pack()
    Label(control_de_inventario, text="inventario El mirador").pack()
    Label(control_de_inventario, text="inventario las brisas").pack()

    control_de_inventario.add_cascade(label="imventarios", inventario=control_de_inventario)
    Button(frame, text = "operativo", command = self.registro).grid(row = 4, column = 1))
    Button(frame, text = "editar", command = self.registro).grid(row = 4, column = 1)
    Button(frame, text = "eliminar", command = self.registro).grid(row = 4, column = 1)
    Button(frame, text = "detalles", command = self.registro).grid(row = 4, column = 1)

    Button(frame, text = "reparacion", command = self.registro).grid(row = 4, column = 1)
    Button(frame, text = "editar", command = self.registro).grid(row = 4, column = 1)
    Button(frame, text = "eliminar", command = self.registro).grid(row = 4, column = 1)
    Button(frame, text = "detalles", command = self.registro).grid(row = 4, column = 1)

    Button(frame, text = "inspeccion", command = self.registro).grid(row = 4, column = 1)
    Button(frame, text = "editar", command = self.registro).grid(row = 4, column = 1)
    Button(frame, text = "eliminar", command = self.registro).grid(row = 4, column = 1)
    Button(frame, text = "detalles", command = self.registro).grid(row = 4, column = 1)

    Button(frame, text = "expancion", command = self.registro).grid(row = 4, column = 1)
    Button(frame, text = "editar", command = self.registro).grid(row = 4, column = 1)
    Button(frame, text = "eliminar", command = self.registro).grid(row = 4, column = 1)
    Button(frame, text = "detalles", command = self.registro).grid(row = 4, column = 1)

    Button(frame, text = "operativo", command = self.registro).grid(row = 4, column = 1)
    Button(frame, text = "editar", command = self.registro).grid(row = 4, column = 1)
    Button(frame, text = "eliminar", command = self.registro).grid(row = 4, column = 1)
    Button(frame, text = "detalles", command = self.registro).grid(row = 4, column = 1)
   
    Button(frame, text = "regresar", command = self.regitro).grid(row = 4, column = 1)

def control_de_humedad(self, dstohumedad):
    Button(frame, text = "editar", command = self.registro).grid(row = 4, column = 1))
    Button(frame, text = "eliminar", command = self.registro).grid(row = 4, column = 1)
    Button(frame, text = "detalles", command = self.registro).grid(row = 4, column = 1)

def control_de_piso(self, datopiso):
    Button(frame, text = "editar", command = self.registro).grid(row = 4, column = 1))
    Button(frame, text = "eliminar", command = self.registro).grid(row = 4, column = 1)
    Button(frame, text = "detalles", command = self.registro).grid(row = 4, column = 1)

def Enfermedad(self, datoenfermedad):
    Button(frame, text = "editar", command = self.registro).grid(row = 4, column = 1))
    Button(frame, text = "eliminar", command = self.registro).grid(row = 4, column = 1)
    Button(frame, text = "detalles", command = self.registro).grid(row = 4, column = 1)

#*****************codigo principal*********************#
datocolor = input("digite el color de la ventana: ")
datoTitulo = input("digite el nombre de la ventana: ")
objvivero_vital=ventana(datocolor, datoTitulo)
auxvivero_vital=objvivero_vital.crear_vivero_vital()
objvivero_vital.crearMenu(auxvivero_vital)
objVista=ventana()
objvivero_vital.crearMenu(auxvivero_vital)
auxvivero_vital.mainloop()
