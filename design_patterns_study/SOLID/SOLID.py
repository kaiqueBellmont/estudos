"""
Os princípios SOLID são:
O Princípio de Responsabilidade Única (SRP)
O princípio aberto-fechado (OCP)
O Princípio de Substituição de Liskov (LSP)
O Princípio de Segregação de Interface (ISP)
O princípio de inversão de dependência (DIP)


Esses cinco princípios não são uma lista ordenada específica (fazer isso, depois aquilo etc.),
mas uma coleção de melhores práticas, desenvolvidas ao longo das décadas. Estão reunidos em uma sigla,
como um veículo mnemônico a ser lembrado, semelhante a outros na informática, por exemplo: SECO: Não se Repita; KISS: Mantenha-o pequeno e simples;
como peças de sabedoria acumulada. Uma pequena observação: a sigla foi criada anos depois que esses cinco princípios foram definidos juntos.


Em geral, os princípios SOLID são etapas básicas de aprendizado para
todo desenvolvedor de código, mas geralmente são
ignorados por aqueles que não consideram a mais alta qualidade do
código sua prioridade absoluta.

No entanto, como cientista de dados, vi que seguir esses princípios é benéfico.
Especificamente, melhora a testabilidade, reduz dívidas técnicas e o tempo necessário para implementar
mudanças quando surgem novos requisitos de clientes / acionistas.

No artigo a seguir, quero explorar esses cinco princípios e oferecer alguns exemplos em Python.
Normalmente, os princípios SOLID são aplicados no contexto de design orientado a objetos (ou seja: classes de Python),
mas acredito que eles são válidos independentemente do nível, e gostaria de manter o exemplo e a
explicação aqui, em um nível para um “Iniciante avançado”, supervisionando a definição formal.
"""