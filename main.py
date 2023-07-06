import pywhatkit as pyw

numTel = "+573122055470"
mensaje = "Mensaje automatizado"
hora = 17
minutos = 10

pyw.sendwhatmsg(numTel, mensaje, hora, minutos, 7, True, 15)
