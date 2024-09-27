import random #impoting random module
questions=[
    #ques1
{
  "question":"Which of the following is a cat’s favorite pastime?",
  "options":["A. Knitting", "B. Sleeping", "C. Writing novels", "D. Skydiving"],
  "answers":"B"
},
{
    #ques2
  "question":"What is a cat’s natural enemy?",
  "options":["A. Dogs", "B. Laser pointers", "C. Water", "D. Birds"],
  "answers":"C" 
},
{
    #ques3
    "question":"How many lives do cats famously have?",
    "options":["A. 3","B. 7","C. 9""D. 10"],
    "answers":"C"
},
{
    #ques4
    "question":"Why do cats love to sit in boxes?",
    "options":["A. Because they’re secret ninjas","B. To protect themselves from imaginary enemies","C. They love confined spaces","D. They are planning world domination from inside the box"],
    "answers":"C"
},
{
    #ques5
    "question":"What is a common reason for cats purring?",
    "options":["A. They are plotting","B. They are hungry","C. They are happy or content","D. They are bored"],
    "answers":"C"
},
{
    #ques6
    "question":"Why do cats knead with their paws?",
    "options":["A. It’s their way of baking bread","B. To mark their territory","C. It reminds them of kittenhood","D. They enjoy it"],
    "answers":"C"
},
{
    #ques7
    "question":"What is the scientific name for a house cat?",
    "options":["A. Felis lupus","B. Felis catus","C. Feline awesomeus","D. Purrfectus"],
    "answers":"B"
},
{
    #ques8
    "question":"Which breed of cat is known for being hairless?",
    "options":["A. Siamese","B. Persian","C. Sphynx","D. Bengal"],
    "answers":"C"
},
{
    #ques9
    "question":"Why do cats' eyes glow in the dark?",
    "options":["A. They are powered by the moon","B. They have a layer called the tapetum lucidum that reflects light",
"C. They are using laser vision","D. It’s a special night-vision skill"],
    "answers":"B"
},
{
    #ques10
    "question":"What is a group of cats called?",
    "options":["A. A murder","B. A clowder","C. A herd","D. A pod"],
    "answers":"B"
},
{
    #ques11
    "question":"How far can a cat jump compared to its body length?",
    "options":["A. 1x its body length","B. 2x its body length","C. 5x its body length","D. 10x its body length"],
    "answers":"C"
},
{
    #ques12
    "question":"What sense is the strongest in cats?",
    "options":["A. Sight","B. Hearing","C. Smell","D. Taste"],
    "answers":"B"
},
{
    #ques13
    "question":"Which breed of cat is known for its 'bobbed' tail?",
    "options":["A. Manx","B. Ragdoll","C. Abyssinian","D. Scottish Fold"],
    "answers":"A"
},
{
    #ques14
    "question":"What is the oldest cat in the world?",
    "options":["A. 12 years old","B. 25 years old","C. 38 years old","D. 50 years old"],
    "answers":"C"
},
{
    #ques15
    "question":"What’s a cat’s secret superpower?",
    "options":["A. Mind reading","B. Always landing on their feet","C. Turning invisible at will","D. Speaking every language"],
    "answers":"B"
},
{
    #ques16
    "question":"Why do cats sometimes bring their owners dead animals?",
    "options":["A. They think you’re a bad hunter","B. To gross you out","C. To show off their skills",
"D. It’s a love offering"],
    "answers":"A"
},
{
    #ques17
    "question":"What’s a cat’s favorite toy?",
    "options":["A. Goldfish","B. A string","C. A computer mouse","D. A rubber duck"],
    "answers":"B"
}
,
{
    #ques18
    "question":"What’s the maximum speed a cat can run?",
    "options":["A. 10 mph","B. 15 mph","C. 30 mph","D. 50 mph"],
    "answers":"C"
},
{
    #ques19
    "question":"What do cats use their whiskers for?",
    "options":["A. Sensing their surroundings","B. Decoration","C. To keep food out of their mouth",
"D. Showing off"],
    "answers":"A"
}
,
{
    #ques20
    "question":"Which breed of cat is famous for its blue eyes?",
    "options":["A. Persian","B. Siamese","C. British Shorthair","D. Maine Coon"],
    "answers":"B"
},
{
    #ques21
    "question":"What’s the primary reason cats scratch things?",
    "options":["A. To sharpen their claws","B. To annoy their owners","C. To exercise","D. To keep things clean"],
    "answers":"A"
},
{
    #ques22
    "question":"How many hours do cats typically sleep each day?",
    "options":["A. 8 hours","B. 12 hours","C. 16 hours","D. 20 hours"],
    "answers":"C"
},
{
    #ques23
    "question":"Which famous artist was known for his love of cats?",
    "options":["A. Pablo Picasso","B. Vincent van Gogh","C. Salvador Dali","D. Leonardo da Vinci"],
    "answers":"D"
},
{
    #ques24
    "question":"What do you call a cat with extra toes?",
    "options":["A. A polydactyl cat","B. A double cat","C. A mutant cat","D. A super cat"],
    "answers":"A"
},
{
    #ques25
    "question":" Why do cats like to rub against people and objects?",
    "options":["A. They’re itchy","B. They’re marking their territory","C. They’re trying to knock you over",
"D. It’s a power move"],
    "answers":"B"
},
{
    #ques26
    "question":"What part of a cat is unique, like a human fingerprint?",
    "options":["A. Tail","B. Whiskers","C. Paw pads","D. Nose"],
    "answers":"D"
},

{
    #ques27
    "question":"What does it mean when a cat’s tail is puffed up?",
    "options":["A. They are ready for a selfie","B. They’re scared or agitated","C. They’re about to fall asleep",
"D. It’s cold outside"],
    "answers":"B"
},
{
    #ques28
    "question":"Why do cats love to chase lasers?",
    "options":["A. They think it's a bug","B. They are practicing their hunting skills","C. They want to catch the light",
"D. They like shiny things"],
    "answers":"B"
}
,
{
    #ques29
    "question":"What is a “catnap”?",
    "options":["A. A quick sleep","B. A long sleep","C. A confused sleep","D. A lazy day"],
    "answers":"A"
}
,
{
    #ques30
    "question":"How many muscles do cats have in their ears?",
    "options":["A. 12","B. 24","C. 32","D. 40"],
    "answers":"C"
}
,
{
    #ques31
    "question":"What’s a cat’s most sensitive body part?",
    "options":["A. Ears","B. Whiskers","C. Paws",
"D. Tail"],
    "answers":"B"
}
,
{
    #ques32
    "question":"Which breed is the “gentle giant” of cats?",
    "options":["A. Siamese","B. Maine Coon","C. Sphynx","D. British Shorthair"],
    "answers":"B"
}
,
{
    #ques33
    "question":"Which type of cat is known for its folded ears?",
    "options":["A. Persian","B. Scottish Fold","C. Burmese","D. Abyssinian"],
    "answers":"B"
}
,
{
    #ques34
    "question":"How long is a cat’s pregnancy?",
    "options":["A. 1 month","B. 2 months","C. 3 months","D. 6 months"],
    "answers":"2"
}
,
{
    #ques35
    "question":"Why do cats chase their tails?",
    "options":["A. Because it’s fun","B. They’re bored","C. They think it’s prey","D. To confuse you"],
    "answers":"A"
}
,
{
    #ques36
    "question":"What’s the technical term for cat hairballs?",
    "options":["A. Furritos","B. Hairloaf","C. Trichobezoars","D. Fluffballs"],
    "answers":"C"
}
,
{
    #ques37
    "question":"What’s the longest recorded cat jump?",
    "options":["A. 5 feet","B. 8 feet","C. 12 feet","D. 15 feet"],
    "answers":"C"
}
,
{
    #ques38
    "question":"What’s the most common cat coat color?",
    "options":["A. Calico","B. Black","C. White","D. Tabby"],
    "answers":"D"
}
,
{
    #ques39
    "question":"Why do cats wag their tails?",
    "options":["A. They’re happy","B. They’re annoyed","C. They’re concentrating","D. They’re tired"],
    "answers":"B"
}
,
{
    #ques40
    "question":" Which breed is known for being large and fluffy?",
    "options":["A. Sphynx","B. Ragdoll","C. Maine Coon","D. Siamese"],
    "answers":"C"
}
,
{
    #ques41
    "question":"What do cats do when they’re bored?",
    "options":["A. Write poetry","B. Stare at walls","C. Sleep","D. Play with imaginary friends"],
    "answers":"C"
}
,
{
    #ques42
    "question":"Why do cats sometimes stare at you without blinking?",
    "options":["A. They are trying to read your mind","B. They are hypnotizing you","C. It’s a sign of affection",
"D. They are confused by your human ways"],
    "answers":"C"
},

{
    #ques43
    "question":"What do you call a cat that loves to swim?",
    "options":["A. Bengal","B. Siamese","C. Turkish Van","D. Persian"],
    "answers":"C"
}
,
{
    #ques44
    "question":"Why do some cats “chirp” at birds?",
    "options":["A. They are trying to mimic bird sounds","B. They are frustrated","C. They are talking to birds",
"D. They are practicing hunting calls"],
    "answers":"B"
}
,
{
    #ques45
    "question":"What breed of cat is most likely to enjoy fetching?",
    "options":["A. Bengal","B. Persian","C. Maine Coon","D. British Shorthair"],
    "answers":"A"
}
,
{
    #ques46
    "question":"What’s a cat’s favorite type of fish?",
    "options":["A. Salmon","B. Tuna","C. Sardine","D. All of the above"],
    "answers":"D"
}
,
{
    #ques47
    "question":"What sound does a content cat usually make?",
    "options":["A. Bark","B. Purr","C. Chirp","D. Squeak"],
    "answers":"B"
}
,
{
    #ques48
    "question":"Which ancient civilization worshipped cats?",
    "options":["A. Romans","B. Greeks","C. Egyptians","D. Mayans"],
    "answers":"C"
},
{
    #ques49
    "question":"What’s the smallest breed of cat?",
    "options":["A. Munchkin","B. Siamese","C. Maine Coon","D. Abyssinian"],
    "answers":"A"
},
{
    #ques50
    "question":"Why do cats love to knock things off tables?",
    "options":["A. They are rebels","B. To annoy you","C. They’re testing gravity","D. They enjoy destruction"],
    "answers":"C"
}
]
"""for question in questions:
    print(f"{question['question']}")
    for option in question["options"]:
        print(f"{option}")
    print(f"Answers:{question['answers']}")"""

answers_list=["A","B","C","D"]
score=0

def playGame():
    print("Play Game")
    global score
    i=0
    asked_questions= []

    while i<len(questions):
        # Getting random number from 0-49
        random_number=random.randrange(0,len(questions)) #getting random number from 0-49
        
        while random_number in asked_questions:
            random_number=random.randrange(0,len(questions))
        
        # Marking the question as asked 
        asked_questions.append(random_number)

        #get the elements of questions list
        random_question=questions[random_number] 
        print(f"Question{i+1} :{random_question["question"]}")
        
        #to loop through dictionary in questions for options
        for option in random_question["options"]:
            print(option)

        user_input=input("Enter A/B/C/D to choose answer\n").upper()

        validate_input(user_input,random_question)
        i+=1

def validate_input(user,random_question):

    """This method is defined to check the 
    validity of user input and checking the answers of user
    """
    global score
    
     # Loop to keep asking until the user provides a valid answer
    while user not in answers_list:
        print("Invalid input. Please enter a valid option (A/B/C/D).")
        user = input("Enter A/B/C/D to choose your answer\n").upper()
    
    # After valid input, check if the user's input matches the correct answer
    if user == random_question["answers"]:
        score += 1
        print("Your answer is correct!")
        print(f"Your Score is: {score}\n")
    else:
        print("Wrong Answer")
    
playGame()

    


   

    
    
