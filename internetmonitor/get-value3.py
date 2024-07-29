#!/usr/bin/env python3
# USO:  get-value.py <AMBIENTE> <ITEM A RETORNAR>

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

# criaçao do caminho do log
def gera_log(arquivo,dado):
    data = dado
    file = arquivo
    #folder = os.getcwd()
    folder = "/data/log"
    try:
        with open(folder+"/"+file,"w+") as log:
            log.write(str(data))
    except FileNotFoundError:
        with open(folder+"/"+file,"w") as log:
            log.write(str(data))
    
    log.close()


#DEFINIR AMBIENTE DE TRABALHO
# PRD - PRODUCAO
# DEV - DESENVOLVIMENTO
#DEFINIR TIPO DE DADOS RETORNADO
# DICIONARIO
#SEQ		idSEQ
#IDS		idServer
#SRV		sServer
#SCT		City
#SCP		Pais
#SCC		CC
#SLT		Latitude_S
#SLO		Longitude_S
#STO		Latencia_S
#VDL		Download
#VUL		Upload
#CIP		IP_Address1
#CNM		ISP
#CRT		ISP_Rate
#CCC		CCCLiente
#CLT		Latitude_C
#CLO		Longitude_C
#CTM		Timestamp_C
#THC		HoraColeta

if  len(sys.argv) > 2 :  
    #  parametros de ambiente
    if  sys.argv[1].upper() =="PRD":
        #print("AMBIENTE DE PRODUCAI")
        #base producao
        connection = mysql_connection('192.168.175.49', 'script', 'Lun@17N0V3', 'NETMON')
    elif sys.argv[1].upper() =="DEV":
        #print("AMBIENTE DE DESENVOLVIMENTO")
        #base de teste
        connection = mysql_connection('192.168.175.49', 'script', 'Lun@17N0V3', 'NETMONTE')
    else:
        #quando o comando é chamado com o parametro de banco invalido o scritp assume o ambiente e dev
        print("WARNING: Invalid environment argument. Assuming development/test environment.")
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
        # RETORNANDO os valores do segundo parametro
        if  sys.argv[2].upper() =="SEQ":
            print(idSEQ)
            gera_log("log_SEQ.log",idSEQ)
        elif sys.argv[2].upper() =="IDS":
            print(idServer)
            gera_log("log_IDS.log",idServer)
        elif sys.argv[2].upper() =="SRV":
            print(sServer)
            gera_log("log_SRV.log",sServer)
        elif sys.argv[2].upper() =="SCP":
            print(Pais)
            gera_log("log_SCP.log",Pais)
        elif sys.argv[2].upper() =="SCC":
            print(CC)
            gera_log("log_SCC.log",CC)
        elif sys.argv[2].upper() =="SLT":
            print(Latitude_S)
            gera_log("log_SLT.log",Latitude_S)
        elif sys.argv[2].upper() =="SLO":
            print(Longitude_S)
            gera_log("log_SLO.log",Longitude_S)
        elif sys.argv[2].upper() =="STO":
            print(Latencia_S)
            gera_log("log_STO.log",Latencia_S)
        elif sys.argv[2].upper() =="VDL":
            print(Download)
            gera_log("log_VDL.log",Download)
        elif sys.argv[2].upper() =="VUL":
            print(Upload)
            gera_log("log_VUL.log",Upload)
        elif sys.argv[2].upper() =="CIP":
            print(IP_Address)
            gera_log("log_CIP.log",IP_Address)
        elif sys.argv[2].upper() =="CNM":
            print(ISP)
            gera_log("log_CNM.log",ISP)
        elif sys.argv[2].upper() =="CRT":
            print(ISP_Rate)
            gera_log("log_CRT.log",ISP_Rate)
        elif sys.argv[2].upper() =="CCC":
            print(CCCLiente)
            gera_log("log_CCC.log",CCCLiente)
        elif sys.argv[2].upper() =="CLT":
            print(Latitude_C)
            gera_log("log_CLT.log",Latitude_C)
        elif sys.argv[2].upper() =="CLO":
            print(Longitude_C)
            gera_log("log_CLO.log",Longitude_C)
        elif sys.argv[2].upper() =="CTM":
            print(Timestamp_C)
            gera_log("log_CTM.log",Timestamp_C)
        elif sys.argv[2].upper() =="THC":
            print(HoraColeta)
            gera_log("log_THC.log",HoraColeta)
        else:
            print("WARNING: Invalid data argument. Assuming time execution script.")
    connection.close()
else:
    #quando o comando é chamado sem parametros o scritp assume o ambiente e dev e retorna o campo hora da coleta
    print("ERROR: Missing all arguments.")
print("OK: Script done.")    