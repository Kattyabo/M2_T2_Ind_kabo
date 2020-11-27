# -*- coding: utf-8 *-* 

import bs4
import requests
import M2_T2_Katherine_Barrera.volumen_M2_T2

#solicitud del volumen de radio
radio_esfera = int(input("Favor ingrese radio de la esfera: "))

#sólo se pueden importar constantes
volumen_esferas = 4/3 * 3.14159 * radio_esfera ** 3

#impresión resultados
print("el resultado del volumen de la esfera es: " + str(volumen_esferas))