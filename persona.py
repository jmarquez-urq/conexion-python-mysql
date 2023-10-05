#! /usr/bin/python

import datetime

class Persona:

    ''' Método iniciador '''
    def __init__(self, dni, nombre, apellido, fn_dia, fn_mes, fn_anio):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = datetime.datetime(fn_anio, fn_mes, fn_dia)
        self.edad = self.calcular_edad()

    '''
    Retorna la edad de una persona a partir de su fecha de nacimiento.
    '''
    def calcular_edad(self):
        este_anio = datetime.datetime.now().year
        if self.ya_cumplio_anios():
            return este_anio - self.fecha_nacimiento.year
        else:
            return este_anio - self.fecha_nacimiento.year - 1

    '''
    Indica si la persona ya cumplió años en el año actual.
    Retorna un booleano.
    '''
    def ya_cumplio_anios(self):
        hoy = datetime.datetime.now()
        if hoy.month > self.fecha_nacimiento.month:
            return True
        elif hoy.month == self.fecha_nacimiento.month \
            and hoy.day >= self.fecha_nacimiento.day:
            return True
        else:
            return False

    '''
    Retorna nombre y apellido de la persona
    '''
    def __str__(self):
        return ( str(self.dni) + ": " + self.nombre + " " + self.apellido
                 + " (" + str(self.edad) + " años)" )
