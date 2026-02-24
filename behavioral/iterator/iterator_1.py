'''
Iterator é um padrão comportamental que tem a intenção
de fornecer um meio de acessar, sequencialmente, os 
elementos de um objeto agregado sem expor sua 
representação subjacente.

- Uma coleção deve fornecer um meio de acessar seus 
elementos sem expor sua estrutura interna
- Uma coleção poe ter maneiras e percursos diferentes
para expor seus elementos
- Você deve separar a complexidade dos algoritimos de 
iteração da coleção em si

A ideia principal do padrão é retirar a responsabilidade
de acesso e percurso de uma coleção, delegando tais tarefas
para um objeto iterador.
'''
#######################################################

from collections.abc import Iterator, Iterable

class MyIterator(Iterator):
    ...

if __name__ == '__main__':
    iterator = MyIterator() #error