

aprovados = ['Rafaela', 'Pedro', 'Renato' , 'Maria']
for nome in aprovados:
    print(nome)


for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)


dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sabado')
for dia in dias_semana:
    print(f'Hoje e {dia}')


for letra in set('Muito legal'):
    print(letra)
