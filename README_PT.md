FACTS-CHALLENGE
Descrição
Considere um modelo de informação, onde um registro é representado por uma tupla. Uma tupla (ou lista) nesse contexto é chamado de fato.

Exemplo de um fato:

# ('entidade', 'atributo', 'valor', 'operação')
('joão', 'idade', 18, True)
Nessa representação, a entidade (E) joão tem o atributo (A) idade com o valor (V) 18.
O valor final (OP) True indica que o fato foi adicionado.

Exemplo de fatos no formato de tuplas, i.e. (E, A, V, OP):

facts = [
    ('gabriel', 'endereço', 'av rio branco, 109', True),
    ('joão', 'endereço', 'rua alice, 10', True),
    ('joão', 'endereço', 'rua bob, 88', True),
    ('joão', 'telefone', '234-5678', True),
    ('joão', 'telefone', '91234-5555', True),
    ('joão', 'telefone', '234-5678', False),
    ('gabriel', 'telefone', '98888-1111', True),
    ('gabriel', 'telefone', '56789-1010', True),
]
Como é comum em um modelo de entidades, os atributos de uma entidade podem ter cardinalidade 1 ou N (muitos).

Nesse esquema, o atributo 'telefone' tem cardinalidade one-to-many e 'endereço' tem cardinalidade one-to-one.

schema = [
    ('endereço', 'cardinality', 'one'),
    ('telefone', 'cardinality', 'many')
]
Nesse exemplo, os seguintes registros representam o histórico de endereços que 'joão' já possuiu:

[
    ('joão', 'endereço', 'rua alice, 10', True)
    ('joão', 'endereço', 'rua bob, 88', True),
]
E o fato considerado vigente (ou ativo) é o último registrado, i.e.:

('joão', 'endereço', 'rua bob, 88', True)

Para indicar a remoção (ou retração) de uma informação, o quarto elemento da tupla pode ser False para representar que a entidade não tem mais aquele valor associado àquele atributo.

Levando isso em consideração nesse exemplo, os seguintes registros representam o histórico de telefones que 'joão' já possuiu:

[
    ('joão', 'telefone', '234-5678', True),     # 1° num adicionado
    ('joão', 'telefone', '91234-5555', True),   # 2° num adicionado
    ('joão', 'telefone', '234-5678', False),    # 1° num removido
]
Levando em consideração que o atributo 'telefone' possui cardinalidade 'many' o primeiro número de telefone foi adicionado, logo depois um novo número foi adicionado e em seguida o primeiro número foi removido. Então a lista de fatos vigentes dos telefones de joão seria:

[
    ('joão', 'telefone', '91234-5555', True),
]
Instruções
O objetivo desse desafio é escrever uma função que retorne quais são os fatos vigentes sobre essas entidades. Ou seja, quais são as informações válidas no momento atual. A função deve receber facts (todos fatos registrados) e schema (o esquema de cardinalidade dos atributos) como argumentos.


O que se deve assumir:

A lista de fatos está ordenada do mais antigo para o mais recente.
Só vão existir essas duas cardinalidades one e many
Todas as tuplas possuirão a estrutura descrita anteriormente
facts tuples = (E, A, V, OP)
schema tuples = (E, A, V)
Entidade, atributo, valor e operação não possuem a sequência de caracteres "---" dentro dos mesmos.
Entradas
A entrada é constítuida de dois arquivos facts.txt e schema.txt, ambos em utf-8. O arquivo facts.txt é formado por várias linhas, cada linha do mesmo representa um fato no formato entidade---atributo---valor---operação utilizando "---" como separador. Já o arquivo schema.txt é formado por várias linhas, enquanto cada linha do mesmo representa um fato do esquema formado por atributo---cardinalidade---tipo de cardinalidade também utilizando "---" como separador.

Saída
A saída é constituída de um output no console. A saída deve estar formatada de forma que cada fato vigente esteja em uma linha. Cada fato deve estar disposto da seguinte forma entidade---atributo---valor---operação utilizando "---" como separador.

Exemplo
Exemplo de Entrada	Exemplo de Saída
facts.txt
gabriel---endereço---av rio branco, 109---True
joão---endereço---rua alice, 10---True
joão---endereço---rua bob, 88---True
joão---telefone---234-5678---True
joão---telefone---91234-5555---True
joão---telefone---234-5678---False
gabriel---telefone---98888-1111---True
gabriel---telefone---56789-1010---True

schema.txt
endereço---cardinality---one
telefone---cardinality---many	output
'gabriel---endereço---av rio branco, 109---True'
'joão---endereço---rua bob, 88---True'
'joão---telefone---91234-5555---True',
'gabriel---telefone---98888-1111---True'
'gabriel---telefone---56789-1010---True'