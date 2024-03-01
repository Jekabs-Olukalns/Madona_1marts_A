import PySimpleGUI as sg 

sadalas=[
    [sg.Text('.')],
    [sg.Button('Aizvērt logu')],
    [sg.InputText(key='-VARDS-')],
    [sg.Button('Submit')],
    [sg.Text('', key='-DATI-')]
]

logs=sg.Window('Mans logs', sadalas)

while True:
    event, values=logs.read()

    if event ==sg.WIN_CLOSED or event =='Aizvērt logu' :
        sg.popup('Ir uzklikšķināts !')
        break 
    elif event == 'Submit':
        aka=values['-VARDS-']
    logs['-DATI-'].update(f"Sveiki, {aka}!")
logs.close()    