from asyncio import events
from PySimpleGUI import PySimpleGUI as sg

print("Faça o cadastro")


sg.theme('Reddit')
layout = [
    [sg.Text('Insira nome de usuario'), sg.Input(
        key='insira nome de usuario')],
    [sg.Text('insira uma senha'), sg.Input(
        key='insira una senha', password_char='*')],
    [sg.Checkbox('Login está correto')],
    [sg.Button('Criar conta')]

]

janela = sg.Window('Criar conta', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Criar conta':
        if valores['Insira seu nome de usuario:'] == 'Insira nome de usuario' and valores['senha'] == 'insira a senha':
            print('Bem vindo ao curso de Python, faça login para continuar!')

sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]

]

janela = sg.Window('Tela de Login', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'andre' and valores['senha'] == '123':
            print('Bem vindo ao curso de Python!')
