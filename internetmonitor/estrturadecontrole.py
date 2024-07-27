#!/usr/bin/env python3
import os
import sys

if  len(sys.argv) > 1 :
    if  sys.argv[1].upper() =="SERVER":
        print("Escolhido servidor")
        
    elif sys.argv[1].upper() =="CLIENTE":
        print("Escolhido Cliente")
    elif sys.argv[1].upper() =='DTEX':
        print("Escolhido Hora de Execução")
    else:
        print("Parametro Inválido")

    print("Argurmento passado ", sys.argv[1].upper())
    print("ARG:", sys.argv)

else:
    print("Usando modelo padrao")    

