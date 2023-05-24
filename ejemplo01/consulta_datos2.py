from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 
# la entidad estudiantes (clase Estudiante) 
jugadores = session.query(Jugador).all() 

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de Jugadores")
for s in jugadores:
    print("%s" % (s))
    # desde cada objeto de la lista
    # jugador
    # se puede acceder al club; como lo definimos
    # al momento de crear la clase Jugador
    print("El Jugador pertenece a: %s " % (s.club))
    print("---------")

print("Presentación de Jugadores - op2")
for s in jugadores:
    print("%s" % (s))
    # desde cada objeto de la lista
    # jugador
    # se puede acceder al club; como lo definimos
    # al momento de crear la clase Jugador
    print("El Jugador pertenece a: %s " % (s.club.nombre))
    print("---------")



