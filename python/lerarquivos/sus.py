import os.path
suport = open('suport.txt', 'r')
for suportread in suport:
    if(os.path.isfile(suportread)):
        if(os.path.isfile(suportread)):
            arquivo = open(suportread, 'r')
            for linha in arquivo:
                print(linha)
            arquivo.close()
        else:
            definirname = input('escreva o nome do arquivo')
            creat = open(definirname, 'w')
            suportedit = open('suport.txt', 'w')
            suportedit.write(definirname)
            definirvalor = input('escreva oque tera no arquivo')
            print("O arquivo não existe")
            creat.write(definirvalor)
            creat.close()
            suportedit.close()
    else:
        print('erro')
suport.close()