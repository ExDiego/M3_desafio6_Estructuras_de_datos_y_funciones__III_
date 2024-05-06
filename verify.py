import preguntas as p


def verificar(alternativas, eleccion):
    #convierte la elección a minúsculas para comparación
    eleccion = eleccion.lower()
    indice_eleccion = ord(eleccion) - ord('a')
    
    if alternativas[indice_eleccion][1] == 1:
        print('Respuesta Correcta !')
        return True
    else:
        print('Respuestas Incorrecta :(')
        return False



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta (A, B, C, D):\n> ')
    verificar(pregunta['alternativas'], respuesta)






