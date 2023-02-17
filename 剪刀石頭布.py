# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 09:21:18 2023

@author: user
"""
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def playpsr():
    pic=[rock,paper,scissors]
    ag=[]
    n=0
    while n==0:
        pcx=input("選擇出石頭、剪刀、布")
        npc=random.sample(range(0,3), 1)
        if pcx =="石頭":
            pc = 0
        elif pcx =="布":
            pc = 1
        elif pcx =="剪刀":
            pc = 2
        else :
            print("請輸入正確文字!")
            break
        
        if pc - npc[0] ==-1 :
            print("玩家",pic[pc])
            print("電腦",pic[npc[0]])
            print("你輸了")
        elif pc - npc[0] == 0 :
            print("玩家",pic[pc])
            print("電腦",pic[npc[0]])
            print("平手!")
        else :
            print("玩家",pic[pc])
            print("電腦",pic[npc[0]])
            print("你贏了!")
        ag=input("再玩一次?(y/n)").upper()
        if ag =="Y" or ag =="YES" :
            n=0
        else :
            n=1

playpsr()