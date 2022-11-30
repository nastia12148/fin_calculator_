import decimal

import PySimpleGUI as sg
import re
from decimal import *


def is_right_size_value(value: Decimal):
    if value > 1000000000000:
        return False
    elif value * 100000000000 % 10 != 0:
        return False
    else:
        return True


def is_number_value(value: str):
    return re.match(r"[-]?\d", value)


def is_correct_number_value(value:str):
    return re.match(r"([+-]?\d+[.,]?\d*$)|([+-]?(([1-9])|([1-9]\d)|([1-9]\d\d))([ ]\d{3})*[.,]?\d*$)", value)


def clear_value(value: str):
    value = value.replace(' ', '')
    value = value.replace(',', '.')
    return value


def calculate_problem(values):
    str_problem = "Decimal("
    for i in range(0, 7):
        if i % 2 == 0:
            if not is_number_value(values[i]):
                return "Your input must contain only numbers and only 1 '.' or ',' symbol"
            elif not is_correct_number_value(values[i]):
                return "Incorrect amount or placement of spaces in " + str(i/2) + " value"
            elif not is_right_size_value(Decimal(clear_value(values[i]))):
                return "The modulus of the input " + str(i/2) + " value is very big or very small!"
            values[i] = clear_value(values[i])
            str_problem += "Decimal("+str(values[i])+")"
        elif i == 1:
            if values[i] == '/':
                if (values[i+2] == '/' and values[i+3] == '0') or eval("Decimal(Decimal(" + values[i+1] + ")" + values[i+2] + "Decimal(" + values[i+3] + "))") < 0.00000000005:
                    return "Divizion by zero!"
            str_problem += values[i] + "("
        elif i == 5:
            if values[i] == '/' and values[i+1] == '0':
                return "Divizion by zero!"
            str_problem += ")" + values[i]
        else:
            if values[i] == '/' and values[i+1] == '0':
                return "Divizion by zero!"
            str_problem += values[i]

    str_problem += ")"
    value = eval(str_problem)
    if value > 1000000000000:
        return "Result is mor than 10^12"

    return eval(str_problem)


def format_output(value):
    if re.match(r"[-]?\d.\d*", str(value)):
        return format(value.normalize(),  '^10,.10f').replace(',', ' ').rstrip('0').rstrip('.')
    else:
        return value


def round_of_result(values):
    if not re.match(r"[-]?\d.\d*",str(calculate_problem(values))):
        window.FindElement("-OUT2-").Update(calculate_problem(values))
    elif values[7]:
        window.FindElement("-OUT2-").Update(
            format(decimal.Decimal(calculate_problem(values)).quantize(decimal.Decimal('0'), rounding=ROUND_HALF_UP)))
    elif values[8]:
        window.FindElement("-OUT2-").Update(
            format(decimal.Decimal(calculate_problem(values)).quantize(decimal.Decimal('0'), rounding=ROUND_HALF_EVEN)))
    elif values[9]:
        window.FindElement("-OUT2-").Update(
            format(decimal.Decimal(calculate_problem(values)).quantize(decimal.Decimal('0'), rounding=ROUND_DOWN)))


layout = [
    [sg.Text("Marynichava Anastasiya Egorovna, 4th course, 4th group, 2022")],
    [
        sg.InputText(0,25,5),
        sg.InputOptionMenu(["+", "-", "*", "/"],default_value="+"),
        sg.Text('('),
        sg.InputText(0,25,5),
        sg.InputOptionMenu(["+", "-", "*", "/"],default_value="+"),
        sg.InputText(0,25,5),
        sg.Text(')'),
        sg.InputOptionMenu(["+", "-", "*", "/"],default_value="+"),
        sg.InputText(0,25,5),

        sg.Button("="),
        sg.Output(key="-OUT-", size=(80, 5)),
    ],
    [[sg.Text("Round")],
    [sg.Radio("Math", "RADI01", default=True)],
    [sg.Radio("Half-even", "RADI01", default=False)],
    [sg.Radio("Down", "RADI01", default=False)],], [sg.Text("Round result"),
     sg.Output(key = "-OUT2-", size= (30,5))],
    ]
window = sg.Window("Financial calculator", layout).finalize()

while True:
    event, values = window.read(timeout=0)

    if event in (None, "Exit"):
        break
    if event == "=":

        window.FindElement("-OUT-").Update((format_output(calculate_problem(values))))
    if values[7] or values[8] or values[9]:
        round_of_result(values)

    else:
        a = 0

