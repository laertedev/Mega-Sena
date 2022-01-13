import random
import PySimpleGUI as sg

sg.theme('DarkGreen1')  # aqui você escolhe a cor do tema
layout = [
    [sg.Text('Mega-Sena', font=('bold', 16))],
    [sg.Text('Gere números aleatórios para jogar na Mega-Sena ', font=13)],
    [sg.Text('               Boa Sorte!!!         ', font=13)],
    [sg.Button('Gerar números'), sg.Button('Sair')],
    [sg.Text('Teve sorte e ganhou o prêmio? Doe uma parte para o desenvolvedor.')],
    [sg.Text('Pix: lopes.laerte@gmail.com')],
    [sg.Text('Desenvolvido por: Laerte Lopes')]

]

janela = sg.Window("Mega-Sena - Milerte v1.0", layout=layout, element_justification='center')


while True:  # criando eventos
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Sair':
        break
    if eventos == 'Gerar números':
        a = str(sorted(random.sample(range(1, 61), 6)))
        sg.popup(f'Os números gerados foram: {a} ')
