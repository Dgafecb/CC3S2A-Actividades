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
        self.correct_answers = 0
        self.incorrect_answers = 0
    def add_question(self, question):
        self.questions.append(question)
    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None
    def answer_question(self,question,answer):
        if question.is_correct(answer):
            self.correct_answers+=1
            return True
        else:
            self.incorrect_answers+=1
            return False
    def load_questions(self,file):
        #Leemos el archivo que contendra preguntas con el formato "pregunta, alternativa1, alt2, alt3, alt4, alternativa_correcta"
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