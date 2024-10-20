porta = 'a'
janela = 'f'

alarme = (porta == 'a') or (janela == 'a')
msg = 'Alarme disparado? ' + str(alarme)
print(msg)

alarme = (porta == 'f') and (janela == 'f')
msg = 'Alarme disparado? ' + str(alarme)
print(msg)
print(not alarme)