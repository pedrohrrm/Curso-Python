preco = float(input('Digite o valor do produto em R$: '))
desconto = int(input('Digite o percentual de desconto que será aplicado: '))
valor_desconto = preco * (desconto/100)
valor_final = preco - valor_desconto
print(f'Aplicando um desconto de {desconto} o produto terá seu preco final de R${valor_final}, tendo um desconto de R${valor_desconto}')