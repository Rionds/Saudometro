#!/usr/bin/env python

import cgitb, cgi

cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()

peso = float(form.getvalue('peso'))
altura = float(form.getvalue('altura'))

print('Content-type:text/html\r\n\r\n')
print('<html>')

print('<head>')
print('<link rel="stylesheet" href="../estiloTela.css">')
print('<link href="healthcare.png" rel="icon">')
print('</head>')

print('<body>')

imc = peso / altura ** 2
agua = peso * 0.035

if imc < 16:
    risco = "Magreza grave"
elif imc < 17:
    risco = "Magreza moderada"
elif imc < 18.5:
    risco = "Magreza leve"
elif imc < 25:
    risco = "Saudável"
elif imc < 30:
    risco = "Sobrepeso"
elif imc < 35:
    risco = "Obesidade Grau I"
elif imc < 40:
    risco = "Obesidade Grau II (severa)"
else:
    risco = "Obesidade Grau III (mórbida)"

print('<div id="imcRes">')
print('Índice de Massa Corporal: %.1f' % imc)
print('<p>Água por dia necessária: %.1f' % agua)

if risco == "Saudável":
    print('<p>Você está saudável!</p>')
else:
    print('<p>Risco: %s' % risco)

print('<div>')

print('</body>')
print("</html>")
