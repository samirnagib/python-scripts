#!/usr/bin/env python3
import json
import platform
import os
import time
import speedtest
import sqlite3
from mysql.connector import connect
from datetime import datetime

# conexao com o banco
def mysql_connection(host, user, passwd, database=None):
    connection = connect(
        host = host,
        user = user,
        passwd = passwd,
        database = database
    )
    return connection

#base de teste
connection = mysql_connection('192.168.175.49', 'script', 'Lun@17N0V3', 'NETMONTE')
#base producao
#connection = mysql_connection('192.168.175.49', 'script', 'Lun@17N0V3', 'NETMON')

query = """Select * from HistoryNetDB order by idSEQ  DESC LIMIT 1"""
cursor = connection.cursor()
cursor.execute(query)
row = cursor.fetchall()

for valor in row:
    idSEQ = valor[0]
    idServer = valor[1]
    sServer = valor[2]
    City = valor[3]
    Pais = valor[4]
    CC= valor[5]
    Latitude_S = valor[6]
    Longitude_S = valor[7]
    Latencia_S = valor[8]
    Download = valor[9]
    Upload = valor[10]
    IP_Address = valor[11]
    ISP = valor[12]
    ISP_Rate = valor[13]
    CCCLiente = valor[14]
    Latitude_C = valor[15]
    Longitude_C = valor[16]
    Timestamp_C = valor[17]
    HoraColeta = valor[18]

connection.close()


print(HoraColeta)


