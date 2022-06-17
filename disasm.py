#!/usr/bin/python3

import sys

def main(argv):
    if (len(argv) == 0):
        print('Error: inform a filename to disassemble.')
        exit()
     
    # Nome do arquivo binário de entrada
    filename = argv[0]
    
    # Opção 'rb' abre o arquivo para leitura em formato binário
    with open(filename, 'rb') as binfile:
        #
        # Seu código começa aqui!
        # 
        # Utilize a variável "binfile" para ler os bytes do arquivo
        #
        dadosDaMarrie = [
        "jns", "load", "store", "add", "subt", 
        "input", "output", "halt", "skipcond", "jump", 
        "clear", "addi", "jumpi", "loadi", "storei"
        ]

        data = binfile.read()

        value = ''

        while data != b'':
            value += "".join(f"{c:02x}" for c in data)
            data = binfile.read(1)
        
        valueArray = ''
        
        for i, v in enumerate(value):
            if i % 4 == 0 and i > 0:
                valueArray += ' '

            valueArray += v

        valueArray = valueArray.split(' ')

        for i in range(0, len(valueArray)):
            n = str(valueArray[i])

            op = dadosDaMarrie[int(n[0], 16)]
            print(f'{op}') if op in ('input', 'output', 'halt', 'clear') else print(f'{op} {int(n[1:])}')

# -------------------------------------
# Trecho a seguir obrigatório para receber os parâmetros via linha de comando.
# NÃO APAGAR!!

if __name__ == "__main__":
    main(sys.argv[1:])