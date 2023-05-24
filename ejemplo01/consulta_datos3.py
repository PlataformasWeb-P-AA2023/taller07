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
# la entidad Club 
clubs = session.query(Club).all() 

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de Clubs y sus jugadores")
for s in clubs:
    print("%s" % (s))
    # desde cada objeto de la lista
    # de tipo Club
    # se puede acceder 
    # a los jugadores
    jugadores = s.jugadores # es una secuencia; es una lista
    # [objJugador1, objJugador2, objJugador3, ..., objJugadorN]
    for i in jugadores:
        print(i.dorsal)
        
    print("---------")


