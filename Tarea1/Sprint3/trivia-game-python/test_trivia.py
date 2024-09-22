import pytest,os 
from trivia import Question,Quiz
# Nos permite configurar y limpiar el archivo test_questions.txt para las pruebas
@pytest.fixture(scope='module')
def test_file():
    # Creamos un archivo de prueba
    test_file_name = 'test_questions.txt'
    test_file = "What is 2+2?,1,2,3,4,4\nWhat is the capital of France?,London,Berlin,Paris,Madrid,Paris"    
    with open(test_file_name,'w') as file:
        file.write(test_file)
    yield test_file_name
    # Finalmente removemos el archivo de prueba creado
    if os.path.exists(test_file_name):
        os.remove(test_file_name)

def test_question_correct_answer():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    assert question.is_correct("4")
def test_question_incorrect_answer():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    assert not question.is_correct("2")

def test_quiz_scoring():
    # Arrange
    quiz = Quiz()
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    # Act
    quiz.add_question(question)
    # Assert
    assert quiz.answer_question(question,"4") == True
    assert quiz.correct_answers == 1

def test_load_questions(test_file):
    quiz = Quiz()
    # Act
    questions = quiz.load_questions(test_file)
    # Assert
    assert len(questions) == 2
    assert questions[0].description == "What is 2+2?"
    assert questions[0].options ==["1","2","3","4"]
    assert questions[0].correct_answer == "4"

