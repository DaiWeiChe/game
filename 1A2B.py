# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 08:53:34 2023

@author: user
"""

import random
import time 
run=input()



def playab():
    ans=random.sample(range(1, 10), 4)

    while True:
        a=0
        b=0
        x=input("輸入四位不重複數字")
        run=[int(x[0]),int(x[1]),int(x[2]),int(x[3])]
        run1=set(run)
        if len(run1)==4 :
            for i in range(0,4,1):
                if run[i]==ans[i]:
                    a+=1
            for i in range(0,4,1):
                for j in range(0,4,1):
                    if run[i]==ans[j]:
                        b+=1
            b-= a
            if a == 4 :
                print("你答對了!")
                time.sleep(2)
                new=input("是否在新一局Y/N")
                if new.upper()=="Y":
                    print('新開一局')
                    ans=random.sample(range(1, 10), 4)

                else:
                    print("遊戲結束")
                    break
                    
            else :
                print(f"{a}a {b}b")
            
        else :
            print("注意數字不能重複!")


playab()