# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:50:26 2020

@author: Tim
"""


import tkinter as tk
import numpy as np
import scipy.stats

def hit_me():
    v1g = var1.get()
    v2g = var2.get()
    v3g = var3.get()
    v4g = var4.get()
    vag = v1g + v2g + v3g + v4g
    obs = np.array([[v1g,v2g], [v3g,v4g]])
    
    chi_ans = scipy.stats.chi2_contingency(obs, correction = False)
    fisher_ans = scipy.stats.fisher_exact(obs, alternative = 'two-sided')
    
    if fisher_ans[1] < 0.05:
        fisher_a = ('兩者有關聯性')
    else:
        fisher_a = ('兩者無關聯性')
        
    if vag < 20:
        a = ('因為樣本數小於20，建議參考費雪檢定')
    elif chi_ans[3][0][0] < 5 or chi_ans[3][0][1] < 5 or chi_ans[3][1][0] < 5 or chi_ans[3][1][1] < 5:
        a = ('因為某細格期望值小於5，建議參考費雪檢定')
    else:
        a = ('建議參考卡方檢定')
    
    if chi_ans[2] == 1: 
        chi_ans = scipy.stats.chi2_contingency(obs, correction = True)       
        
        if chi_ans[1] < 0.05:
            chi_a = ('兩者有關聯性')
        else:
            chi_a = ('兩者無關聯性')
            
        oupt = ('........透過卡方檢定........' +
                '\n\n＊自由度：' + str(chi_ans[2]) +
                '\n＊p-value:' + str(chi_ans[1]) +
                '\n＊關聯性：' + str(chi_a) + 
                '\n\n........透過費雪檢定........' +
                '\n\n＊p-value:' + str(fisher_ans[1]) +
                '\n＊關聯性：' + str(fisher_a) + 
                '\n\n............................')
        oupt2 = ('＊' + str(a))       
        var_1.set(oupt)
        var_2.set(oupt2)
       
    else:
        
        if chi_ans[1] < 0.05:
            chi_a = ('兩者有關聯性')
        else:
            chi_a = ('兩者無關聯性')
            
        oupt = ('........透過卡方檢定........' +
                '\n\n＊自由度：' + str(chi_ans[2]) +
                '\n＊p-value:' + str(chi_ans[1]) +
                '\n＊關聯性：' + str(chi_a) + 
                '\n\n........透過費雪檢定........' +
                '\n\n＊p-value:' + str(fisher_ans[1]) +
                '\n＊關聯性：' + str(fisher_a) + 
                '\n\n............................')
        oupt2 = ('＊' + str(a))
        var_1.set(oupt)
        var_2.set(oupt2)
    

window = tk.Tk()
window.title('卡方＆費雪檢定')
window.geometry('600x450')
var_1 = tk.StringVar()
var_2 = tk.StringVar()

l1 = tk.Label(window,
              text = '卡方＆費雪檢定',
              font = ('標楷體', 16),
              height = 2).place(x = 220, y = 1)
l2 = tk.Label(window, 
              textvariable = var_1, 
              font = ('標楷體', 12), 
              justify = 'left',
              anchor = 'w').place(x = 180, y = 200)
l3 = tk.Label(window, 
              textvariable = var_2, 
              font = ('標楷體', 12),
              fg = 'red',
              justify = 'left',
              anchor = 'w').place(x = 180, y = 410)

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
e1 = tk.Entry(window, textvariable = var1).place(x = 230, y = 55, width = 50, height = 25)
e2 = tk.Entry(window, textvariable = var2).place(x = 320, y = 55, width = 50, height = 25)
e3 = tk.Entry(window, textvariable = var3).place(x = 230, y = 105, width = 50, height = 25)
e4 = tk.Entry(window, textvariable = var4).place(x = 320, y = 105, width = 50, height = 25)

b = tk.Button(window,
              text = '開始分析',
              font = ('標楷體', 14),
              command = hit_me).place(x = 250, y = 150)

window.mainloop()
