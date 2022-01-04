# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 19:16:49 2021

@author: Aaron Ramirez
"""


import detectarbordes as borde



mascara6 = borde.mascara(1)
mascarabien  = borde.mascara(1.5)
mascara35 = borde.mascara(2)

imagen="TajMahal_orig.jpg"


borde.hig_bost(imagen, mascara6,"1")
borde.hig_bost(imagen, mascarabien,"1.5")
borde.hig_bost(imagen, mascara35,"2")


imagen2="cat.png"

borde.hig_bost(imagen2, mascara6,"1")
borde.hig_bost(imagen2, mascarabien,"1.5")
borde.hig_bost(imagen2, mascara35,"2")
    

imagen3= "mejorada.jpg"

borde.hig_bost(imagen3, mascara6, "1")
borde.hig_bost(imagen3, mascarabien, "1.5")
borde.hig_bost(imagen3, mascara35, "2")
