from operator import le
import tkinter as tk
import numpy as np 
from tkinter import E, W, N, S

calculator = tk.Tk()
calculator.title(string='Python Calculator')
# calculator.iconbitmap('E:\python\Icon\calc.ico')


# create a list

calc_keys = [
    {
        'text':'c',
        'command': lambda:insert_number_in_calc_result('c')
    },
    {
        'text':'^',
        'command': lambda:insert_number_in_calc_result('**')
    },
    {
        'text':'%',
        'command': lambda:insert_number_in_calc_result('%')
    },
    {
        'text':'/',
        'command': lambda:insert_number_in_calc_result('/')
    },
    {
        'text':'7',
        'command': lambda:insert_number_in_calc_result('7')
    },    
    {
        'text':'8',
        'command': lambda:insert_number_in_calc_result('8')
    },    
    {
        'text':'9',
        'command': lambda:insert_number_in_calc_result('9')
    },
    {
        'text':'+',
        'command': lambda:insert_number_in_calc_result('+')
    }, 
    {
        'text':'4',
        'command': lambda:insert_number_in_calc_result('4')
    },    
    {
        'text':'5',
        'command': lambda:insert_number_in_calc_result('5')
    },    
    {
        'text':'6',
        'command': lambda:insert_number_in_calc_result('6')
    },
    {
        'text':'-',
        'command': lambda:insert_number_in_calc_result('-')
    }, 
    {
        'text':'1',
        'command': lambda:insert_number_in_calc_result('1')
    },    
    {
        'text':'2',
        'command': lambda:insert_number_in_calc_result('2')
    },    
    {
        'text':'3',
        'command': lambda:insert_number_in_calc_result('3')
    },
    {
        'text':'*',
        'command': lambda:insert_number_in_calc_result('*')
    },
    {
        'text':'<',
        'command': lambda:insert_number_in_calc_result('<')
    },
    {
        'text':'0',
        'command': lambda:insert_number_in_calc_result('0')
    },  
    {
        'text':'.',
        'command': lambda:insert_number_in_calc_result('.')
    }, 
    {
        'text':'=',
        'command': lambda:insert_number_in_calc_result('=')
    }, 

]
result_label = tk.Label(
    master= calculator,
    text= '0',
    width=30,
    height=3,
    font=('Times', 14) 
)
# Check user input
def detect_decimal(current):
    for charecter in current[::-1]:
        if charecter  == '.':
            return True
        if charecter in ['+', '-', '*', '^', '/', '%']:
            return False
    return False

# last_op_index = -1
# last_dot_index = -1
def insert_number_in_calc_result(btn_text):
    current = result_label['text']
    # global last_op_index, last_dot_index
    if btn_text in ['+', '-', '*']:
        last_op_index = len(current)

    # print(last_op_index, last_dot_index)
    if btn_text == 'c':
        result_label['text'] = '0'
        # last_op_index , last_dot_index = 0, 0

    elif current == '0':
        result_label['text'] = btn_text

    elif btn_text == '=':
        result_label['text'] = f'{eval(current)}'
    elif btn_text == None:
        result = f'{eval(current)}'
        result_label['text'] = result
        # last_op_index = 0
        # if '.' in result:
            # last_dot_index = len(current) - 2
            # last_dot_index = result.index('.')

    elif btn_text =='.': #and (not (last_dot_index > last_op_index or current[-1])):
            if not detect_decimal(current):
                result_label['text'] += btn_text
            # last_dot_index = len(current)

    elif btn_text == '<':
        if result_label['text'] != '0':
            result_label['text'] = current[:-1]
        else:
            pass
    else:
        if btn_text in ['+', '-', '*'] and current[-1] in ['+', '-', '*']:
            result_label['text'] = current[:-1] + btn_text
        else:
            result_label['text'] += btn_text
    



calc_keys_objs = []

for calc_keys_data in calc_keys:
    if calc_keys_data['text'] not in ['c','=']:
        btn = tk.Button(
            master= calculator,
            text = calc_keys_data['text'], 
            command = calc_keys_data['command'],
            width=2,
            height=3,
            fg='white',
            border=2,
            font=('Times', 13, 'bold'),
            background="black",
            
        )
    else:
        if calc_keys_data['text'] == 'c':
            btn = tk.Button(
            master= calculator,
            text = calc_keys_data['text'], 
            command = calc_keys_data['command'],
            width=2,
            height=3,
            fg='red',
            border=2,
            font=('Times', 15, 'bold'),
            background='darkgrey',
            
            )
        elif calc_keys_data['text'] == '=':
            btn = tk.Button(
            master= calculator,
            text = calc_keys_data['text'], 
            command = calc_keys_data['command'],
            width=2,
            height=3,
            fg='black',
            border=2,
            font=('Times', 15, 'bold'),
            background='royalblue',
            
            )

    calc_keys_objs.append(btn)
print(type(calc_keys_objs))
# 0 , 1, 2, 3 // 4 = 0

for i, calc_keys_obj in enumerate(calc_keys_objs):
    calc_keys_obj.grid(row = i // 4 + 1 , column = i % 4, sticky = (N, S, W, E))



result_label.grid(row=0, column=0, columnspan=4,sticky=(E, W))

calculator.mainloop()