import pytest
from trivia import Question,Quiz
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