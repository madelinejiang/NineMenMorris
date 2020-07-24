#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import argparse
import sys


def ReadInput():
    parser = argparse.ArgumentParser()
    parser.add_argument("board1", help="board1 input filename")
    parser.add_argument("board2", help="board2 output filename")
    parser.add_argument("depth", help="search tree depth")
    args = parser.parse_args()
    #print(args.board1,args.board2)
    
    b1=open(args.board1,"r")
    inputboard=b1.read()
    b1.close()    
    return inputboard,args.board2,int(args.depth)

def CapitalizeCase(b):
    b_new=[]
    for c in b:
        piece=c
        if c=="w" or c=="b":
            piece=c.upper()
        b_new.append(piece)
    return "".join(b_new)

def SwapBW(b):
    tempb_list=[]
    for char in b:
        tempc=char
        if char=="b":
            tempc="w"
        elif char=="w":
            tempc="b"
        tempb_list.append(tempc)
    return ''.join(tempb_list)


def GenerateMovesOpening(b):
    L=[]
    L=GenerateAdd(b)
    return L

def GenerateBlackMovesOpening(b):
    swap_b=SwapBW(b)
    L_b=GenerateMovesOpening(swap_b)
    for i in range(len(L_b)):
        L_b[i]=SwapBW(L_b[i])        
    return L_b
    
def GenerateAdd(b):
    L=[]
    for location in range(len(b)):
        if b[location]=="x":
            b_list=list(b)
            b_list[location]="w"
            b_copy="".join(b_list)
            
            if closeMill(location,b_copy):
                GenerateRemove(b_copy,L)
            else:
                L.append(b_copy)       
    return L


def GenerateMovesMidgameEndgame(b):
    if b.count("w")==3:
        #print("Call Hop")
        return GenerateHopping(b)
    else:
        #print("Call GenMove")
        return GenerateMove(b)
    
def GenerateBlackMovesMidgameEndgame(b):
    swap_b=SwapBW(b)
    L_b=GenerateMovesMidgameEndgame(swap_b)
    for i in range(len(L_b)):
        L_b[i]=SwapBW(L_b[i])        
    return L_b
    
def GenerateHopping(b):
    L=[]
    indices=[i for i,position in enumerate(b) if position=="w"]
    for j in indices:
        for location,piece in enumerate(b):
            if piece=="x":
                b_list=list(b)
                b_list[j]="x"
                b_list[location]="w"
                b_copy="".join(b_list)
                if closeMill(location,b_copy):
                    GenerateRemove(b_copy,L)
                else:
                    L.append(b_copy)
    return L

def GenerateMove(b):
    L=[]
    for location,piece in enumerate(b):
        if piece=="w":
            n=neighbors(location)
            for j in n:
                if b[j]=="x":
                    #print("Gen move from",location,"to",j)
                    b_list=list(b)
                    b_list[location]="x"
                    b_list[j]="w"
                    b_copy="".join(b_list)
                    if closeMill(j,b_copy):
                        GenerateRemove(b_copy,L)
                    else:
                        L.append(b_copy)
    return L


def GenerateRemove(b,L):
    #print("Called remove")
    for location in range(len(b)):
        if b[location]=="b":
            if not closeMill(location,b):
                b_copy=list(b)
                b_copy[location]="x"
                L.append("".join(b_copy))
    return

def neighbors(j):
    N=[]
    N_cases={0:[1,3,8],             1:[0,2,4],             2:[1,5,13],             3:[0,4,6,9],             4:[1,3,5],             5:[2,4,7,12],             6:[3,7,10],             7:[5,6,11],             8:[0,9,20],             9:[3,8,10,17],             10:[6,9,14],             11:[7,12,16],             12:[5,11,13,19],             13:[2,12,22],             14:[10,15,17],             15:[14,16,18],             16:[11,15,19],             17:[9,14,18,20],             18:[15,17,19,21],             19:[12,16,18,22],             20:[8,17,21],             21:[18,20,22],             22:[13,19,21]           
            }

    return N_cases.get(j,[-1])
    
def closeMill(j,b):
    C=b[j]
    if C=="x":
        return False
    if j==0:
        if C==b[1] and C==b[2]:
            return True
        elif C==b[3] and C==b[6]:
            return True
        elif C==b[8] and C==b[20]:
            return True
        else:
            return False
        
    elif j==1:
        if C==b[0] and C==b[2]:
            return True
        else:
            return False
    elif j==2:
        if C==b[0] and C==b[1]:
            return True
        elif C==b[5] and C==b[7]:
            return True
        elif C==b[13] and C==b[22]:
            return True
        else:
            return False
    elif j==3:
        if C==b[4] and C==b[5]:
            return True
        elif C==b[0] and C==b[6]:
            return True
        elif C==b[9] and C==b[17]:
            return True
        else:
            return False
    elif j==4:
        if C==b[3] and C==b[5]:
            return True
        else:
            return False
    elif j==5:
        if C==b[3] and C==b[4]:
            return True
        elif C==b[2] and C==b[7]:
            return True
        elif C==b[12] and C==b[19]:
            return True
        else:
            return False
    elif j==6:
        if C==b[0] and C==b[3]:
            return True
        elif C==b[10] and C==b[14]:
            return True
        else:
            return False
    elif j==7:
        if C==b[2] and C==b[5]:
            return True
        elif C==b[11] and C==b[16]:
            return True
        else:
            return False
        
    elif j==8:
        if C==b[9] and C==b[10]:
            return True
        elif C==b[0] and C==b[20]:
            return True
        else:
            return False
    elif j==9:
        if C==b[8] and C==b[10]:
            return True
        elif C==b[3] and C==b[17]:
            return True
        else:
            return False
    elif j==10:
        if C==b[8] and C==b[9]:
            return True
        elif C==b[6] and C==b[14]:
            return True
        else:
            return False
    if j==11:
        if C==b[7] and C==b[16]:
            return True
        elif C==b[12] and C==b[13]:
            return True
        else:
            return False
    elif j==12:
        if C==b[11] and C==b[13]:
            return True
        elif C==b[5] and C==b[19]:
            return True
        else:
            return False
    elif j==13:
        if C==b[11] and C==b[12]:
            return True
        elif C==b[2] and C==b[22]:
            return True
        else:
            return False
    elif j==14:
        if C==b[15] and C==b[16]:
            return True
        elif C==b[20] and C==b[17]:
            return True
        elif C==b[6] and C==b[10]:
            return True
        else:
            return False
    elif j==15:
        if C==b[14] and C==b[16]:
            return True
        elif C==b[18] and C==b[21]:
            return True
        else:
            return False
    elif j==16:
        if C==b[14] and C==b[15]:
            return True
        elif C==b[7] and C==b[11]:
            return True
        elif C==b[19] and C==b[22]:
            return True
        else:
            return False
    elif j==17:
        if C==b[3] and C==b[9]:
            return True
        elif C==b[18] and C==b[19]:
            return True
        elif C==b[14] and C==b[20]:
            return True
        else:
            return False
    elif j==18:
        if C==b[17] and C==b[19]:
            return True
        elif C==b[15] and C==b[21]:
            return True
        else:
            return False
    elif j==19:
        if C==b[17] and C==b[18]:
            return True
        elif C==b[16] and C==b[22]:
            return True
        elif C==b[5] and C==b[12]:
            return True
        else:
            return False
    elif j==20:
        if C==b[0] and C==b[8]:
            return True
        elif C==b[14] and C==b[17]:
            return True
        elif C==b[21] and C==b[22]:
            return True
        else:
            return False
    elif j==21:
        if C==b[20] and C==b[22]:
            return True
        elif C==b[15] and C==b[18]:
            return True
        else:
            return False
    elif j==22:
        if C==b[20] and C==b[21]:
            return True
        elif C==b[16] and C==b[19]:
            return True
        elif C==b[2] and C==b[13]:
            return True
        else:
            return False
    else:
        print("error in closeMill")
        return False
     
        
        
def StaticEstimation_O(b):
    return b.count("w")-b.count("b")


def StaticEstimation_MEgame(b):
    
    numWhitePieces=b.count("w")
    numBlackPieces=b.count("b")
    L=[]
    numBlackMoves=0
    
    if numBlackPieces<=2:
        return 10000
    elif numWhitePieces<=2:
        return -10000
    
    L=GenerateMovesMidgameEndgame(SwapBW(b))
    numBlackMoves=len(L)
    
    if numBlackMoves==0:
        return 10000
    else:
        return(1000*(numWhitePieces-numBlackPieces)-numBlackMoves)
    return

def CountMills(b,color):
    out=0
    m=[b[0],b[1],b[2]]
    if m.count(color)==3:
        out+=1
    m=[b[3],b[4],b[5]]
    if m.count(color)==3:
        out+=1
    m=[b[8],b[9],b[10]]
    if m.count(color)==3:
        out+=1
    m=[b[11],b[12],b[13]]
    if m.count(color)==3:
        out+=1
    m=[b[14],b[15],b[16]]
    if m.count(color)==3:
        out+=1
    m=[b[17],b[18],b[19]]
    if m.count(color)==3:
        out+=1
    m=[b[20],b[21],b[22]]
    if m.count(color)==3:
        out+=1
    m=[b[0],b[8],b[20]]
    if m.count(color)==3:
        out+=1
    m=[b[3],b[8],b[17]]
    if m.count(color)==3:
        out+=1
    m=[b[6],b[10],b[14]]
    if m.count(color)==3:
        out+=1
    m=[b[15],b[18],b[21]]
    if m.count(color)==3:
        out+=1
    m=[b[7],b[11],b[16]]
    if m.count(color)==3:
        out+=1
    m=[b[5],b[12],b[19]]
    if m.count(color)==3:
        out+=1
    m=[b[2],b[13],b[22]]
    if m.count(color)==3:
        out+=1
    m=[b[0],b[3],b[5]]
    if m.count(color)==3:
        out+=1
    m=[b[14],b[17],b[20]]
    if m.count(color)==3:
        out+=1
    m=[b[2],b[5],b[7]]
    if m.count(color)==3:
        out+=1
    m=[b[16],b[19],b[22]]
    if m.count(color)==3:
        out+=1
        
    return out

def CanMill(b,color):
    out=0
    m=[b[0],b[1],b[2]]
    if m.count(color)==2 and m.count("x")==1:
        out+=1
    m=[b[3],b[4],b[5]]
    if m.count(color)==2 and m.count("x")==1:
        out+=1
    m=[b[8],b[9],b[10]]
    if m.count(color)==2 and m.count("x")==1:
        out+=1
    m=[b[11],b[12],b[13]]
    if m.count(color)==2 and m.count("x")==1:
        out+=1
    m=[b[14],b[15],b[16]]
    if m.count(color)==2 and m.count("x")==1:
        out+=1
    m=[b[17],b[18],b[19]]
    if m.count(color)==2 and m.count("x")==1:
        out+=1
    m=[b[20],b[21],b[22]]
    if m.count(color)==2 and m.count("x")==1:
        out+=1
    m=[b[0],b[8],b[20]]
    if m.count(color)==2 and m.count("x")==1:
        out+=1
    m=[b[3],b[8],b[17]]
    if m.count(color)==2 and m.count("x")==1:
        out+=1
    m=[b[6],b[10],b[14]]
    if m.count(color)==2 and m.count("x")==1:
        out+=1
    m=[b[15],b[18],b[21]]
    if m.count(color)==2 and m.count("x")==1:
        out+=1
    m=[b[7],b[11],b[16]]
    if m.count(color)==2 and m.count("x")==1:
        out+=1
    m=[b[5],b[12],b[19]]
    if m.count(color)==2 and m.count("x")==1:
        out+=1
    m=[b[2],b[13],b[22]]
    if m.count(color)==2 and m.count("x")==1:
        out+=1
    m=[b[0],b[3],b[5]]
    if m.count(color)==2 and m.count("x")==1:
        out+=1
    m=[b[14],b[17],b[20]]
    if m.count(color)==2 and m.count("x")==1:
        out+=1
    m=[b[2],b[5],b[7]]
    if m.count(color)==2 and m.count("x")==1:
        out+=1
    m=[b[16],b[19],b[22]]
    if m.count(color)==2 and m.count("x")==1:
        out+=1
    
    return out



def ImpStaticEstimation_O(b):
    se= b.count("w")-b.count("b")
    count=CountMills(b,"w")-CountMills(b,"b")
    can=CanMill(b,"w")-CanMill(b,"b")
    
    if can>1:
        can=2
    elif can<-1:
        can=-2
        
    x=4*se+2*count+can
    
    return x

def ImpStaticEstimation_MEgame(b):
    
    numWhitePieces=b.count("w")
    numBlackPieces=b.count("b")
    L=[]
    numBlackMoves=0
    
    if numBlackPieces<=2:
        return 10000
    elif numWhitePieces<=2:
        return -10000
    
    L=GenerateMovesMidgameEndgame(SwapBW(b))
    numBlackMoves=len(L)
    
    L_w=GenerateMovesMidgameEndgame(b)
    numWhiteMoves=len(L_w)
    
    if numBlackMoves==0:
        return 10000
    elif numWhiteMoves==0:
        return -10000
    else:
        
        return(1000*(numWhitePieces-numBlackPieces)+numWhiteMoves-numBlackMoves+CountMills(b,"w")-CountMills(b,"b"))

        #return(1000*(numWhitePieces-numBlackPieces)+numWhiteMoves-numBlackMoves)
 

