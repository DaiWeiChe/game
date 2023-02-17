# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 09:08:10 2022

@author: user
"""
def playtest() :
    
    while True :
        ap=input("輸入第一個座標(x,y)以空格分開\n").split()
        bp=input("輸入第二個座標(x,y)以空格分開\n").split()
        cp=input("輸入第三個座標(x,y)以空格分開\n").split()
        dp=input("輸入第四個座標(x,y)以空格分開\n").split()
        
        ap[0],ap[1]=int(ap[0]),int(ap[1])
        bp[0],bp[1]=int(bp[0]),int(bp[1])
        cp[0],cp[1]=int(cp[0]),int(cp[1])
        dp[0],dp[1]=int(dp[0]),int(dp[1])
           
        aline1=(abs((ap[0]-bp[0]))**2+abs((ap[1]-bp[1]))**2)**(1/2)
        aline2=(abs((ap[0]-cp[0]))**2+abs((ap[1]-cp[1]))**2)**(1/2)
        aline3=(abs((ap[0]-dp[0]))**2+abs((ap[1]-dp[1]))**2)**(1/2)
        
        bline1=(abs((ap[0]-bp[0]))**2+abs((ap[1]-bp[1]))**2)**(1/2)
        bline2=(abs((bp[0]-cp[0]))**2+abs((bp[1]-cp[1]))**2)**(1/2)
        bline3=(abs((bp[0]-dp[0]))**2+abs((bp[1]-dp[1]))**2)**(1/2)
        
        cline1=(abs((ap[0]-cp[0]))**2+abs((ap[1]-cp[1]))**2)**(1/2)
        cline2=(abs((bp[0]-cp[0]))**2+abs((bp[1]-cp[1]))**2)**(1/2)
        cline3=(abs((cp[0]-dp[0]))**2+abs((cp[1]-dp[1]))**2)**(1/2)
        
        dline1=(abs((ap[0]-dp[0]))**2+abs((ap[1]-dp[1]))**2)**(1/2)
        dline2=(abs((bp[0]-dp[0]))**2+abs((bp[1]-dp[1]))**2)**(1/2)
        dline3=(abs((cp[0]-dp[0]))**2+abs((cp[1]-dp[1]))**2)**(1/2)
        
        a=sorted([aline1,aline2,aline3])
        b=sorted([bline1,bline2,bline3])
        c=sorted([cline1,cline2,cline3])
        d=sorted([dline1,dline2,dline3])
    

        if a[2]==b[2] and a[2]==c[2]and a[2]==d[2]:
            if a[0]==a[1] :
                print("正方形!")
            else :
                print("長方形!")
        else :
            if a[0]==a[1]and b[0]==b[1]and c[0]==c[1] and d[0]==d[1]:
                print("菱形!")
            else:    
                print("非正方形或長方形或菱形")
        
        new=input("是否再測一次Y/N")
        if new.upper()=="Y":
            print('新測試')

        else:

            break
            
playtest()