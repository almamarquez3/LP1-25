from objetos import MEMORIZADOR, CALCULADORA, ANALIZADOR_TEXTO, SOLICITADOR

##GUIA 1
print("hola mundo desde python".upper())


mensaje= "ESTO ES UN MENSAJE"

print(mensaje.lower())

num=0.2

print(num.is_integer())

texto= "hola, mundo"

print(texto.replace("mundo", "Python"))

############

#
# int main() {
 # int num1 = 5, num2 = 10;
 # int resultado = num1 + num2;
 # printf("El resultado es %d\n", resultado);
 # return 0;
# }

print(CALCULADORA.sumar(5,10))

##########

textito="Python es genial"

print(ANALIZADOR_TEXTO.contar_palabras(textito))

#########

num1=SOLICITADOR.pedir_numero()
num2=SOLICITADOR.pedir_numero()

print(CALCULADORA.el_mayor_entre(num1,num2))

print(CALCULADORA.multiplicar(num1, num2))

print(CALCULADORA.restar(num1,num2))

print(CALCULADORA.sumar(num1, num2))

############

txt=SOLICITADOR.pedir_texto()

print(ANALIZADOR_TEXTO.palabra_mas_larga(txt))

###

txt1=SOLICITADOR.pedir_texto()
txt2=SOLICITADOR.pedir_texto()

txt1_palabra=ANALIZADOR_TEXTO.palabra_mas_larga(txt1)
txt2_palabra=ANALIZADOR_TEXTO.palabra_mas_larga(txt2)

txt1_palabra=ANALIZADOR_TEXTO.cantidad_de_letras(txt1_palabra)
txt2_palabra=ANALIZADOR_TEXTO.cantidad_de_letras(txt2_palabra)

if txt1_palabra>txt2_palabra:
    print(ANALIZADOR_TEXTO.cantidad_de_letras(txt1))
else:
    print(ANALIZADOR_TEXTO.cantidad_de_letras(txt2))
