# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 10:12:16 2023

@author: user
"""

import numpy as np


maze = [[2, 2, 2, 2, 2, 2, 2],
        [2, 0, 0, 0, 0, 0, 2],
        [2, 0, 2, 0, 2, 0, 2],
        [2, 0, 0, 2, 0, 0, 2],
        [2, 2, 0, 2, 0, 2, 2],
        [2, 1, 0, 2, 0, 4, 2],
        [2, 2, 2, 2, 2, 2, 2]]

###建造牆壁
len(maze[0])        
list=[2]*(2+len(maze[0]))
for i in range(len(maze)) :
    maze[i].append(2)
    maze[i].insert(0,2)
maze.append(list)
maze.insert(0,list)
maze2 = np.array(maze)
maze2=maze2*5


while True :
    
    n_count = 0
    
    for i in range(len(maze2)-2):        ###排除牆壁不運算
        for j in range(len(maze2[0])-2): ###排除牆壁不運算
            
            if maze2[i+1,j+1] == 5 or maze2[i+1,j+1] == 20 :
                pass
            
            elif maze2[i+1,j+1] == 0 :
                maze_N = maze2[i+1-1,j+1]
                maze_S = maze2[i+1+1,j+1]
                maze_W = maze2[i+1,j+1-1]
                maze_E = maze2[i+1,j+1+1]
                count = 0
            
                if maze_N ==10 :
                    count +=1
                if maze_S ==10 :
                    count +=1
                if maze_W ==10 :
                    count +=1
                if maze_E ==10 :
                    count +=1
                if count == 3 :
                    maze2[i+1,j+1] = 10
                    n_count += 1
                    print(n_count)
    if n_count ==0 :
        print("走到終點")
        print(maze2)
        mouse_move_count = 0
        for i in range(len(maze2)) :
            for j in range(len(maze2[0])):
                if maze2[i,j] != 10:
                    mouse_move_count +=1
        print(f"共總了{mouse_move_count}步")
        break
    else :
        continue  