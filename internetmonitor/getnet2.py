#!/usr/bin/env python3
import json
import platform
import os
import time
import speedtest
import sqlite3
from mysql.connector import connect
from datetime import datetime


agora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#import pandas as pd
#Apaga a tela
os.system("clear")
print("Hora da coleta:", agora)
servers = []
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1
# conexao com o banco
def mysql_connection(host, user, passwd, database=None):
    connection = connect(
        host = host,
        user = user,
        passwd = passwd,
        database = database
    )
    return connection


s = speedtest.Speedtest(secure=True)
srvs = s.get_servers(servers)
bestsrv = s.get_best_server()
dl = s.download(threads=threads)
ul = s.upload(threads=threads)
results_dict = s.results.dict()
compar = results_dict.get('client')
tm = results_dict.get('timestamp')
print(" ")
print("Download...: ", '{:,.2f}'.format(dl/(1000*1000)), "Mpbs") 
print("Upload.....: ", '{:,.2f}'.format(ul/(1000*1000)), "Mpbs")
print("Sponsor....: ", bestsrv['id'], "-", bestsrv['sponsor']) 
print("Localidade.: ", bestsrv['name'])
print("Pais.......: ", bestsrv['country'], ",", bestsrv['cc'] )
print("Latitude...: ", bestsrv['lat'])
print("Longitude..: ", bestsrv['lon'])
print("Latencia...: ", bestsrv['latency'])
print(":..........................................................: ")
print("IP.........: ", compar['ip'])
print("Provedor...: ", compar['isp']);
print("Avaliacao..: ", compar['isprating']);
print("Latitude...: ", compar['lat']);
print("Longitude..: ", compar['lon']);
print("Pais.......: ", compar['country']);
print(":..........................................................: ")
print("Timestamp..: ", tm )

print('Gravando dados no banco...') 

#base de teste
#connection = mysql_connection('192.168.175.49', 'script', 'Lun@17N0V3', 'NETMONTE')
#base producao
connection = mysql_connection('192.168.175.49', 'script', 'Lun@17N0V3', 'NETMON')

	

query = """INSERT INTO HistoryNetDB ( idServer,sServer,City,Pais,CC,Latitude_S,Longitude_S,Latencia_S,Download,Upload,IP_Address,ISP,ISP_Rate,CCCLiente,Latitude_C,Longitude_C,Timestamp_C, HoraColeta ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s );"""
val = (int(bestsrv['id']), bestsrv['sponsor'], bestsrv['name'], bestsrv['country'], bestsrv['cc'], float(bestsrv['lat']), float(bestsrv['lon']), float(bestsrv['latency']), float(dl), float(ul),compar['ip'], compar['isp'], float(compar['isprating']), compar['country'], float(compar['lat']), float(compar['lon']), tm, agora )

cursor = connection.cursor()
cursor.execute(query, val)

connection.commit()

print('Dados inseridos com sucesso.')

connection.close()

