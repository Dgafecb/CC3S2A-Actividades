from trivia import Quiz, Question
def test_quiz_scoring():
    quiz = Quiz()
    # Cargar preguntas
    while quiz.current_question_index<10:
        question = quiz.get_next_question()
        if question:
            print(question.description)
            for id, option in enumerate(question.options):
                print(f"{id+1}) {option}")
            answer = input("Tu respuesta: ")
            if quiz.answer_question(question,answer):
                print("¡Correcto!")
            else:
                print("Incorrecto")
        else:
            break
    print(f"Juego terminado. Respuestas correctas: {quiz.correct_answers},incorrectas: {quiz.incorrect_answers}")