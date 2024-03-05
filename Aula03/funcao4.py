def escrever_tabuada(valor):
  """Escreve a tabuada de um determinado valor em um arquivo de texto."""
 
  with open("tabuada.txt", "w") as arquivo:
    for i in range(1, 11):
      arquivo.write(f"{valor} x {i} = {valor * i}\n")
 
 
if __name__ == "__main__":
  valor = int(input("Digite um valor: "))
  escrever_tabuada(valor)