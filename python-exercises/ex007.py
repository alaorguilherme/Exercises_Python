alune = input('Professore, poderia me dizer o nome de alune: ')
nota = float(input('Qual a nota de matemática de {}: '.format(alune)))
nota2 = float(input('e a nota de física: '))
m = ((nota+nota2)/2)
s = (nota+nota2)
print('Muito bom, professore, a soma das notas de {} é {}, já sua média é igual a {:.2}'.format(alune, s, m))