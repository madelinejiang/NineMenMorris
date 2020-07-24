#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy
import argparse
import sys
import copy
#tree is byproduct of the search itself

import MorrisV


# In[3]:


def clean_input(b):
    #TODO do some error checking here
    return b.lower()


# In[4]:


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


def MiniMaxOpening(board,depth,is_max):
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
        o_out,l_out,b_out=MiniMaxOpening(b,depth-1, not is_max)
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
        
    
    


# In[14]:


board1,board2,depth=MorrisV.ReadInput()

capitalize_flag=False
for c in board1:
    if c.isupper():
        capitalize_flag=True
        break
        
estimate, positions, board_out=MiniMaxOpening(board1.lower(),depth,True)
board_write=board_out

if capitalize_flag:
    board_write=MorrisV.CapitalizeCase(board_out)
    
print("Board Position:",board_write )
print("Positions evaluated by static estimation:", positions )
print("MINIMAX estimate:", estimate )

fo=open(board2,"w")
fo.write(board_write)
fo.close()

