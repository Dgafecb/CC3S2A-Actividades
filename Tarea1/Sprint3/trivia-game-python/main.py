from trivia import Quiz, Question
def load_questions(file):
    #Leemeos el archivo que contendra preguntas con el formato "pregunta, alternativa1, alt2, alt3, alt4, alternativa_correcta"
    questions = []
    with open(file,'r') as file:
        for line in file:
            line = line.strip()
            if line:
                secciones = line.split(',')
                description = secciones[0].strip()
                options= [option.strip() for option in secciones[1:-1]]
                correct_answer = secciones[-1].strip()
                question = Question(description,options,correct_answer)
                questions.append(question)
    return questions
def quiz_scoring():
    quiz = Quiz()
    #Agregamos la capacidad de elegir la dificultad
    dificultad = input("Que dificultad deseas usar: \n1) Facil\n2) Intermedio\n 3) Dificil \n")
    if int(dificultad)==3:
        preguntas='questions_dificil.txt'
    elif int(dificultad)==2:
        preguntas='questions_intermedio.txt'
    else:
        preguntas='questions_facil.txt'#Predeterminado elegira el set de preguntas facil
    #Cargamos las preguntas de questions.txt
    questions= load_questions(preguntas)
    for question in questions:
        quiz.add_question(question)#Agregamos las preguntas al quiz

    while quiz.current_question_index<10:
        question = quiz.get_next_question()
        if question:
            print(question.description)
            for id, option in enumerate(question.options):
                print(f"{id+1}) {option}")
            
            answer = input("Tu respuesta: \n")
            if quiz.answer_question(question,answer):
                print("¡Correcto!")
            else:
                print("Incorrecto")
        else:
            break
    print("Juego terminado.")
    print(f"Preguntas contestadas: {quiz.current_question_index}")
    print(f"Respuestas correctas: {quiz.correct_answers}")
    print(f"Respuestas Incorrectas: {quiz.incorrect_answers}")

def run_quiz():
    print("Bienvenido al juego de trivia")
    print("Responde a las siguientes preguntas seleccionando el numero de la opcion correcta")
    quiz_scoring()
    
run_quiz()#Iniciamos el juego
    