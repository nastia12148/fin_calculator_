import PySimpleGUI as sg
import re
import hashlib

layout = [
    [sg.InputText(), sg.InputOptionMenu(['+', '-']), sg.InputText(), sg.Button('='), sg.Output(key='-OUT-', size=(80,20))
     ],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('File Compare', layout).finalize()
while True:  # The Event Loop
    event, values = window.read(timeout=0)

    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == '=':
        if not values[0] or not values[2]:
            window.FindElement('-OUT-').Update('You need to input values')
        elif not re.match(r'([+-]?[0-9]+[.,]?[0-9]*$)', values[0]) or not re.match(r'([+-]?[0-9]+[.,]?[0-9]*$)', values[2]):
            window.FindElement('-OUT-').Update('Wrong input values')
        elif abs(float(values[0])) > 1000000000 or abs(float(values[2])) > 1000000000:
            window.FindElement('-OUT-').Update('Input value is very big!')
        else:
            if values[1] == '+':
                window.FindElement('-OUT-').Update(float(values[0]) + float(values[2]))
            elif values[1] == '-':
                window.FindElement('-OUT-').Update(float(values[0]) - float(values[2]))
            else:
                window.FindElement('-OUT-').Update('You need to choose the operation')

