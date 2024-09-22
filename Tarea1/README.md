# Juego de trivia con FastAPI, PostgreSQL y DevOps
## Reglas del juego:
- Inicio del juego: Al lanzar el juego, se muestra un mensaje de bienvenida junto con las
instrucciones sobre cómo jugar.
-  Número de rondas: El juego constará de un total de 10 rondas, cada una con una pregunta
única.
-  Preguntas: Se presenta una pregunta con cuatro opciones de respuesta numeradas. Solo una
opción es correcta.
-  Selección de respuesta: El jugador elige su respuesta ingresando el número correspondiente
a la opción elegida.
-  Puntuación: Cada respuesta correcta otorga un punto. No se penaliza por respuestas
incorrectas.
-  Fin del Juego: Al finalizar las rondas, se muestra la puntuación total del jugador, junto con un
desglose de respuestas correctas e incorrectas

## Sprint1
Durante el sprint 1 realizamos el setup basico para nuestro proyecto
Empezamos por crear nuestro archivo requirements.txt
```
fastapi>=0.115.0
uvicorn>=0.30.6
asyncpg>=0.29.0
databases>=0.9.0
```
Esto nos permite configurar nuestro entorno virtual para instalar nuestras dependencias
```
python3 -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```
Luego procedimos a crear nuestro archivo Dockerfile para el entorno FastAPI y PostgreSQL
[![image.png](https://i.postimg.cc/br3GmSSZ/image.png)](https://postimg.cc/9wwFMMp2)
y nuestro archivo docker-compose.yml para gestionar PostgreSQL
[![image.png](https://i.postimg.cc/kX2M0pk1/image.png)](https://postimg.cc/Yhwwgb2Y)

Luego hicimos nuestras clases Quiz y Question basicas
```python
class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer
    def is_correct(self, answer):
        return self.correct_answer == answer
    
class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
    def add_question(self, question):
        self.questions.append(question)
    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None
```
Y ahora podemos implementar unas pruebas basicas para la clase question en test_trivia.py
```python
import pytest
from trivia import Question
def test_question_correct_answer():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    assert question.is_correct("4")
def test_question_incorrect_answer():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    assert not question.is_correct("2")

```
Como nuestro archivo requirements.txt incluia pytest podemos proceder a realizar las pruebas unitarias para este sprint
[![image.png](https://i.postimg.cc/0Qm56M0T/image.png)](https://postimg.cc/TLdvFPS0)

## Sprint2
Primero ampliamos la logica de la clase Quiz para que nos permite mantener el conteo de respuestas correctas e incorrectas
```python
class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
```
y verificar si la respuesta dada es correcta, asi como actualizar el conteo de respuestas correctas e incorrectas
```python
def answer_question(self,question,answer):
        if question.is_correct(answer):
            self.correct_answers+=1
            return True
        else:
            self.incorrect_answers+=1
            return False
```

Esto implica que necesitamos pruebas unitarias para probar esta nueva funcionalidad
```python
def test_quiz_scoring():
    # Arrange
    quiz = Quiz()
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    # Act
    quiz.add_question(question)
    # Assert
    assert quiz.answer_question(question,"4") == True
    assert quiz.correct_answers == 1
```
y finalmente agregamos la funcionalidad basica para mostrar las preguntas del quiz
```python
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
```

## Sprint3