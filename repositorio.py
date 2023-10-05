#! /usr/bin/env python3
import mysql.connector
from persona import Persona

class Repositorio:
    '''Consulta y escribe personas en la BD'''

    def __init__(self):
        pass

    def get_all(self):
        '''
        Retorna una lista de objetos Persona, con todas las que haya en
        la Base de Datos
        '''
        lista_personas = []
        
        return lista_personas

    def get_one(self, dni):
        '''
        Retorna un objeto persona, con el dni correspondiente, o None si no
        la encuentra
        '''
        persona = None
        
        return persona


    def guardar(self, persona):
        '''Guarda la persona en la BD'''
        pass

    def actualizar(self, persona):
        '''Actualiza la persona en la BD'''
        pass

    def eliminar(self, persona):
        '''Elimina la persona de la BD'''
        pass

