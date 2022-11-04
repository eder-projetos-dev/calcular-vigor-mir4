import PySimpleGUI as sg
import datetime as dt

agora = dt.datetime.now();
agora = agora.strftime("%H:%M")

"""
Calcula o vigor atual
Retorna o horário de duração do vigor """

def vigorAtual():
    horas, minutos = valores["vigor_atual"].split(":")
    agora = dt.datetime.now();
    return agora + dt.timedelta(hours=int(horas), minutes=int(minutos));
    
"""
Recupera o vigor tomando pilulas de 1h ou 30 minutos
Retorna o horário que terminará o efeito das pilulas """

def aumentarVigor():        
    pilulas_1h = int(valores["pilulas_1h"])
    pilulas_30min = int(valores["pilulas_30min"]) * 30
    termina = vigorAtual() + dt.timedelta(hours=pilulas_1h, minutes=pilulas_30min);
    return termina.strftime("%H:%M")
  
layout = [    
    [sg.InputText(agora, key="hora_atual"), sg.Text("Horário Atual")],   
    [sg.InputText("00:00", key="vigor_atual"), sg.Text("Vigor Atual")],
    [sg.Text("Aumentar Vigor")],
    [sg.InputText(0, key="pilulas_1h"), sg.Text("Pilulas de 1h")],
    [sg.InputText(0, key="pilulas_30min"), sg.Text("Pilulas de 30 min")],
    [sg.Text("Expira em")],
    [sg.InputText("00:00", key="expira")],
    [sg.Button("Calcular"), sg.Button("Cancelar")],    
]

janela = sg.Window("Calcular Recuperação de Vigor - MIR4", layout)

while True:    
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break    
    if evento == "Calcular":
        agora = dt.datetime.now().strftime("%H:%M")
        janela["hora_atual"].update(agora) # atualizar horário atual                        
        janela["expira"].update(aumentarVigor()) # horário que terminará o vigor       

janela.close()
