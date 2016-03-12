# -*- coding: utf-8 -*-
import pygal
from atendimentos import simulaAtendimento

MAX_EVENTOS = 1000 #Número máximo de chegadas e serviços
MAX_AMOSTRAS = 10000 #Número máximo de amostragens para cálculo da média
EXERCICIO = 3
CENARIO = 2

###OBS###
'''
    Resultado do 3.3 parece estranho.
    Para o 3.4 não se deve plotar gráfico, já que há apenas um lambda.
'''
#########


def main():
    print "Resolvendo para Exercicio "+str(EXERCICIO)+" Cenario "+str(CENARIO)
    (lista_lambda, lista_fila) = simulaAtendimento(MAX_AMOSTRAS, MAX_EVENTOS, EXERCICIO, CENARIO)
    
    ###Plotting do gráfico###
    line_chart = pygal.Line()
    line_chart.title = 'Exercicio '+str(EXERCICIO)+' Cenario '+str(CENARIO)
    line_chart.x_labels = map(str, lista_lambda)
    line_chart.add('Media na Fila', lista_fila)
    line_chart.render_in_browser()
    print "rodei"
    
    
    
    
    
main()