import requests

url_base = 'https://proverbia.net/frase-del-dia'

def getFrase():
    text = requests.get(url_base) #Respuesta
    rawText = text.content.decode() #Contenido en bruto

    posFrase = rawText.find('class="bsquote"')
    iniFrase = rawText.find('<p>', posFrase)
    finFrase = rawText.find('</p', posFrase)
    frase = rawText[iniFrase+3:finFrase]

    posAutor = rawText.find('<a title=', finFrase)
    iniAutor = rawText.find('>', posAutor)
    finAutor = rawText.find('</a>', iniAutor)
    autor = rawText[iniAutor+2:finAutor]

    return frase, autor

proverbia = getFrase()
print(proverbia[0])
print(proverbia[1])