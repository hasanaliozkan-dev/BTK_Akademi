from Question import Question
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionindex = 0
    def getquestion(self):
        return self.questions[self.questionindex]
    def displayQuestions(self):
        question = self.getquestion()
        print(f"Question {self.questionindex + 1}:{question.text}")

        for q in question.choices:
            print("-" + q)
        answer = input("Answer:").capitalize()
        self.guess(answer)
        self.loadQuestion()
    def guess(self,answer):
        question = self.getquestion()
        if question.checkAnswer(answer):
            self.score += 1
        self.questionindex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionindex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestions()
    def showScore(self):
        print(f"Score : {self.score}")

    def displayProgress(self):
        totalQuestions = len(self.questions)
        questionNumber = self.questionindex + 1
        if questionNumber > totalQuestions:
            print("The quiz is over")
        else:
            print(f"Question {questionNumber} of {totalQuestions}".center(100,"*") )
