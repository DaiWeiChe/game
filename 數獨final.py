# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 19:39:07 2022

@author: user
"""
#pip install numpy
import random
import numpy as np
import time


# 以現有數獨創造新的數獨矩陣(模擬魔術方塊轉動)
def random_sudo(sudo, times):
    ranlist=[0,3,6]
    for _ in range(times):
        # 隨機交換兩行
        rand_row_base = random.sample(ranlist, 1)  ##隨機取任一個3*3小九宮格(0,3,6分別代表從左數來第1,,3個3*3小九宮格
        rand_rows = random.sample(range(3), 2)   ##從小九宮格中取任意兩行
        row_1 = rand_row_base[0] + rand_rows[0]
        row_2 = rand_row_base[0] + rand_rows[1]
        sudo[[row_1, row_2], :] = sudo[[row_2, row_1], :]
    
        # 隨機交換兩列
        rand_col_base = random.sample(ranlist, 1)
        rand_cols = random.sample(range(3), 2)
        col_1 = rand_col_base[0] + rand_cols[0]
        col_2 = rand_col_base[0] + rand_cols[1]
        sudo[:, [col_1, col_2]] = sudo[:, [col_2, col_1]]
           
        #小九宮格互換:列交換
        rand_block_base = random.sample(ranlist, 2)
        block_1 = [rand_block_base[0] ,rand_block_base[0]+1,rand_block_base[0]+2]
        block_2 = [rand_block_base[1] ,rand_block_base[1]+1,rand_block_base[1]+2]
        sudo[block_1+block_2,:] = sudo[block_2+block_1,:]
           
        #小九宮格互換:行交換
        rand_block_base = random.sample(ranlist, 2)
        block_1 = [rand_block_base[0] ,rand_block_base[0]+1,rand_block_base[0]+2]
        block_2 = [rand_block_base[1] ,rand_block_base[1]+1,rand_block_base[1]+2]
        sudo[:,block_1+block_2] = sudo[:,block_2+block_1]

        
###清除隨機空格
def get_sudo_subject(sudo, del_nums):
    subject = sudo.copy()
 
    # 依照級別清除不同數量數字
    #初級清除15、中級44、高級55、困難59
    clears = random.sample(range(81), del_nums)
    for clear_index in clears:
        # 0-80轉換為行列索引
        row_index = clear_index // 9
        col_index = clear_index % 9
        subject[row_index, col_index] = 0
    return subject        
      
###視覺化
def print_sudo2(sudo):
    base = 3
    side = base*base
    def expandLine(line):
        return line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:13]
    line0  = expandLine("╔═══╤═══╦═══╗")
    line1  = expandLine("║ . │ . ║ . ║")
    line2  = expandLine("╟───┼───╫───╢")
    line3  = expandLine("╠═══╪═══╬═══╣")
    line4  = expandLine("╚═══╧═══╩═══╝")

    symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums   = [ [""]+[symbol[n] for n in row] for row in sudo ]
    print(line0)
    for r in range(1,side+1):
        print( "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )
        print([line2,line3,line4][(r%side==0)+(r%base==0)])


####數獨遊戲


def play_sudo():
    
    x = input("歡迎遊玩數獨!\n"+"選擇遊玩難度(初級、中級、高級、困難):")
    if x == "初級":
        sudo_degree = 15
    elif x == "中級":
        sudo_degree = 44
    elif x == "高級":
        sudo_degree = 55
    elif x == "困難":
        sudo_degree = 59
    else :
        sudo_degree = random.sample(range(35,60), 1)
        print("未指定難度，將隨機生成難度!!!")
    
    print("即將生成數獨",end="")
    for i in range(14):
        if i < 5:
            print(".",end="")
            time.sleep(0.8)
        elif i < 13:
            print(".",end="")
            time.sleep(0.2)
        else :
            print("........................")
        
    ###創造基礎數獨矩陣
    board=[[5, 2, 7, 8, 9, 3, 6, 4, 1],\
          [9, 3, 4, 6, 1, 2, 5, 7, 8],\
          [6, 1, 8, 5, 7, 4, 2, 3, 9],\
          [2, 4, 6, 9, 3, 8, 1, 5, 7],\
          [1, 9, 3, 2, 5, 7, 8, 6, 4],\
          [8, 7, 5, 1, 4, 6, 9, 2, 3],\
          [3, 5, 2, 7, 8, 1, 4, 9, 6],\
          [7, 8, 9, 4, 6, 5, 3, 1, 2],\
          [4, 6, 1, 3, 2, 9, 7, 8, 5]]
    sudo = np.array(board)
    
    ###創造新的數獨
    random_sudo(sudo,50)
    sudo_subj=get_sudo_subject(sudo,sudo_degree)
    
    print("遊戲開始!!!")
    print_sudo2(sudo_subj)
    checkinput=list(range(1,10)) 
    while True :
        position = input("選擇要填上的位置(由上至下,由左至右)並以空格分隔 : ").split()
        position[0],position[1] = int(position[0]),int(position[1])
        ans = int(input("要填入的數字(1-9) : "))
        n=0
        while n==0 :
            if position[0] not in checkinput or position[0] not in checkinput or ans not in checkinput :
                print("輸入格式錯誤!!!")
                break
            
            elif sudo_subj[position[0]-1,position[1]-1] != 0 :   
                change_ans = input("該格已有數字存在，確定要更改?(y/n)")
                
                if change_ans.lower() == "y" :
                    
                    sudo_subj[position[0]-1,position[1]-1] = ans
                    print_sudo2(sudo_subj)
                    n=1
                else :
                    break
            
            else:
                sudo_subj[position[0]-1,position[1]-1] = ans
                print_sudo2(sudo_subj)
                n=1
        last = 0
        for i in range(9):
            for j in range(9):
                if sudo_subj[i,j] == 0:
                    last+=1
        correct = 0
        for i in range(9):
            for j in range(9):
                if sudo_subj[i,j] == sudo[i,j]:
                    correct+=1
        
        if correct == 81 :
            print('\033[1;34;1m 恭喜你完成數獨!!!\n你的答案與解答相同!\033[0m\n')
            break
        elif last == 0:
            print("你完成了!\n"+"但似乎有哪裡填錯了...\n"+"好好檢查一下")
            continue

play_sudo()



    