import PySimpleGUI as sg 

def read_file(filename): 
    try:
        with open (filename):

except Exception as e:

def main():
    layout=[
        [sg.Text("Ievadiet txt  nosaukumu :")],
        [sg.InputText(key='filenename'), sg.FileBrowse()],
        [sg.Button('Nolasit datni'), sg.Button('Iziet')],
        [sg.]
    ]

while true:

if __name__=="__main__":
    main()
 