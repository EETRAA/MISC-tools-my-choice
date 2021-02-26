# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 11:38:42 2021

@author: Administrator
"""

from tkinter import *
import wb

website_realtimehot = 'https://s.weibo.com/top/summary?cate=realtimehot'
website_socialevent = 'https://s.weibo.com/top/summary?cate=socialevent'

realtimehot = wb.weibo_hot(website_realtimehot)
socialevent = wb.weibo_hot(website_socialevent)

mainframe = Tk()
mainframe.config(bg = 'white')
mainframe.title('test')

frame2 = Toplevel()
frame2.config(bg = 'white')
frame2.title('test')

s=Scrollbar(mainframe)
l=Listbox(mainframe)
s2=Scrollbar(frame2)
l2=Listbox(frame2)

s.config(command = l.yview)
l.config(yscrollcommand = s.set, font = ('幼圆',20))
s2.config(command = l2.yview)
l2.config(yscrollcommand = s2.set, font = ('幼圆',20))

s.pack(side = RIGHT, fill = Y)
l.pack(side = LEFT, fill = BOTH, expand = TRUE)
s2.pack(side = RIGHT, fill = Y)
l2.pack(side = LEFT, fill = BOTH, expand = TRUE)

'''
for index,elements in zip([x for x in range(100)],[x for x in range(100)]):
    l.insert(index, elements)
'''
for i in range(len(realtimehot.get_contents())):
    #Label(text = realtimehot.get_contents()[i], font = ('宋体',20,'underline italic'),bd = 2, relief = FLAT).pack()
    #Button(mainframe,text = i, font = ('宋体',20,'underline italic'),bd = 3, relief = RIDGE, cursor = 'hand2', bg = 'white').pack()
    l.insert(i,realtimehot.get_contents()[i])

for i in range(len(socialevent.get_contents())):
    #Label(text = realtimehot.get_contents()[i], font = ('宋体',20,'underline italic'),bd = 2, relief = FLAT).pack()
    #Button(mainframe,text = i, font = ('宋体',20,'underline italic'),bd = 3, relief = RIDGE, cursor = 'hand2', bg = 'white').pack()
    l2.insert(i,socialevent.get_contents()[i])


mainframe.mainloop()