# Idea: Hacer un quizz que dadas unas preguntas con 4 opciones, si la aciertas pasas a la siguiente y si no pierdes y vuelves a empezar

import random

# La primera opción es la correcta, y el programa las desordena
QUESTIONS = [["¿Cuál es la capital de Francia?", ["París", "Roma", "Londres", "Berlín"]],
    ["¿Quién pintó la Mona Lisa?", ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"]],
    ["¿Cuál es el río más largo del mundo?", ["Amazonas", "Nilo", "Yangtsé", "Mississippi"]],
    ["¿En qué año comenzó la Segunda Guerra Mundial?", ["1939", "1945", "1914", "1941"]],
    ["¿Cuál es el elemento más abundante en la corteza terrestre?", ["Oxígeno", "Silicio", "Aluminio", "Hierro"]],
    ["¿Cuál es el país más poblado del mundo?", ["China", "India", "Estados Unidos", "Brasil"]],
    ["¿Quién escribió el libro '1984'?", ["George Orwell", "Fyodor Dostoyevsky", "Ernest Hemingway", "William Shakespeare"]],
    ["¿Cuál es el planeta más grande del sistema solar?", ["Júpiter", "Saturno", "Urano", "Neptuno"]],
    ["¿Quién pintó 'La noche estrellada'?", ["Vincent van Gogh", "Claude Monet", "Salvador Dalí", "Pablo Picasso"]],
    ["¿Cuál es el océano más grande del mundo?", ["Océano Pacífico", "Océano Atlántico", "Océano Índico", "Océano Ártico"]],
    ["¿En qué año llegó el hombre a la Luna?", ["1969", "1975", "1961", "1972"]],
    ["¿Cuál es el símbolo químico del oro?", ["Au", "Ag", "Fe", "Cu"]],
    ["¿Quién escribió 'Cien años de soledad'?", ["Gabriel García Márquez", "Jorge Luis Borges", "Pablo Neruda", "Mario Vargas Llosa"]],
    ["¿Cuál es el país más grande del mundo en términos de superficie?", ["Rusia", "Canadá", "Estados Unidos", "China"]],
    ["¿Quién pintó 'La última cena'?", ["Leonardo da Vinci", "Pablo Picasso", "Michelangelo", "Vincent van Gogh"]],
    ["¿Cuál es el autor de 'Romeo y Julieta'?", ["William Shakespeare", "Friedrich Nietzsche", "Charles Dickens", "Jane Austen"]],
    ["¿Cuál es la montaña más alta del mundo?", ["Monte Everest", "Monte Kilimanjaro", "Monte Aconcagua", "Monte Denali"]],
    ["¿Quién fue el primer presidente de los Estados Unidos?", ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John F. Kennedy"]],
    ["¿Cuál es el país conocido como 'la tierra del sol naciente'?", ["Japón", "China", "India", "Rusia"]],
    ["¿Cuál es el país más grande de Sudamérica?", ["Brasil", "Argentina", "Colombia", "Perú"]],
    ["¿Quién escribió 'Don Quijote de la Mancha'?", ["Miguel de Cervantes", "Federico García Lorca", "Jorge Luis Borges", "Pablo Neruda"]],
    ["¿Cuál es el océano más pequeño del mundo?", ["Océano Ártico", "Océano Índico", "Océano Pacífico", "Océano Atlántico"]],
    ["¿Quién pintó 'Los girasoles'?", ["Vincent van Gogh", "Pablo Picasso", "Salvador Dalí", "Leonardo da Vinci"]],
    ["¿Cuál es el país más poblado de África?", ["Nigeria", "Egipto", "Etiopía", "Sudáfrica"]],
    ["¿Quién escribió 'Hamlet'?", ["William Shakespeare", "Jane Austen", "Fyodor Dostoyevsky", "Gabriel García Márquez"]],
    ["¿Cuál es el metal líquido a temperatura ambiente?", ["Mercurio", "Plomo", "Hierro", "Aluminio"]],
    ["¿Quién pintó 'La persistencia de la memoria'?", ["Salvador Dalí", "Claude Monet", "Pablo Picasso", "Vincent van Gogh"]],
    ["¿Cuál es el país más visitado del mundo?", ["Francia", "España", "Estados Unidos", "China"]],
    ["¿Cuál es el libro más vendido de todos los tiempos?", ["La Biblia", "Don Quijote de la Mancha", "El principito", "Harry Potter y la piedra filosofal"]],
    ["¿Quién escribió 'Orgullo y prejuicio'?", ["Jane Austen", "Emily Brontë", "Virginia Woolf", "Charlotte Brontë"]],
    ["¿Cuál es el animal terrestre más rápido del mundo?", ["Guepardo", "León", "Jirafa", "Elefante"]],
    ["¿En qué país se encuentra la Torre Eiffel?", ["Francia", "Italia", "Alemania", "España"]],
    ["¿Cuál es la montaña más alta de Europa?", ["Monte Elbrus", "Monte Blanc", "Monte Everest", "Monte Kilimanjaro"]],
    ["¿Quién escribió 'El Gran Gatsby'?", ["F. Scott Fitzgerald", "Ernest Hemingway", "Mark Twain", "J.D. Salinger"]],
    ["¿Cuál es el país más pequeño del mundo?", ["Ciudad del Vaticano", "Mónaco", "Nauru", "Tuvalu"]],
    ["¿Cuál es el pintor del famoso cuadro 'La persistencia de la memoria'?", ["Salvador Dalí", "Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci"]],
    ["¿Cuál es el país más poblado de Europa?", ["Rusia", "Alemania", "Francia", "Reino Unido"]],
    ["¿Quién escribió 'Crimen y castigo'?", ["Fyodor Dostoyevsky", "Leo Tolstoy", "Anton Chekhov", "Aleksandr Solzhenitsyn"]],
    ["¿Cuál es el instrumento musical más grande de la orquesta?", ["Contrabajo", "Piano", "Trombón", "Violín"]]]

# Para dado una letra te de un numero de la lista de respuestas, y el otro para poder hacer el print en consola con el a,b,c,d delante
ANSWERS = {"a": 0, "b": 1, "c": 2, "d": 3}
PRINT_ANSWERS = ["a", "b", "c", "d"]

def print_question(i, question):
    print(f"{i}- {question[0]}")
    for n, opcion in enumerate(question[1]):
        print(f"{PRINT_ANSWERS[n]}) {opcion}")

def valid_answer():
    while True:
        user_answer = input("Respuesta: $ ").lower()
        if user_answer in ANSWERS:
            return user_answer
        else:
            print("Respuesta inválida. Por favor, ingresa 'a', 'b', 'c' o 'd'")

def Quizz():
    n_question = 1
    n_correct = 0
    random.shuffle(QUESTIONS)
    for question in QUESTIONS:
        correct_answer = question[1][0]
        random.shuffle(question[1])
        print_question(n_question, question)
        user_answer = valid_answer()
        if question[1][ANSWERS[user_answer]] == correct_answer:
            n_correct += 1
            print("\n¡Correcto!\n")
        else:
            print("\nRespuesta incorrecta, eliminado del Quizz")
            break
        n_question += 1


if __name__ == "__main__":
    Quizz()