import pyautogui
import time

print("Contesta las siguientes preguntas, no usaremos tus datos de mala manera ;)")
q1 = input("Marvel o DC: ")
q2 = input("Escribe un refrán, catchphrase, dicho popular o cita de libro o película: ")
#q3 = input("Cuál es la mejor hora del día para comer pastel: ")
#q4 = input("Ingresa una dirección de correo electrónico falsa: ")


def firstForm():
    if q1 == "Marvel":
        pyautogui.click(x = 529, y = 593, clicks = 1)
    
    elif q1 == "DC":
        pyautogui.click(x = 529, y = 646, clicks = 1)

    elif q1 == "Ambos":
        pyautogui.click(x = 529, y = 695, clicks = 1)

    elif q1 == "Ninguno" or "":
        pyautogui.click(x = 529, y = 745, clicks = 1)

    pyautogui.press('tab')
    pyautogui.press('tab')

    pyautogui.typewrite(q2)

if __name__ == "__main__":
    firstForm()
