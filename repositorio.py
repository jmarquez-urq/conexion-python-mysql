#! /usr/bin/env python3
import mysql.connector
from persona import Persona

class Repositorio:
    '''Consulta y escribe personas en la BD'''

    def __init__(self):
        credenciales = {
                'user': 'desarrollador_python',
                'password': '1234',
                'host': 'localhost',
                'database': 'conexion_python',
        }
        self.bd = mysql.connector.connect(**credenciales)
        self.cursor = None
        if self.bd and self.bd.is_connected:
            self.cursor = self.bd.cursor()

    def get_all(self):
        '''
        Retorna una lista de objetos Persona, con todas las que haya en
        la Base de Datos
        '''
        lista_personas = []
        
        consulta = "SELECT dni, nombre, apellido, fecha_nacimiento FROM personas"
        self.cursor.execute(consulta)
        todas_las_personas = self.cursor.fetchall()
        for dni, nombre, apellido, fecha_nacimiento in todas_las_personas:
            dia = fecha_nacimiento.day
            mes = fecha_nacimiento.month
            anio = fecha_nacimiento.year
            p = Persona(dni, nombre, apellido,dia, mes, anio)
            lista_personas.append(p)

        return lista_personas

    def get_one(self, dni):
        '''
        Retorna un objeto persona, con el dni correspondiente, o None si no
        la encuentra
        '''
        persona = None
        consulta = "SELECT dni, nombre, apellido, fecha_nacimiento "
        consulta+= "FROM personas WHERE dni = %s"
        self.cursor.execute(consulta, [ dni ])
        (dni, nombre, apellido, fn) = self.cursor.fetchone()
        dia = fn.day
        mes = fn.month
        anio = fn.year
        persona = Persona(dni, nombre, apellido, dia, mes, anio)
        
        return persona


    def guardar(self, persona):
        '''Guarda la persona en la BD'''
        query = "INSERT INTO personas (dni, nombre, apellido, fecha_nacimiento) "
        query+= "VALUES (%s, %s, %s, %s)"

        self.cursor.execute(query, [
            persona.dni,
            persona.nombre,
            persona.apellido,
            persona.fecha_nacimiento
        ])
        self.bd.commit()



    def actualizar(self, persona):
        '''Actualiza la persona en la BD'''
        query = "UPDATE personas "
        query+= "SET nombre = %s, apellido = %s, fecha_nacimiento = %s "
        query+= "WHERE dni = %s"

        self.cursor.execute(query, [
            persona.nombre,
            persona.apellido,
            persona.fecha_nacimiento,
            persona.dni
        ])
        self.bd.commit()

    def eliminar(self, persona):
        '''Elimina la persona de la BD'''
        query = "DELETE FROM personas WHERE dni = %s"
        self.cursor.execute(query, [persona.dni])
        self.bd.commit()



