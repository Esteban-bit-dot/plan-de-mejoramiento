import modelo as controlador

class modelo:

  def __init__ (self, datocolor, datoforma, datotamaño):
    pass
# abctraccion

class vivero_vital:

  def __init__ (self, datocolor, datoforma, datotamaño):
    self.color=""
    self.forma=""
    self.tamaño=""

  def asignacion_material(self, datocolor, datoforma, datotamaño):
    self.color=datocolor
    self.forma=datoforma
    self.tamaño=datotamaño
    print(f"los viveros son: {self.color}- de forma {self.forma}- de tamaño {self.tamaño}")
    
# encapsulamiento

class vivero_vital:

  def __init__(self, datocolor, datoforma, datotamaño, datoplanta):
    self.color=""
    self.forma=""
    self.tamaño=""

  def asignacion_material(self, datocolor, datoforma, datotamaño):
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
    
   def asignacion_material(self, datocolor, datoforma, datotamaño):
    self.color=datocolor
    self.forma=datoforma
    self.tamaño=datotamaño
    print(f"los viveros son: {self.color}- de forma {self.forma}- de tamaño {self.tamaño}")
    

  class vivero_hijo1:
   
   def __init__(self, datocolor, datoforma, datotamaño,datoplanta):
     super(). __init__(self)
     self.color=""
     self.forma=""
     self.tamaño=""
     self.planta=""

   def asignacion_material(self, datocolor, datoforma, datotamaño, datoplanta):
     super().asignacion_material(datocolor, datoforma, datotamaño, datoplanta)
     self.color=datocolor
     self.forma=datoforma
     self.tamaño=datotamaño
     self.planta=datoplanta
     print(f"los viveros son: {self.color}- de forma {self.forma}- de tamaño {self.tamaño} y tiene{self.planta}")
    

  class vivero_hijo2:
   
   def __init__(self, datocolor, datoforma, datotamaño, datoplanta):
     super(). __init__(self)
     self.color=""
     self.forma=""
     self.tamaño=""
     self.planta=""

   def asignacion_material2(self, datocolor, datoforma, datotamaño, datoplanta):
     super().asignacion_material(datocolor, datoforma, datotamaño, datoplanta)
     self.color=datocolor
     self.forma=datoforma
     self.tamaño=datotamaño
     self.planta=datoplanta
     print(f"los viveros son: {self.color}- de forma {self.forma}- de tamaño {self.tamaño} y tiene{self.planta}")
    
#polimorfismo

class vivero_hijo1:
   
  def __init__(self, datocolor, datoforma, datotamaño, datoplanta):
     super(). __init__(self)
     self.color=""
     self.forma=""
     self.tamaño=""
     self.planta=""

  def asignacion_material1(self, datocolor, datoforma, datotamaño, datoplanta):
    super().asignacion_material1(datocolor, datoforma, datotamaño, datoplanta)
    self.color=datocolor
    self.forma=datoforma
    self.tamaño=datotamaño
    self.planta=datoplanta
    print(f"los viveros son: {self.color}- de forma {self.forma}- de tamaño {self.tamaño} y tiene{self.planta}")
    

class vivero_hijo2:

   def __init__(self, datocolor, datoforma, datotamaño, datoplanta):
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
   

def guardar_datos(self, Auxlista):
    self.Herencia = Auxlista[0]

def buscar_datos(self, datos):
    if datos == self.datos():
       print("encontrado")
    else:
       print("no exite")

def actualizar_datos(self, datos):
  if datos == self.datos():
    if datos == vivero_vital:
      print ("ingrese los datos que va actualizar: ")
  else:
     print("error")

def eliminar_datos(self, datos):
   if datos == self.datos():
     if datos == vivero_vital:
      print ("ingrese los datos que va eliminar: ")
   else:
     print("error")

while vivero_vital == 2:
     vivero_vital = 2 
     print(vivero_vital)
     if vivero_vital == 0:
      print("error")
      break
     else:
        print("fin del bucle") 

#CRUD
class Vivero:
 
 def __init__(self, datocolor, datoforma, datotamaño, datoplanta):
      self.datocolor = datocolor
      self.datoforma = datoforma
      self.datotamaño = datotamaño
      self.datoplanta = datoplanta

 def Guardar_datos(self, datocolor, datoforma, datotamaño, datoplanta):
    self.color = datocolor
    self.forma = datoforma
    self.tamaño = datotamaño
    self.plantas = datoplanta

 def Actualizar_datos(self, datocolor, datoforma, datotamaño, datoplanta):
    self.color = datocolor
    self.forma = datoforma
    self.tamaño = datotamaño
    self.plantas = datoplanta
    self.actualizar_datos = (datocolor, datoforma, datotamaño, datoplanta)

 def Eliminar_datos(self, datocolor, datoforma, datotamaño, datoplanta):
    self.color = datocolor
    self.forma = datoforma
    self.tamaño = datotamaño
    self.plantas = datoplanta
    self.Eliminar_datos = (datocolor, datoforma, datotamaño, datoplanta)

 def Mostrar_datos(self, datocolor, datoforma, datotamaño, datoplanta):
    tuple == (datocolor, datoforma, datotamaño, datoplanta)
    self.color = datocolor
    self.forma = datoforma
    self.tamaño = datotamaño
    self.plantas = datoplanta
    self.Mostrar_datos = (datocolor, datoforma, datotamaño, datoplanta)

def set_datos(self, datos):
    datos = self.datos();

def get_datos(self, datos):
    return datos();

#******************************Codigo Pricipal***************************************#
objvivero_vital=Vivero("marron", "rentagulo", "grande", "rojo")
objvivero_hijo1=Vivero("marron claro", "retangulo", "mediano", "plantas")
objvivero_hijo2=Vivero("marron claro", "retangulo", "mediano", "plantas")
objvivero_vital.Guardar_datos("marron claro", "retangulo", "mediano", "plantas")
objvivero_vital.Actualizar_datos("marron claro", "retangulo", "mediano", "plantas")
objvivero_vital.Eliminar_datos("marron claro", "retangulo", "mediano", "plantas")
objvivero_vital.Mostrar_datos("marron claro", "retangulo", "mediano", "plantas")
