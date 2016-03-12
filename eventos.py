# -*- coding: utf-8 -*-

import numpy
#from main import MAX_EVENTOS

###
def geraListaEventos(MAX_EVENTOS, taxaChegada1, tipoSaida1, taxaSaida1, taxaChegada2=None, tipoSaida2=None, taxaSaida2=None):
    prox_evento = ""
    lista_eventos = []
    
    ###1 Saída Exponencial (Cenário 1)###
    if tipoSaida1 == "exponencial" and tipoSaida2 == None:
        for k in range(MAX_EVENTOS):
            tempo_chegada = numpy.random.exponential(1/taxaChegada1) #Pega um tempo de chegada
            tempo_saida = numpy.random.exponential(1/taxaSaida1) #Pega um tempo de saída
            
            #Confere qual tempo é menor e atribui se o próximo evento  é chegada ou saída
            if tempo_chegada < tempo_saida:
                prox_evento = "chegada"
            elif tempo_chegada > tempo_saida:
                prox_evento = "saida"
            
            lista_eventos.append(prox_evento)
                
    ###2 Saídas Exponenciais (Cenário 2)###
    if tipoSaida1 == "exponencial" and tipoSaida2 == "exponencial":
        fila_tipo1 = 0 ###OBS: inclui servidor
        fila_tipo2 = 0 ###OBS: inclui servidor
        #lista_eventos.append("debug")
        for k in range(MAX_EVENTOS):           
            #print fila_tipo1+fila_tipo2, lista_eventos[-1]
            if fila_tipo1 == 0 and fila_tipo2 == 0: #Se não há ninguém na fila, só chegadas podem ocorrer
                #print "ninguem na fila no evento " + str(k)
                tempo_chegada1 = numpy.random.exponential(1/(taxaChegada1))
                tempo_chegada2 = numpy.random.exponential(1/(taxaChegada2))
                
                if tempo_chegada1 < tempo_chegada2:
                    prox_evento = "chegada1"
                    fila_tipo1+=1
                else:
                    prox_evento = "chegada2"
                    fila_tipo2+=1
            else:#Se há alguém na fila
                if fila_tipo1 == 0 and fila_tipo2 != 0:#Só há tipo2 na fila, logo só chegadas e saídas2 podem ocorrer
                    tempo_chegada1 = numpy.random.exponential(1/(taxaChegada1))
                    tempo_chegada2 = numpy.random.exponential(1/(taxaChegada2))
                    tempo_saida2 = numpy.random.exponential(1/(taxaSaida2))
                    
                    menor_tempo = min(tempo_chegada1, tempo_chegada2, tempo_saida2)
                    
                    if menor_tempo == tempo_chegada1:#ocorreu uma chegada1
                        prox_evento = "chegada1"
                        fila_tipo1+=1
                    elif menor_tempo == tempo_chegada2:#ocorreu uma chegada2
                        prox_evento = "chegada2"
                        fila_tipo2+=1
                    elif menor_tempo == tempo_saida2:#ocorreu uma saida2
                        prox_evento = "saida2"
                        fila_tipo2-=1
                elif fila_tipo1 != 0 and fila_tipo2 == 0:#Apenas chegadas e saídas1 podem ocorrer
                    tempo_chegada1 = numpy.random.exponential(1/(taxaChegada1))
                    tempo_chegada2 = numpy.random.exponential(1/(taxaChegada2))
                    tempo_saida1 = numpy.random.exponential(1/(taxaSaida1))
                    
                    menor_tempo = min(tempo_chegada1, tempo_chegada2, tempo_saida1)
                    
                    if menor_tempo == tempo_chegada1:#ocorreu uma chegada1
                        prox_evento = "chegada1"
                        fila_tipo1+=1
                    elif menor_tempo == tempo_chegada2:#ocorreu uma chegada2
                        prox_evento = "chegada2"
                        fila_tipo2+=1
                    elif menor_tempo == tempo_saida1:#ocorreu uma saida1
                        prox_evento = "saida1"
                        fila_tipo1-=1
                else: #Chegadas e saídas de quaisquer tipo podem ocorrer
                    tempo_chegada1 = numpy.random.exponential(1/(taxaChegada1))
                    tempo_chegada2 = numpy.random.exponential(1/(taxaChegada2))
                    tempo_saida1 = numpy.random.exponential(1/(taxaSaida1))
                    tempo_saida2 = numpy.random.exponential(1/(taxaSaida2))
                    
                    menor_tempo = min(tempo_chegada1, tempo_chegada2, tempo_saida1, tempo_saida2)
                    
                    if menor_tempo == tempo_chegada1:#ocorreu uma chegada1
                        prox_evento = "chegada1"
                        fila_tipo1+=1
                    elif menor_tempo == tempo_chegada2:#ocorreu uma chegada2
                        prox_evento = "chegada2"
                        fila_tipo2+=1
                    elif menor_tempo == tempo_saida1:#ocorreu uma saida1
                        prox_evento = "saida1"
                        fila_tipo1-=1
                    elif menor_tempo == tempo_saida2:#ocorreu uma saida2
                        prox_evento = "saida2"
                        fila_tipo2-=1

            lista_eventos.append(prox_evento)
    ###2 Saídas Determinísticas (Cenário 3)###
    if tipoSaida1 == "deterministica" and tipoSaida2 == "deterministica":
        fila_tipo1 = 0 ###OBS: inclui servidor
        fila_tipo2 = 0 ###OBS: inclui servidor
        #lista_eventos.append("debug")
        for k in range(MAX_EVENTOS):           
            #print fila_tipo1+fila_tipo2, lista_eventos[-1]
            if fila_tipo1 == 0 and fila_tipo2 == 0: #Se não há ninguém na fila, só chegadas podem ocorrer
                #print "ninguem na fila no evento " + str(k)
                tempo_chegada1 = numpy.random.exponential(1/(taxaChegada1))
                tempo_chegada2 = numpy.random.exponential(1/(taxaChegada2))
                
                if tempo_chegada1 < tempo_chegada2:
                    prox_evento = "chegada1"
                    fila_tipo1+=1
                else:
                    prox_evento = "chegada2"
                    fila_tipo2+=1
            else:#Se há alguém na fila
                if fila_tipo1 == 0 and fila_tipo2 != 0:#Só há tipo2 na fila, logo só chegadas e saídas2 podem ocorrer
                    tempo_chegada1 = numpy.random.exponential(1/(taxaChegada1))
                    tempo_chegada2 = numpy.random.exponential(1/(taxaChegada2))
                    tempo_saida2 = 1/taxaSaida2
                    
                    menor_tempo = min(tempo_chegada1, tempo_chegada2, tempo_saida2)
                    
                    if menor_tempo == tempo_chegada1:#ocorreu uma chegada1
                        prox_evento = "chegada1"
                        fila_tipo1+=1
                    elif menor_tempo == tempo_chegada2:#ocorreu uma chegada2
                        prox_evento = "chegada2"
                        fila_tipo2+=1
                    elif menor_tempo == tempo_saida2:#ocorreu uma saida2
                        prox_evento = "saida2"
                        fila_tipo2-=1
                elif fila_tipo1 != 0 and fila_tipo2 == 0:#Apenas chegadas e saídas1 podem ocorrer
                    tempo_chegada1 = numpy.random.exponential(1/(taxaChegada1))
                    tempo_chegada2 = numpy.random.exponential(1/(taxaChegada2))
                    tempo_saida1 = 1/taxaSaida1
                    
                    menor_tempo = min(tempo_chegada1, tempo_chegada2, tempo_saida1)
                    
                    if menor_tempo == tempo_chegada1:#ocorreu uma chegada1
                        prox_evento = "chegada1"
                        fila_tipo1+=1
                    elif menor_tempo == tempo_chegada2:#ocorreu uma chegada2
                        prox_evento = "chegada2"
                        fila_tipo2+=1
                    elif menor_tempo == tempo_saida1:#ocorreu uma saida1
                        prox_evento = "saida1"
                        fila_tipo1-=1
                else: #Chegadas e saídas de quaisquer tipo podem ocorrer
                    tempo_chegada1 = numpy.random.exponential(1/(taxaChegada1))
                    tempo_chegada2 = numpy.random.exponential(1/(taxaChegada2))
                    tempo_saida1 = 1/taxaSaida1
                    tempo_saida2 = 1/taxaSaida2
                    
                    menor_tempo = min(tempo_chegada1, tempo_chegada2, tempo_saida1, tempo_saida2)
                    
                    if menor_tempo == tempo_chegada1:#ocorreu uma chegada1
                        prox_evento = "chegada1"
                        fila_tipo1+=1
                    elif menor_tempo == tempo_chegada2:#ocorreu uma chegada2
                        prox_evento = "chegada2"
                        fila_tipo2+=1
                    elif menor_tempo == tempo_saida1:#ocorreu uma saida1
                        prox_evento = "saida1"
                        fila_tipo1-=1
                    elif menor_tempo == tempo_saida2:#ocorreu uma saida2
                        prox_evento = "saida2"
                        fila_tipo2-=1
            lista_eventos.append(prox_evento)
    ###2 Saídas Uniformes (Cenário 4)###
    if tipoSaida1 == "uniforme" and tipoSaida2 == "uniforme":
        fila_tipo1 = 0 ###OBS: inclui servidor
        fila_tipo2 = 0 ###OBS: inclui servidor
        for k in range(MAX_EVENTOS):           
            #print fila_tipo1+fila_tipo2, lista_eventos[-1]
            if fila_tipo1 == 0 and fila_tipo2 == 0: #Se não há ninguém na fila, só chegadas podem ocorrer
                #print "ninguem na fila no evento " + str(k)
                tempo_chegada1 = numpy.random.exponential(1/(taxaChegada1))
                tempo_chegada2 = numpy.random.exponential(1/(taxaChegada2))
                
                if tempo_chegada1 < tempo_chegada2:
                    prox_evento = "chegada1"
                    fila_tipo1+=1
                else:
                    prox_evento = "chegada2"
                    fila_tipo2+=1
            else:#Se há alguém na fila
                if fila_tipo1 == 0 and fila_tipo2 != 0:#Só há tipo2 na fila, logo só chegadas e saídas2 podem ocorrer
                    tempo_chegada1 = numpy.random.exponential(1/(taxaChegada1))
                    tempo_chegada2 = numpy.random.exponential(1/(taxaChegada2))
                    tempo_saida2 =  numpy.random.uniform(taxaSaida2[0], taxaSaida2[1])
                    
                    menor_tempo = min(tempo_chegada1, tempo_chegada2, tempo_saida2)
                    
                    if menor_tempo == tempo_chegada1:#ocorreu uma chegada1
                        prox_evento = "chegada1"
                        fila_tipo1+=1
                    elif menor_tempo == tempo_chegada2:#ocorreu uma chegada2
                        prox_evento = "chegada2"
                        fila_tipo2+=1
                    elif menor_tempo == tempo_saida2:#ocorreu uma saida2
                        prox_evento = "saida2"
                        fila_tipo2-=1
                elif fila_tipo1 != 0 and fila_tipo2 == 0:#Apenas chegadas e saídas1 podem ocorrer
                    tempo_chegada1 = numpy.random.exponential(1/(taxaChegada1))
                    tempo_chegada2 = numpy.random.exponential(1/(taxaChegada2))
                    tempo_saida1 =  numpy.random.uniform(taxaSaida1[0], taxaSaida1[1])
                    
                    menor_tempo = min(tempo_chegada1, tempo_chegada2, tempo_saida1)
                    
                    if menor_tempo == tempo_chegada1:#ocorreu uma chegada1
                        prox_evento = "chegada1"
                        fila_tipo1+=1
                    elif menor_tempo == tempo_chegada2:#ocorreu uma chegada2
                        prox_evento = "chegada2"
                        fila_tipo2+=1
                    elif menor_tempo == tempo_saida1:#ocorreu uma saida1
                        prox_evento = "saida1"
                        fila_tipo1-=1
                else: #Chegadas e saídas de quaisquer tipo podem ocorrer
                    tempo_chegada1 = numpy.random.exponential(1/(taxaChegada1))
                    tempo_chegada2 = numpy.random.exponential(1/(taxaChegada2))
                    tempo_saida1 =  numpy.random.uniform(taxaSaida1[0], taxaSaida1[1])
                    tempo_saida2 =  numpy.random.uniform(taxaSaida2[0], taxaSaida2[1])
                    
                    menor_tempo = min(tempo_chegada1, tempo_chegada2, tempo_saida1, tempo_saida2)
                    
                    if menor_tempo == tempo_chegada1:#ocorreu uma chegada1
                        prox_evento = "chegada1"
                        fila_tipo1+=1
                    elif menor_tempo == tempo_chegada2:#ocorreu uma chegada2
                        prox_evento = "chegada2"
                        fila_tipo2+=1
                    elif menor_tempo == tempo_saida1:#ocorreu uma saida1
                        prox_evento = "saida1"
                        fila_tipo1-=1
                    elif menor_tempo == tempo_saida2:#ocorreu uma saida2
                        prox_evento = "saida2"
                        fila_tipo2-=1
            lista_eventos.append(prox_evento)
        '''
        for k in range(MAX_EVENTOS):        
            tempo_chegada = numpy.random.exponential(1/(taxaChegada1+taxaChegada2))
            tempo_saida1 =  numpy.random.uniform(taxaSaida1[0], taxaSaida1[1])
            tempo_saida2 =  numpy.random.uniform(taxaSaida2[0], taxaSaida2[1])
            #print tempo_chegada, tempo_saida1, tempo_saida2
            if tempo_chegada < min(tempo_saida1, tempo_saida2):
                prox_evento = "chegada"
            elif tempo_chegada > min(tempo_saida1, tempo_saida2):
                if tempo_saida1 == min(tempo_saida1, tempo_saida2):
                    prox_evento = "saida1"
                else:
                    prox_evento = "saida2"
            
            lista_eventos.append(prox_evento)
            '''
        
    
    #print lista_eventos
    return lista_eventos
###
