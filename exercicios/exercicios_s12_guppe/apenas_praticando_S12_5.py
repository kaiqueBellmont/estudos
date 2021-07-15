def checa(num1, num2):
    if num1 / num2 != 0:
        print("impar")


@checa
def naosei(a, b):
    return a, b


print(naosei(10, 5))


def checa_login():
    if not request.usuario:
        redirect('http://www.suaempresa.com.br/login')


def home(request):
    return 'Pode acessar home'

@checa_login
def servicos(request):
    return 'Pode acessar serviços'
