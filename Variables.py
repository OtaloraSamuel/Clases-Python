import yfinance
ticker=input("Digita el código de la acción: ")
data=yfinance.Ticker(ticker).history("6mo")
cierre=data.Close
#cierre.plot()
maxima=round(cierre.max(),2)
minima=round(cierre.min(),2)
valor_medio=round(cierre.mean(),2)

import pyautogui
import pyperclip
import webbrowser
import time

destinatario="erick.chiguano2020@gmail.com"
asunto="Análisis acciones últimos 6 meses"
mensaje=f"""
Hola erick,

Acá te envío el análisis de las acciones de los últimos 6 meses de {ticker}:

Cotización máxima: USD {maxima}
Cotización minima: USD {minima}
Valor medio: USD {valor_medio}

Hablamos!

Samuel,
"""

webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

time.sleep(3)



pyautogui.click(78,170)
time.sleep(1)
pyperclip.copy(destinatario)
time.sleep(1)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

pyperclip.copy(asunto)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

pyperclip.copy(mensaje)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("ctrl","enter")
time.sleep(2)
pyautogui.hotkey("ctrl","f4")
