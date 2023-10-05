#! /usr/bin/python

import datetime
from persona import Persona

class Listado:
    def __init__(self):
        self.listado = []

    def nueva_persona(self, dni, nombre, apellido, fn_dia, fn_mes, fn_anio):
        p = Persona(dni, nombre, apellido, fn_dia, fn_mes, fn_anio)
        self.listado.append(p)

    def eliminar_persona(self,dni):
        p = self.buscar_por_dni(dni)
        if p:
            self.listado.remove(p)

    def modificar_datos(self, dni, nombre, apellido, fn_dia, fn_mes, fn_anio):
        p = self.buscar_por_dni(dni)
        if p:
            if len(nombre) > 0:
                p.nombre = nombre
            if len(apellido) > 0:
                p.apellido = apellido
            if fn_dia > 0 and fn_mes > 0 and fn_anio > 0:
                p.fecha_nacimiento = datetime.datetime(fn_anio, fn_mes, fn_dia)
                p.edad = p.calcular_edad()


    def buscar_por_dni(self, dni):
        for persona in self.listado:
            if persona.dni == dni:
                return persona
        return None

    def __str__(self):
        personas = ""
        for persona in self.listado:
            personas = personas + str(persona) + "\n"
        return personas

