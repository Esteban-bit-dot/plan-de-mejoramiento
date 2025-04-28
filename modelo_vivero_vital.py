class modelo_vivero_vital:
     
# abctraccion

 class vivero_vital:

  def __init__ (self,datocolor,datoforma,datotamaño,datoplanta):
    self.color=""
    self.forma=""
    self.tamaño=""

  def asignacion_material(self, datocolor,datoforma,datotamaño):
    self.color=datocolor
    self.forma=datoforma
    self.tamaño=datotamaño
    print(f"los viveros son: {self.color}- de forma {self.forma}- de tamaño {self.tamaño}")
    
# encapsulamiento

class vivero:
  def __init__(self,datocolor,datoforma,datotamaño,datoplanta):
    self.color=""
    self.forma=""
    self.tamaño=""

  def asignacion_material(self, datocolor,datoforma,datotamaño):
    self.color=datocolor
    self.forma=datoforma
    self.tamaño=datotamaño
    print(f"los viveros son: {self.color}- de forma {self.forma}- de tamaño {self.tamaño}")
   
# Herencia

  class vivero_vital:
   def __init__(self,datocolor,datoforma,datotamaño,datoplanta):
    self.color=""
    self.forma=""
    self.tamaño=""
    
   def asignacion_material(self, datocolor,datoforma,datotamaño):
    self.color=datocolor
    self.forma=datoforma
    self.tamaño=datotamaño
    print(f"los viveros son: {self.color}- de forma {self.forma}- de tamaño {self.tamaño}")
    

  class vivero_hijo1:
   def __init__(self,datocolor,datoforma,datotamaño,datoplanta):
    super(). __init__()
    self.color=""
    self.forma=""
    self.tamaño=""
    self.planta=""

  def asignacion_material(self,datocolor,datoforma,datotamaño,datoplanta):
    super().asignacion_material(datocolor,datoforma,datotamaño,datoplanta)
    self.color=datocolor
    self.forma=datoforma
    self.tamaño=datotamaño
    self.planta=datoplanta
    print(f"los viveros son: {self.color}- de forma {self.forma}- de tamaño {self.tamaño} y tiene{self.planta}")
    

  class vivero_hijo2:
   def __init__(self,datocolor,datoforma,datotamaño,datoplanta):
    super(). __init__()
    self.color=""
    self.forma=""
    self.tamaño=""
    self.planta=""

  def asignacion_material2(self,datocolor,datoforma,datotamaño,datoplanta):
    super().asignacion_material(datocolor,datoforma,datotamaño,datoplanta)
    self.color=datocolor
    self.forma=datoforma
    self.tamaño=datotamaño
    self.planta=datoplanta
    print(f"los viveros son: {self.color}- de forma {self.forma}- de tamaño {self.tamaño} y tiene{self.planta}")
    
#polimorfismo

  class vivero_hijo1:
   def __init__(self,datocolor,datoforma,datotamaño,datoplanta):
     super(). __init__(self)
     self.color=""
     self.forma=""
     self.tamaño=""
     self.planta=""

  def asignacion_material1(self,datocolor,datoforma,datotamaño,datoplanta):
    super().asignacion_material1(datocolor,datoforma,datotamaño,datoplanta)
    self.color=datocolor
    self.forma=datoforma
    self.tamaño=datotamaño
    self.planta=datoplanta
    print(f"los viveros son: {self.color}- de forma {self.forma}- de tamaño {self.tamaño} y tiene{self.planta}")
    

  class vivero_hijo2:

   def __init__(self,datocolor,datoforma,datotamaño,datoplanta):
    super().__init__(self)
    self.color=""
    self.forma=""
    self.tamaño=""
    self.planta=""

  def asignacion_material2(self, datocolor, datoforma, datotamaño, datoplanta):
    super().asignacion_material2(datocolor, datoforma, datotamaño, datoplanta)
    self.color=datocolor
    self.forma=datoforma
    self.tamaño=datotamaño
    self.planta=datoplanta
    print(f"los viveros son: {self.color}- de forma {self.forma}- de tamaño {self.tamaño} y tiene{self.planta}")
   

  def guardar_datos(self,Auxlista):
    self.Herencia=Auxlista[0]

def buscar_datos(self,dato):
    if dato == self.datos():
       print("encontrado")
    else:
       print("no exite")

def actualizar(self, dato):
  if dato == self.datos():
    if dato == vivero_vital:
      print ("ingrese los datos que va actualizar: ")
  else:
     print("error")

  vivero_vital = vivero
while vivero =="2":
     vivero_vital = 2 
     print(vivero)
     if vivero_vital == 0:
      print("error")
      break
     else:
        print("fin del bucle") 

def Guardar_datos(self, datocolor, datoforma, datotamaño, datoplanta):
    self.color=datocolor
    self.forma=datoforma
    self.tamaño=datotamaño
    self.plantas= datoplanta

def Actualizar_datos(self, datocolor, datoforma, datotamaño, datoplanta):
    self.color=datocolor
    self.forma=datoforma
    self.tamaño=datotamaño
    self.plantas= datoplanta
    self.actualizar_datos = (datocolor, datoforma, datotamaño, datoplanta)

def Eliminar_datos(self,datocolor,datoforma,datotamaño, datoplanta):
    self.color=datocolor
    self.forma=datoforma
    self.tamaño=datotamaño
    self.plantas= datoplanta
    self.Eliminar_datos = (datocolor,datoforma,datotamaño, datoplanta)

def Mostrar_datos(self,datocolor,datoforma,datotamaño, datoplanta):
    tuple == (datocolor,datoforma,datotamaño, datoplanta)
    self.color=datocolor
    self.forma=datoforma
    self.tamaño=datotamaño
    self.plantas= datoplanta
    self.Mostrar_datos = (datocolor,datoforma,datotamaño, datoplanta)

def setdatos(self, datos):
    dato = self.dato()

def getdatos(datos):
     return datos();

#******************************Codigo Pricipal***************************************#

objvivero_vital=vivero()
objvivero_vital.asignacion_material("marron claro", " rectangulo", " mediano")
objvivero_hijo1=vivero()
objvivero_hijo1.asignacion_material("marron claro","retangulo","mediano","plantas")
objvivero_hijo2=vivero()
objvivero_hijo2.asignacion_material2("marron claro","retangulo","mediano","plantas")
objvivero_vital.Guardar_datos()
Guardar_datos.vivero_vital=Actualizar_datos()
Eliminar_datos.objvivero_vital()
Mostrar_datos()
