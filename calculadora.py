Valor_produto = flot(input("Digite o valor do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto: "))
if persentual_desconto < 0 or percentual_desconto > 100:
  print("Desconto invalido! Digite um valor entre 0 e 100,")
else:
  valor_desconto = valor_produto * percentual_desconto / 100
  valor_final = valor_produto - valor_desconto
  print("Valor do desconto: R$", valor_desconto)
  print("Valor do produto: R$", valor_final)
