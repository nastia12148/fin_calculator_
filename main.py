import PySimpleGUI as sg
import re
from decimal import *

layout = [
    [sg.Text("Marynichava Anastasiya Egorovna, 4th course, 4th group, 2022")],
    [
        sg.InputText(),
        sg.InputOptionMenu(["+", "-", "*", "/"]),
        sg.InputText(),
        sg.Button("="),
        sg.Output(key="-OUT-", size=(80, 5)),
    ],
    ]
window = sg.Window("Financial calculator", layout).finalize()

while True:
    event, values = window.read(timeout=0)

    if event in (None, "Exit"):
        break
    if event == "=":
        values[0] = values[0].replace(",", ".")
        values[2] = values[2].replace(",", ".")
        if not values[0] or not values[2]:
            window.FindElement("-OUT-").Update("You need to input values")

        elif not re.match(r"([+-]?[0-9]+[.,]?[0-9]*$)", values[0]) or not re.match(
            r"([+-]?[0-9]+[.,]?[0-9]*$)", values[2]
        ):
            window.FindElement("-OUT-").Update("Wrong input values")

        elif abs(Decimal(values[0])) > 1000000000000 or abs(Decimal(values[2])) > 1000000000000:
            window.FindElement("-OUT-").Update("The modulus of the input value is very big!")

        elif abs(Decimal(values[0])) < 0.000001 or abs(Decimal(values[2])) < 0.000001:
            window.FindElement("-OUT-").Update("The modulus of the input value is very small!")
        else:
            if values[1] == "+":
                if abs(Decimal(values[0]) + Decimal(values[2])) <= 1000000000000:
                    window.FindElement("-OUT-").Update(Decimal(Decimal(values[0]) + Decimal(values[2])).normalize())
                else:
                    window.FindElement("-OUT-").Update("The modulus of the sum more than 1 000 000 000 000!")

            elif values[1] == "-":
                if abs(Decimal(values[0]) - Decimal(values[2])) <= 1000000000000:
                    window.FindElement("-OUT-").Update(Decimal(Decimal(values[0]) - Decimal(values[2])).normalize())
                else:
                    window.FindElement("-OUT-").Update("The modulus of the difference more than 1 000 000 000 000!")

            elif values[1] == "*":
                if abs(Decimal(values[0]) * Decimal(values[2])) <= 1000000000000:
                    window.FindElement("-OUT-").Update(Decimal(Decimal(values[0]) * Decimal(values[2])).normalize())
                else:
                    window.FindElement("-OUT-").Update("The modulus of the multiplication more than 1 000 000 000 000!")

            elif values[1] == "/":
                if values[2] == 0:
                    window.FindElement("-OUT-").Update("Division by zero error!")
                if abs(Decimal(values[0]) * Decimal(values[2])) <= 1000000000000:
                    window.FindElement("-OUT-").\
                        Update(Decimal(Decimal(values[0]) / Decimal(values[2])).quantize(Decimal("0.000001")).normalize())
                else:
                    window.FindElement("-OUT-").Update("The modulus of the division more than 1 000 000 000 000!")

            else:
                window.FindElement("-OUT-").Update("You need to choose the operation")
