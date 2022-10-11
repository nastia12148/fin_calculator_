from unicodedata import decimal

import PySimpleGUI as sg
import re
from decimal import *

layout = [
    [sg.Text("Marynichava Anastasiya Egorovna, 4th course, 4th group, 2022")],
    [
        sg.InputText(),
        sg.InputOptionMenu(["+", "-"]),
        sg.InputText(),
        sg.Button("="),
        sg.Output(key="-OUT-"),
    ],
    ]
window = sg.Window("File Compare", layout).finalize()
while True:  # The Event Loop
    event, values = window.read(timeout=0)

    if event in (None, "Exit"):
        break
    if event == "=":
        if not values[0] or not values[2]:
            window.FindElement("-OUT-").Update("You need to input values")

        elif not re.match(r"([+-]?[0-9]+[.,]?[0-9]*$)", values[0]) or not re.match(
            r"([+-]?[0-9]+[.,]?[0-9]*$)", values[2]
        ):
            window.FindElement("-OUT-").Update("Wrong input values")

        elif abs(Decimal(values[0])) > 1000000000000 or abs(Decimal(values[2])) > 1000000000000:
            window.FindElement("-OUT-").Update("Input value is very big!")

        else:
            if values[1] == "+":
                window.FindElement("-OUT-").Update(Decimal(Decimal(values[0]) + Decimal(values[2])))

            elif values[1] == "-":
                window.FindElement("-OUT-").Update(Decimal(Decimal(values[0]) - Decimal(values[2])))

            else:
                window.FindElement("-OUT-").Update("You need to choose the operation")
