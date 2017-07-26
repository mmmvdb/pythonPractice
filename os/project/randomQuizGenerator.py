# This is a the practice project from automate the boring stuff with python, the os chapter.

# We are supposed to make a program that will come up with 35 randomized quizzes, with random orders, random incorrect answers,
# and answer keys

# More specific requirements

# Create 35 quizzes
# Create 50 multiple-choice questions per quizzes
# Each question has a right answer and 3 random wrong answers, and each question is in random order
# Output is 35 quiz text files, 35 answer sheets

# For more information, this is apparently a state capital quiz... like they teach that in school anymore


import random
import os

# ==== Get quiz data ====

# This should probably be in a different file if this was the real world, but this is just an exercise so:
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

dirPath = os.path.join(os.getcwd() , 'quizzes')

if os.path.isdir(dirPath) == False:
    os.makedirs(dirPath)
   
# ==== Generate 35 quiz files ====
for quizNum in range(35):
    # ==== Create the quiz and answer key files ====
    quizFile = open(os.path.join(dirPath, 'capitalsquiz%s.txt' % (quizNum + 1)), 'w')
    keyFile  = open(os.path.join(dirPath, 'capitalsquiz_answers%s.txt' % (quizNum + 1)), 'w')
    
    # ==== Write out the header for the quiz ====
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    
    # ==== Shuffle the order of the states ====
    states = list(capitals.keys())
    random.shuffle(states)
        
    # ==== Loop through all 50 states, making a question for each ====
    for questionNum in range(50):
        # save correct answer
        correctAnswer = capitals[states[questionNum]]
        
        # create wrong answers by duplicating values, removing our right answer and randomly sampling 3
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        
        # create the possible answers as a list
        answerOptions = wrongAnswers + [correctAnswer]
        
        # and shuffle them
        random.shuffle(answerOptions)
        
        # write out the question in the quiz
        quizFile.write('%s.  What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        
        quizFile.write('\n')
        
        # write out the to the answer key
        keyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
        
    quizFile.close()
    keyFile.close()
        