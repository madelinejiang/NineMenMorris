#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
import argparse
import sys

import MorrisV


# In[4]:


def ABOpening(board,depth,alpha,beta,is_max):
    saved_b=""
    positions_count=0
    
    if depth==0:
        return MorrisV.StaticEstimation_O(board),1,""
    
    elif is_max:
        maxE=-sys.maxsize
        L=MorrisV.GenerateMovesOpening(board)
        for b in L:
            e,p_out,dv=ABOpening(b,depth-1,alpha,beta,not is_max)
            positions_count+=p_out
            maxE=max(maxE,e)
            if alpha<e:
                alpha=e
                saved_b=b
            if beta<=alpha:
                break
        return maxE,positions_count,saved_b
    
    else:
        minE=sys.maxsize
        L=MorrisV.GenerateBlackMovesOpening(board)
        for b in L:
            e,p_out,dv=ABOpening(b,depth-1,alpha,beta,not is_max)
            positions_count+=p_out
            minE=min(minE,e)
            if e<beta:
                beta=e
                saved_b=b
            if beta<=alpha:
                break
        return minE, positions_count,saved_b

        


# In[6]:


# board1="xxxBBBxxxxxxxxWWWxxxxxx".lower()
# estimate, positions, board_out=ABOpening(board1,5,-sys.maxsize,sys.maxsize,True)

# print("Board Position:",board_out )
# print("Positions evaluated by static estimation:", positions )
# print("AB estimate:", estimate )

board1,board2,depth=MorrisV.ReadInput()

capitalize_flag=False
for c in board1:
    if c.isupper():
        capitalize_flag=True
        break
        
estimate, positions, board_out=ABOpening(board1.lower(),depth,-sys.maxsize,sys.maxsize,True)
board_write=board_out

if capitalize_flag:
    board_write=MorrisV.CapitalizeCase(board_out)
    
print("Board Position:",board_write )
print("Positions evaluated by static estimation:", positions )
print("AB estimate:", estimate )

fo=open(board2,"w")
fo.write(board_write)
fo.close()


# In[ ]:




