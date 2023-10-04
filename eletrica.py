while True:
    pergunta = input("o que quer calcular? Digite 'r' para resistência; 'req' para resistência equivalente; 'v' para tensão; e 'a' para corrente: ")
    if pergunta == "r":
        v = float(input("qual a tensão aplicada no resitor em V?"))
        i = float(input("qual a corrente aplicada no resitor em mA?"))
        resultado = v/i
        print(f"a resistência do circuito é {resultado} KΩ")
    elif pergunta == "req":
        tipo = input("o circuito é em série ou em paralelo?")
        if tipo == "paralelo":
            paralelo = int(input("quantos divisões em paralelo?"))
            i = 0
            resistores_serie = []
            lista = []
            lista2 = []
        
            while i < paralelo:
                serie = int(input("quantos resistores em série na divisão?"))
                resistores_serie.append(serie)
                h = 1
                soma = 0
                while h <= serie:
                    resistor = float(input("qual o valor da resistencia do {h}ª resistor em KΩ?"))
                    soma += resistor
                    h += 1
                lista.append(soma)
                i += 1
            for x in lista:
                if x != 0:
                    lista2.append(x)
            resistencia = 0
            for x in lista2:
                resistencia += 1/x
                resistencia_final = resistencia ** (-1)
            print(f"a resistência equivalente é {resistencia_final}KΩ")
        elif tipo == "serie":
            resistores = int(input("quantos resistores tem no circuito?"))
            i = 1
            resistencia = []
            while resistores >= i:
                resistores2 = float(input(f"qual a resistência do {i}ª resistor em KΩ?"))
                resistencia.append(resistores2)
                i += 1
            print(f"a resistência equivalente no circuito é igual a {sum(resistencia)}KΩ")
    elif pergunta == "v":
        tipo = input("o circuito é em série ou em paralelo?")
        if tipo == "paralelo":
            paralelo = int(input("quantos divisões em paralelo?"))
            i = 0
            resistores_serie = []
            lista = []
            lista2 = []
        
            while i < paralelo:
                serie = int(input("quantos resistores em série na divisão?"))
                resistores_serie.append(serie)
                h = 1
                soma = 0
                while h <= serie:
                    resistor = float(input("qual o valor da resistencia do {h}ª resistor em KΩ?"))
                    soma += resistor
                    h += 1
                lista.append(soma)
                i += 1
            for x in lista:
                if x != 0:
                    lista2.append(x)
            resistencia = 0
            for x in lista2:
                resistencia += 1/x
                resistencia_final = resistencia ** (-1)
            corrente = float(input("qual a corrente do circuito em mA?"))
            v = corrente*resistencia_final
            print(f"a tensão nesse circuito é {v:.2f}V")
        elif tipo == "serie":
            resistores = int(input("quantos resistores tem no circuito?"))
            corrente = float(input("qual a corrente do circuito em mA?"))
            i = 1
            resistencia = []
            listatensoes = []
            while resistores >= i:
                resistores2 = float(input(f"qual a resistência do {i}ª resistor em KΩ?"))
                resistencia.append(resistores2)
                i += 1
            tensao_total = sum(resistencia)*corrente
            for r in resistencia:
                resultado = r*corrente
                listatensoes.append(resultado)
            f = 0
            h = 1
            while f < len(listatensoes):
                print(f"tensão no {h}ª resistor é igual a {listatensoes[f]}V")
                h += 1
                f += 1
            print(f"a tensão total do circiuto é de {tensao_total}V")
    elif pergunta == "a":
        tipo = input("o circuito é em série ou em paralelo?")
        if tipo == "paralelo":
            paralelo = int(input("quantos divisões em paralelo?"))
            i = 0
            resistores_serie = []
            lista = []
            lista2 = []
        
            while i < paralelo:
                serie = int(input("quantos resistores em série na divisão?"))
                resistores_serie.append(serie)
                h = 1
                soma = 0
                while h < serie:
                    resistor = float(input("qual o valor da resistencia do {h}ª resistor em KΩ?"))
                    soma += resistor
                    h += 1
                lista.append(soma)
                i += 1
            for x in lista:
                if x != 0:
                    lista2.append(x)
            resistencia = 0
            for x in lista2:
                resistencia += 1/x
                resistencia_final = resistencia ** (-1)
            tensao = float(input("qual a tensão do circuito em V?"))
            a = tensao/resistencia_final
            f = 0
            h = 1
            while f < len(lista2):
                print(f"corrente no {h}ª divisão é igual a {tensao/lista2[f]}mA")
                h += 1
                f += 1
            print(f"a corrente nesse circuito é {a:.2f}mA")
        if tipo == "serie":
            resistores = int(input("quantos resistores tem no circuito?"))
            tensao = float(input("qual a tensão do circuito em V?"))
            resistor = []
            g = 1
            while g <= resistores:
                resistencias = float(input(f"qual a resistência do {g}ª resistor em KΩ?"))
                resistor.append(resistencias)
                g += 1
            resistencia_total = sum(resistor)
            a = tensao/resistencia_total
            print(f"a corrente no circuito é {a}mA")