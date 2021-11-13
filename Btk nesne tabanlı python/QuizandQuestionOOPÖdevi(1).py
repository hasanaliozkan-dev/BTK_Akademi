from Question import Question
from Quiz import Quiz

q1 = Question("En büyük il hangisidir?",["Konya" ,"Adana" ,"Ankara" ,"Erzurum"],"Konya")
q2 = Question("En kalabalık il hangisidir?",["Konya" ,"Istanbul" ,"Ankara" ,"Erzurum"],"Istanbul")
q3 = Question("Başkent hangisidir?",["Konya" ,"Adana" ,"Ankara" ,"Erzurum"],"Ankara")
q4 = Question("En büyük il hangisidir?",["Konya" ,"Adana" ,"Ankara" ,"Erzurum"],"Konya")
q5 = Question("En kalabalık il hangisidir?",["Konya" ,"Istanbul" ,"Ankara" ,"Erzurum"],"Istanbul")
q6 = Question("Başkent hangisidir?",["Konya" ,"Adana" ,"Ankara" ,"Erzurum"],"Ankara")
q7 = Question("En büyük il hangisidir?",["Konya" ,"Adana" ,"Ankara" ,"Erzurum"],"Konya")
q8 = Question("En kalabalık il hangisidir?",["Konya" ,"Istanbul" ,"Ankara" ,"Erzurum"],"Istanbul")
q9 = Question("Başkent hangisidir?",["Konya" ,"Adana" ,"Ankara" ,"Erzurum"],"Ankara")
questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9]
quiz = Quiz(questions)

quiz.loadQuestion()
