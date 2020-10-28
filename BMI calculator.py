# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 08:03:26 2019

@author: smokedpirate
"""

#BMI calculator 
weight = float( input("Your weight in kg: ") )
height = float( input("Your height in metre: ") )

BMI = weight/(height*height)

print("your BMI is: ",BMI)

if ( BMI < 16):
   print("severely underweight")

elif ( BMI >= 16 and BMI < 18.5):
   print("underweight")

elif ( BMI >= 18.5 and BMI < 25):
   print("Healthy")

elif ( BMI >= 25 and BMI < 30):
   print("overweight")

elif ( BMI >=30 and BMI < 35):
   print("Obese")

elif (BMI > 35):
    print("Extremely obese")
    
    
