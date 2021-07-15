# 3) O princípio de substituição de Liskov (LSP)

"""
“Funções que usam ponteiros ou referências para classes base devem ser capazes de usar objetos de classes derivadas sem saber”
"""
# Alternativamente, isso pode ser expresso como “ As classes derivadas devem ser substituíveis por suas classes base ”.

"""Em (talvez) palavras mais simples, se uma subclasse redefine uma função também presente na classe pai, 
um usuário-cliente não deve estar notando nenhuma diferença no comportamento e é um substituto para a classe base. 
Por exemplo, se você estiver usando uma função e seu colega alterar a classe base, você não deve notar nenhuma 
diferença na função que está usando.
 
 Dentre todos os princípios SÓLIDOS, este é o mais difícil de entender e 
explicar. Para este princípio, não existe uma solução padrão do tipo “modelo” onde deva ser aplicado, e é difícil 
oferecer um “exemplo padrão” para mostrar. 

De maneira mais simplista, posso colocar, esse princípio pode ser resumido 
dizendo: Se em uma subclasse , você redefine uma função que também está presente na classe base , as duas funções 
devem ter o mesmo comportamento. Isso, porém, não significa que devam ser obrigatoriamente iguais, mas que o usuário 
deve esperar o mesmo tipo de resultado, dada a mesma entrada. No exemplo ocp.py, o método de “operação” está presente 
nas subclasses e na classe base, e um usuário final deve esperar o mesmo comportamento dos dois. 

O resultado desse 
princípio é que escreveríamos nosso código de maneira consistente e, o usuário final precisará aprender como nosso 
código funciona, apenas um. 

Termo aditivo: (Você pode pular para o próximo princípio). 
    
    Uma consequência do LSP é que: 
    a nova função redefinida na subclasse deve ser válida e possivelmente usada sempre que a mesma função na classe pai 
    for usada. 
    
    Este não é, normalmente o caso, na verdade geralmente nós, humanos, pensamos em termos de teoria dos 
    conjuntos. 
    Ter uma classe que define um conceito e subclasses que expandem o primeiro com uma exceção ou 
    comportamento diferente. 
    Por exemplo, a subclasse “Ornitorrinco”, da classe base “Mamíferos”, teria a exceção de que 
    esses mamíferos põem ovos. 
    
    O LSP, nos diz que criaria uma função chamada “give_birth”, esta função terá um 
    comportamento diferente para a subclasse Platypus e a subclasse Dog. Portanto, deveríamos ter uma classe base mais 
    abstrata do que Mamíferos que acomodasse isso. Se isso parece muito confuso, não se preocupe, a aplicação deste 
    último aspecto do LSP raramente é totalmente implementada e raramente sai dos livros teóricos. """