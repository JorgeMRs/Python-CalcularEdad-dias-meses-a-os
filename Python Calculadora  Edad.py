# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 22:43:44 2022

@author: jocad
"""

def calcular_edad(dia_nacio:int, mes_nacio:int,anio_nacio:int,dia_actual:int,mes_actual:int,anio_actual:int)->int:
    MN = mes_nacio
    DN = dia_nacio
    AN = anio_nacio
  
    
    dias_naci  = (DN + ((MN - 1) * 30)) + ( (360 * anio_nacio) -1 )

    dias_acual = (dia_actual + ((mes_actual - 1) * 30)) + ( (360 * anio_actual) -1 )
    
     
    dias_sobra = dias_acual - dias_naci 
  
    años  = 0         
    dias_meses = 0
    meses = 0
    dias  = 0
    sobras = 0
    
    
    if dias_sobra < 360:
        años = 0
        meses = (dias_sobra // 30) 
        dias =  dias_sobra - (meses * 30)
        
    else:
        
       
            años = dias_sobra // 360
            sobras = dias_sobra - (años * 360)
            while sobras // 30 >=1 :
                meses += 1
                sobras = sobras - 30
            dias = sobras % 30
               
            
    
    return "ustes tiene : ", años, " años con", meses , " meses y ", dias, " dias." 
   


 
