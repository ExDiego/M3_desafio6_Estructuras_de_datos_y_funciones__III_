preguntas_basicas = {
    'pregunta_1': {'enunciado': ['¿Cuál es el océano más grande del mundo?'],
                    'alternativas': [['Océano Pacífico', 1],
                                    ['Océano Atlántico', 0],
                                    ['Océano Índico', 0],
                                    ['Océano Ártico', 0]]},

    'pregunta_2': {'enunciado': ['¿Cuál es el animal terrestre más rápido?'],
                    'alternativas': [['Leopardo', 0],
                                    ['Guepardo', 1],
                                    ['León', 0],
                                    ['Lobo', 0]]},

    'pregunta_3': {'enunciado': ['¿Cuál es la capital de Francia?'],
                    'alternativas': [['Roma', 0],
                                    ['París', 1],
                                    ['Madrid', 0],
                                    ['Londres', 0]]}
}

preguntas_intermedias = {
    'pregunta_1': {'enunciado': ['¿En qué año comenzó la Primera Guerra Mundial?'],
                    'alternativas': [['1914', 1],
                                    ['1939', 0],
                                    ['1918', 0],
                                    ['1945', 0]]},

    'pregunta_2': {'enunciado': ['¿Quién pintó la Mona Lisa?'],
                    'alternativas': [['Leonardo da Vinci', 1],
                                    ['Pablo Picasso', 0],
                                    ['Vincent van Gogh', 0],
                                    ['Salvador Dalí', 0]]},

    'pregunta_3': {'enunciado': ['¿Cuál es el río más largo del mundo?'],
                    'alternativas': [['Río Amazonas', 0],
                                    ['Río Nilo', 1],
                                    ['Río Yangtsé', 0],
                                    ['Río Misisipi', 0]]}
}

preguntas_avanzadas = {
    'pregunta_1': {'enunciado': ['¿Cuál es el elemento más abundante en la Tierra?'],
                    'alternativas': [['Hierro', 0],
                                    ['Aluminio', 0],
                                    ['Oxígeno', 1],
                                    ['Carbono', 0]]},

    'pregunta_2': {'enunciado': ['¿Cuál es el autor de la obra "Don Quijote de la Mancha"?'],
                    'alternativas': [['Miguel de Cervantes', 1],
                                    ['William Shakespeare', 0],
                                    ['Friedrich Nietzsche', 0],
                                    ['Gabriel García Márquez', 0]]},

    'pregunta_3': {'enunciado': ['¿Qué planeta es conocido como "El planeta rojo"?'],
                    'alternativas': [['Júpiter', 0],
                                    ['Marte', 1],
                                    ['Venus', 0],
                                    ['Mercurio', 0]]}
}

pool_preguntas = {'basicas': preguntas_basicas,
                    'intermedias': preguntas_intermedias,
                    'avanzadas': preguntas_avanzadas}
