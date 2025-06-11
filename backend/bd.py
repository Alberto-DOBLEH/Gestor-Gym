import mysql.connector
import pymysql

def conexion():
    return pymysql.connect(host="localhost",
                                   user="root",
                                   password="root",
                                   database="gestor_gimnasio")