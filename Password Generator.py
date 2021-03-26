import random
from tkinter import *
from tkinter import messagebox
import os

#config janela do APP
mainWindow = Tk()
mainWindow.geometry('220x180')
mainWindow.title('Gerador de senhas aleatórias')
mainWindow.eval('tk::PlaceWindow . center')

chars = 'abcdefghijklmnopqrstuvwxyz'
specialChars = '!@#$%&*.'
nums = '1234567890'
useSpecial = BooleanVar()
useNums = BooleanVar()
#passwordLenght = 10
defaultValue = False
passLenght = IntVar()
passQuantity = IntVar()

def password_gen(password_lenght, password_quantity, use_special, use_nums):
    passwordList = []

    if use_special == True and use_nums == True:
        using_chars = (chars + specialChars + nums).strip()
    elif use_special == True and use_nums == False:
        using_chars = (chars + specialChars).strip()
    elif use_special == False and use_nums == True:
        using_chars = (chars + nums.strip())
    else:
        using_chars = chars.strip()

    while len(passwordList) < password_quantity:
        password = ''
        for x in range(0, password_lenght):
            randenum = random.randint(0, len(using_chars)-1)
            password += (using_chars[randenum])
        passwordList.append(password)

    passwordFile = open((os.path.expanduser("~/Desktop/passwords.txt")), "w")
    for passwords in range(0, len(passwordList)):
        passwordFile.write('{}\n'.format(passwordList[passwords]))
    passwordFile.close()
    return passwordList

def showinfo():
    messagebox.showinfo(title='Aviso', message='Processo finalizado.\nAs senhas estão salvas em sua área de trabalho!')


#config conteúdo da janela
title = Label(mainWindow, text='Gerador de senhas aleatórias !').grid(row=0, column=0, columnspan=2)
howManyChars = Entry(mainWindow, width=2, textvariable=passLenght).grid(row= 2, column =0, sticky=EW)
charsLabel = Label(mainWindow, text='Quantidade de caracteres').grid(row= 2, column=1, sticky=W)
howManyPasswords = Entry(mainWindow, width=2, textvariable=passQuantity).grid(row= 3, column = 0, sticky=EW)
HowManyPasswordsLabel = Label(mainWindow, text='Quantidade de senhas').grid(row= 3, column = 1, sticky=W)
passwordCheckSpecial = Checkbutton(mainWindow, text='Usar caracteres especiais (!@#$%&*.)', variable=useSpecial, onvalue=True, offvalue=False, command=print(useSpecial)).grid(row= 4, column = 0, sticky=W, columnspan=2)
passwordCheckNum = Checkbutton(mainWindow, text='Usar números', variable=useNums, onvalue=True, offvalue=False).grid(row= 5, column = 0, sticky=W, columnspan=2)
generateButton = Button(mainWindow, text='Gerar', command=lambda:[print(password_gen(passLenght.get(), passQuantity.get(), useSpecial.get(), useNums.get())), showinfo()]).grid(row= 6, column = 0, columnspan=2)

mainWindow.mainloop()
