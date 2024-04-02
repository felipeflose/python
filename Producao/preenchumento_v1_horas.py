import pyautogui
import time 
import holidays
import pandas as pd
import pyautogui
import time 


#lançamento das horas mensais

def periodo_lancamento():
    data = pd.read_csv('modelo_mes.csv',delimiter=';')
    data = data['dia'].head(1)
    return data


def periodo_prreenchimento():
    d = periodo_lancamento()
    for i in d:
        print(str(i)+'-')
        return str(i)
    
def acao_preenchimento(d):


## 1 periodo

    time.sleep(10)
    pyautogui.click(x = 1278, y = -261) #projeto padrao

    time.sleep(1)
    pyautogui.click( x = 302 , y = -613) 

    pyautogui.write(d)

    pyautogui.press(['tab'])
    time.sleep(2)
    pyautogui.write('09:00')
    time.sleep(2)
    pyautogui.press(['tab'])
    pyautogui.write('12:00')
    pyautogui.press(['tab'])
    time.sleep(2)
    pyautogui.press(['tab'])
    pyautogui.click(x = 653, y = -612)
    pyautogui.write('0')
    time.sleep(2)
    pyautogui.click(x = 1039, y = -290)

## 2 periodo
    
    time.sleep(10)
    pyautogui.click(x = 1278, y = -261) #projeto padrao

    time.sleep(1)
    pyautogui.click( x = 302 , y = -613) 

    pyautogui.write(d)

    pyautogui.press(['tab'])
    time.sleep(2)
    pyautogui.write('13:00')
    time.sleep(2)
    pyautogui.press(['tab'])
    pyautogui.write('18:00')
    pyautogui.press(['tab'])
    time.sleep(2)
    pyautogui.press(['tab'])
    pyautogui.click(x = 653, y = -612)
    pyautogui.write('0')
    time.sleep(2)
    pyautogui.click(x = 1039, y = -290)

                              
def lancamento():

    for d in periodo_lancamento():
        print(d)
        acao_preenchimento(d)

def main():
    lancamento()
main() 