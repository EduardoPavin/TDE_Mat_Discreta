# Alunos: Daniela Tamy Yuki e Eduardo Augusto C. d'O. Pavin

import ast
import sys

# Função de cálculo do produto cartesiano
def produto_cartesiano(conjunto1, conjunto2):
    resultado = {(x, y) for x in conjunto1 for y in conjunto2}
    return resultado

# Solicitar ao usuário o nome do arquivo de entrada
nome_arquivo = input("Digite o nome do arquivo de entrada (conjuntos.txt / conjuntos2.txt / conjuntos3.txt / conjuntos4.txt ): ")

try:
    with open(nome_arquivo) as file:
        for line in file:
            line = line.strip() # Remover espaços em branco no início e no final da linha

            if len(line) >= 1:
                operacao = line[0]

                # Ler a próxima linha
                conjunto1_line = next(file).split()
                conjunto2_line = next(file).split()

                # Converter as linhas em conjuntos usando set()
                conjunto1 = set(conjunto1_line)
                conjunto2 = set(conjunto2_line)

                # Verificar a operação e calcular o resultado apropriado
                if operacao == "U":
                    resultado = conjunto1.union(conjunto2)
                elif operacao == "I":
                    resultado = conjunto1.intersection(conjunto2)
                elif operacao == "D":
                    resultado = conjunto1.difference(conjunto2)
                elif operacao == "C":
                    resultado = produto_cartesiano(conjunto1, conjunto2)
                else:
                    resultado = None
                    print("Operação inválida")

                if resultado is not None:
                    print("Operação:", operacao, "conjunto 1:", conjunto1_line, "conjunto 2:", conjunto2_line, "resultado:", resultado)

except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
except Exception as e:
    sys.exit()  # Encerrar
