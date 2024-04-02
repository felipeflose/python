import pyautogui
import time 
import holidays
import pandas as pd
import pyautogui
import time 


#lançamento das horas extras

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


    #pyautogui.keyDown('alt')
    #pyautogui.press(['tab'])
    #pyautogui.keyUp('alt')
    #pyautogui.press(['tab'])

    time.sleep(10)
    pyautogui.click( x = 1276, y = -236) 

    time.sleep(1)
    pyautogui.click( x = 302 , y = -613) 

    pyautogui.write(d)

    pyautogui.press(['tab'])
    time.sleep(2)
    pyautogui.write('18:00')

    
    time.sleep(2)
    pyautogui.press(['tab'])
    pyautogui.write('20:00')
    pyautogui.press(['tab'])
    time.sleep(2)
    pyautogui.press(['tab'])

    pyautogui.click(x = 653, y = -612)
    pyautogui.write('0')
    time.sleep(2)
    pyautogui.click(x = 1039, y = -290)
    time.sleep(1)
    pyautogui.click(x = 346, y = -497)
    pyautogui.write('Atividades Leega')
    pyautogui.click(x = 1039, y = -290)
    time.sleep(1)
    pyautogui.click( x = 1269, y = -221)
    time.sleep(1)
    pyautogui.click( x = 1269, y = -224)


    
                                            


   
 
def lancamento():

    for d in periodo_lancamento():
        print(d)
        acao_preenchimento(d)

def main():
    lancamento()
main() 