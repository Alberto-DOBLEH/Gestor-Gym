import mysql.connector
import pymysql

def conexion():
    return pymysql.connect(host="localhost", user="root", passwd="root", database="gestor_gimnasio")