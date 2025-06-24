import pyautogui

pyautogui.hotkey('Win', 'r') #hotkey é um comando que utilizamos para combinar teclas 
pyautogui.sleep(1) #sleep é um comando que utilizamos para deixar o codigo em espera por alguns segundos
pyautogui.write("calc") #write é um comando que utilizamos para o que queremos escrever
pyautogui.press('enter') #teclado pressiona enter
pyautogui.sleep(2) #pausa curta
pyautogui.press('8') #teclado pressiona 8 
pyautogui.sleep(2) #pausa curta
pyautogui.press('+') #teclado pressiona + 
pyautogui.sleep(2) #pausa curta
pyautogui.press('2') #teclado pressiona 2
pyautogui.press('=') #tecladp pressiona = 

print("O cálculo de 8 + 2 foi realizado na calculadora do Winwos")
print("Confira o histórico na calculadora")