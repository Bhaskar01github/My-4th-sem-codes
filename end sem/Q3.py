#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:33:39 2023

@author: bb21ms147
"""
import random
strg='Ram '
r1= random.random()

if r1 >0.4:                        
   print("ram choose sita")
   strg=strg+'Sita '
   gift1=random.random()
   if gift1>0.5:                        
       print("ram gives chocolates to sita")
       strg=strg+'W '
       gift2=random.random()
       if gift2>0.5:
           print("Sita gives perfume to ram" )
           strg+='P'
       else:
           print("Sita gives sunglasses to ram")
           strg+='S'
       
   else:
       print("ram gives chips to sita")
       strg=strg+'C'

   if strg=='Ram Sita W P':
       print("Correct pairs:[Ram,Sita],[Shyam,Gita]")
else:
    strg='Shyam '
    r2= random.random()

    if r2 >0.5:                        
       print("Shyam choose Gita")
       strg=strg+'Gita '
       sgift1=random.random()
       if sgift1>0.5:                        
           print("shyam gives chips to gita")
           strg=strg+'C '
           sgift2=random.random()
           if sgift2>0.5:
               print("Gita gives sunglasses to shyam" )
               strg+='S '
           else:
               print("Gita gives perfume to shyam")
               strg+='P '
       
       else:
          print("shyam gives chocolates to gita")
          strg=strg+'C'
        
      
        