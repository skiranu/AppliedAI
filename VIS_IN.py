import random
import time
import pyttsx3
engine = pyttsx3.init()
#YOU CAN ADD/DELETE THE questionnaire from below.
AUDIO=['Why do you want to study at this University',
'Why do you want to study this degree',
'Why do you want to study in the USA',
'What are you going to specialize in',
'How many universities did you apply',
'Which universities did you apply to',
'How many admission did you get admitted',
'Where did you complete the undergraduate or graduate degree',
'What is your undergraduate GPA',
'Tell me about the university you are planning to attend.',
'Mention the name of the professor’s you had contacted.',
'When and where did you get your bachelor’s degree',
'How long will you study in the USA',
'How do you know about this university',
'What is your academic background',
'Do you plan to study PhD after MS',
'Why did you apply to these universities',
'Why not attend University X',
'What courses are you planning to take in your first semester',
'Why not study in India?'
,'Who is sponsoring your education in the US'
,'What does your sponsor do'
,'Where did you get this bank statement?'
,'Why do you think we should give you visa to study in USA?'
,'Are there any reasons why you shouldn’t be given F1 Visa?'
,'Did you pay anyone to get this bank statement?'
,'What is your university yearly expense?'
,'Did you get an education loan?'
,'Can you show your Bank Statements?'
,'What is your father’s salary?'
,'How long has he been working here?'
,'Do you have a statement from the sponsor on bank letterhead?'
,'Do you have a financial affidavit from the US-based sponsor?'
,'How will you finance your education for 2 years or 3 years when your bank balance shows 1 year worth of expenses?'
,'Why the specified University.'
,'Which Universities did you apply to (both admits and rejects).'
,'Show me your GRE scorecard.'
,'Where did you Undergraduate from.'
,'Show me your Undergraduate degree.'
,'Who is sponsoring you.'
,'Are you married?'
,'What does your father do.'
,"What is your father's Income."
,'How many brothers and sisters do you have.'
,'Do you have any relatives in the USA.'
,"Why don't you do this course in your country?"
,'What will you do after completing MS.'
,'Show your Experience Certificate.'
,'Why Study in the USA.'
,'Did you got Scholarships.'
,'Have you got any Loans.'
,'Show your Pass Books/Bank statements.'
,'What is your Undergraduate GPA/Percentage.'
,'Do you have any backlogs?'
,'Are your parents retired? How will they pay?'
,'Tell about your university.'
,'Mention some professor names.'
,'Tell me how can you prove that you are gonna come back.'
,'Where did your brother/parents complete their studies.'
,"What's your Religion."
,'Why are you leaving your current job?'
,'Have you ever been to the US?'
,'What will you do after coming back to home.'
,'You have so many brothers and sisters so your fathers saving is just for you? How will you finance?'
,'Where do your parents live (If they live in the USA).'
,'Do you know anyone in your University?'
,'Do you know anyone in the US?'
,'What will you do if your Visa is rejected.'
,'Will you come back to home during summers.'
,'Where are you planning to stay in the USA?'
,'Have you paid your semester fees?'
,"You don't have scholarship and you want to come back.. how will you pay your debt?"]

import os 
i=0
# The text that you want to convert to audio
engine.say("please pass me your passport and I20")
engine.runAndWait()
time.sleep(2)
#Number of questions is 15 in the while loop, this can be changed.
while(i<15):
    #random questions asked.
    random1 = random.randint(0,len(AUDIO)-1)
    mytext = AUDIO[random1]
    engine.say(mytext)
    engine.runAndWait()
    #time given for each answer,could be changed accordingly.
    time.sleep(15)
    i=i+1
    


