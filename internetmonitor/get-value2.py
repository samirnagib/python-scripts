#!/usr/bin/env python3
# USO:  get-value.py <AMBIENTE> <DADO>

import platform
import os
import time
from mysql.connector import connect
from datetime import datetime
import sys

# conexao com o banco
def mysql_connection(host, user, passwd, database=None):
    connection = connect(
        host = host,
        user = user,
        passwd = passwd,
        database = database,
        auth_plugin='mysql_native_password')
    return connection


#DEFINIR AMBIENTE DE TRABALHO
# PRD - PRODUCAO
# DEV - DESENVOLVIMENTO
#DEFINIR TIPO DE DADOS RETORNADO
# SRV - DADOS DO SERVIDOR
# CLI - DADOS DO CLIENTE
# DUL - DOWNLOAD E UPLODAD E LATENCIA
# EXC - EXECUCAO DO SCRITP
# ALL - TODOS OS DADOS


if  len(sys.argv) > 2 :  #  parametros
    if  sys.argv[1].upper() =="PRD":
        #print("AMBIENTE DE PRODUCAI")
        #base producao
        connection = mysql_connection('192.168.175.49', 'script', 'Lun@17N0V3', 'NETMON')
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

    elif sys.argv[1].upper() =="DEV":
        #print("AMBIENTE DE DESENVOLVIMENTO")
        #base de teste
        connection = mysql_connection('192.168.175.49', 'script', 'Lun@17N0V3', 'NETMONTE')
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
    else:
        #print("Parametro de banco nao selecionado, assumindo banco de testes.")
        #base de teste
        connection = mysql_connection('192.168.175.49', 'script', 'Lun@17N0V3', 'NETMONTE')
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
    # fim da selecao de banco
    #RECUPERAR A INFORMACAO    
    if sys.argv[2].upper() =="SRV":
        print(idServer,",",sServer,",",City,",",Pais,",",CC,",",Latitude_S,",",Longitude_S)
    elif sys.argv[2].upper() =="CLI":
        print(IP_Address,",",ISP,",",ISP_Rate,",",CCCLiente,",",Latitude_C,",",Longitude_C)
    elif sys.argv[2].upper() =="DUL":
        print(Download,",",Upload,",",Latencia_S)
    elif sys.argv[2].upper() =="EXC":
        print(HoraColeta)
    elif sys.argv[2].upper() =="ALL":
         print(idServer,",",sServer,",",City,",",Pais,",",CC,",",Latitude_S,",",Longitude_S,Download,",",Upload,",",Latencia_S,IP_Address,",",ISP,",",ISP_Rate,",",CCCLiente,",",Latitude_C,",",Longitude_C,",",HoraColeta)
    else:
        print(HoraColeta)

else:
    #print("Parametro de banco nao selecionado, assumindo banco de testes.")
    #base de teste
    connection = mysql_connection('192.168.175.49', 'script', 'Lun@17N0V3', 'NETMONTE')
    query = """Select * from HistoryNetDB order by idSEQ  DESC LIMIT 1"""
    cursor = connection.cursor()
    cursor.execute(query)
    row = cursor.fetchall()
    for valor in row:
        HoraColeta = valor[18]
    print(HoraColeta)

connection.close()
