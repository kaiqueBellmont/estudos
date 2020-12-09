"""
Estruturas condicionais
if (Se), else, elif (else if)
"""

idade = 18

"""
# Estrutura condicional if, else em C

if(idade < 18){
    printf("Menor de idade");
}else if(idade == 18){
  printf("Tem 18 anos");
}else{
  printf("É menor de idade");
}
"""

"""
# Estrutura condicional if, else em Java

if(idade < 18){
    System.out.println("Menor de idade");
}else if(idade == 18){
  System.out.println("Tem 18 anos");
}else{
  System.out.println("É menor de idade");
}
"""
"""
Um Bloco em python começa com Dois pontos " : " 
Na proxima linha, inicia - se com 4 espaços.
"""

# Só tem um if / else, mas elif pode ter vários. Fica a dica ai.

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de idade')
