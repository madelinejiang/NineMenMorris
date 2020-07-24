#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
import argparse
import sys
import copy
#tree is byproduct of the search itself

import MorrisV


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

#TODO
#movegenerator FOR BLACK
###flip->generate for white L
############->for every b in l flip


def GenerateMovesOpening(b):
    L=[]
#     b_flip=SwapBW(b)
    L=GenerateAdd(b)
#     for board in L:
#         board=SwapBW(board)
    return L
    
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


#remember L is mutable
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
    N_cases={0:[3,8,1],             1:[0,4,2],             2:[1,5,13],             3:[0,4,9,6],             4:[3,1,5],             5:[4,2,12,7],             6:[10,3,7],             7:[6,11,5],             8:[0,20,9],             9:[8,10,17,3],             10:[9,14,6],             11:[16,12,7],             12:[11,13,19,5],             13:[12,22,2],             14:[17,15,10],             15:[14,16,18],             16:[15,11,19],             17:[9,20,18,14],             18:[15,17,19,21],             19:[18,16,22,12],             20:[8,21,17],             21:[20,22,18],             22:[21,19,13]           
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

# def MiniMaxOpening(board,depth,is_max):
#     #if is_max true then white's turn to play
#     L=[]
#     positions_count=0
#     out_val=0
#     saved_b=""
 
#     if is_max==True:
#         out_val=-sys.maxsize
    
#     else:
#         out_val=sys.maxsize
        
#     if depth==0:
#         se=MorrisV.StaticEstimation_O(board)
#         if is_max:
#             if se>out_val:
#                 out_val=se
#         else:
#             if se<out_val:
#                 out_val=se
#         return out_val, 1, ""
    
#     elif is_max:
#         L=MorrisV.GenerateMovesOpening(board)
#     else:
#         L=MorrisV.GenerateBlackMovesOpening(board)
    
#     for b in L:
#         o_out,l_out,b_out=MiniMaxOpening(b,depth-1, not is_max)
#         positions_count+=l_out
        
#         if is_max:
#             if o_out>out_val:
#                 out_val=o_out
#                 saved_b=b
#         else:
#              if o_out<out_val:
#                 out_val=o_out
#                 saved_b=b
#     return out_val, positions_count, saved_b
        
    
        
    
# def MiniMaxOpeningBlack(board,depth):
#     b_flipped=SwapBW(board)
#     out_val,positions_count,saved_w=MiniMaxOpening(b_flipped,depth,True)
   
#     return out_val, positions_count, SwapBW(saved_w)
        
    
            
# board1="xxxBBBxxxxxxxxWWWxxxxxx".lower()
# estimate, positions, board_out=MiniMaxOpeningBlack(board1,2)

# print("Board Position:",SwapBW(board_out) )
# print("Positions evaluated by static estimation:", positions )
# print("MINIMAX estimate:", estimate ) 

def MiniMaxOpeningBlack(board,depth,is_max):
    #if is_max true then white's turn to play
    L=[]
    positions_count=0
    out_val=0
    saved_b=""
 
    if is_max==True:
        out_val=-sys.maxsize
    
    else:
        out_val=sys.maxsize
        
    if depth==0:
        se=MorrisV.StaticEstimation_O(board)
        if is_max:
            if se>out_val:
                out_val=se
        else:
            if se<out_val:
                out_val=se
        return out_val, 1, ""
    
    elif is_max:
        L=MorrisV.GenerateMovesOpening(board)
    else:
        L=MorrisV.GenerateBlackMovesOpening(board)
    
    for b in L:
        o_out,l_out,b_out=MiniMaxOpeningBlack(b,depth-1, not is_max)
        positions_count+=l_out
        
        if is_max:
            if o_out>out_val:
                out_val=o_out
                saved_b=b
        else:
             if o_out<out_val:
                out_val=o_out
                saved_b=b
    return out_val, positions_count, saved_b

board1,board2,depth=MorrisV.ReadInput()

capitalize_flag=False
for c in board1:
    if c.isupper():
        capitalize_flag=True
        break
        
estimate, positions, board_out=MiniMaxOpeningBlack(board1.lower(),depth,False)
board_write=board_out

if capitalize_flag:
    board_write=MorrisV.CapitalizeCase(board_out)
    
print("Board Position:",board_write )
print("Positions evaluated by static estimation:", positions )
print("MINIMAX estimate:", estimate )

fo=open(board2,"w")
fo.write(board_write)
fo.close()
    
    

