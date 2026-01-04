import math
def posicion_mas(t,a,w, phi=0):
    """
    POSICION EN FUNCION DEL TIEMPO DEL MOVIMIENTO ARMONICO SIMPLE
    parametros:
    A = Amplitud (m)
    w = Velocidad angular(rad/s)
    t = tiempo (s)
    phi = Fase inicial (rad)
    """
    return  a*math.sin(w* t + phi)
def velocidad_mas(t,a,w, phi=0):
    """
        VELOCIDAD EN FUNCION DEL TIEMPO DEL MOVIMIENTO ARMONICO SIMPLE
        parametros:
        A = Amplitud (m)
        w = Velocidad angular(rad/s)
        t = tiempo (s)
        phi = Fase inicial (rad)
        """
    return -w*a*math.cos(w* t + phi)
