import preguntas as p
import random

def shuffle_alt(pregunta):
    # Paso 4: Tomar de las preguntas sólo la clave correspondiente a alternativas y estas deben ser mezcladas.
    alternativas = pregunta['alternativas']
    random.shuffle(alternativas)
    return pregunta['alternativas']

if __name__ == '__main__':
    pregunta_ejemplo = p.pool_preguntas['basicas']['pregunta_1']
    print(shuffle_alt(pregunta_ejemplo)) #verificación de las alternativas mezcladas
    