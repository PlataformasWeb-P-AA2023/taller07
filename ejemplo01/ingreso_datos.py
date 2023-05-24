from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

# se crea un objetos de tipo Club 
club1 = Club(nombre="Barcelona", deporte="Fútbol", \
        fundacion=1920)

club2 = Club(nombre="Emelec", deporte="Fútbol", \
        fundacion=1930)

club3 = Club(nombre="Liga de Quito", deporte="Fútbol", \
        fundacion=1940)

# Se crean objeto de tipo Jugador
#
jugador1 = Jugador(nombre ="Damian Diaz", dorsal=10, posicion="mediocampo", \
        club=club1)
jugador2 = Jugador(nombre ="Matias Oyola", dorsal=18, posicion="mediocampo", \
        club=club1)
jugador3 = Jugador(nombre ="Dario Aymar", dorsal=2, posicion="defensa", \
        club=club1)


jugador4 = Jugador(nombre ="Oscar Bagui", dorsal=6, posicion="defensa", \
        club=club2)
jugador5 = Jugador(nombre ="Romario Caicedo", dorsal=11, posicion="mediocampo", \
        club=club2)


jugador6 = Jugador(nombre ="Adrián Gabbarini", dorsal=1, posicion="arquero", \
        club=club3)
jugador7 = Jugador(nombre ="Cristian Martinez", dorsal=9, posicion="delantero", \
        club=club3)

# se agrega los objetos
# a la sesión
session.add(club1)
session.add(club2)
session.add(club3)
session.add(jugador1)
session.add(jugador2)
session.add(jugador3)
session.add(jugador4)
session.add(jugador5)
session.add(jugador6)

# se confirma las transacciones
session.commit()
