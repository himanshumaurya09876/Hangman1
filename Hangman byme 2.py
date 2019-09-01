import random

mylists =  ["apple", "apricot", "almond", "banana", "blackberry", "blueberry", "coconut", "cherry", "date", "guava", "gooseberry", "grape", "grapefruit", "jackfruit", "kiwifruit", "lemon", "lime", "lychee", "mango", "melon", "watermelon", "orange", "peach", "pear", "plum", "pineapple", "pomegranate", "raspberry", "strawberry", "tomato", "antelope", "ass", "ape", "bear", "bitch", "buffalo", "bull", "cow", "cat", "chimpanzee", "dog", "deer", "donkey", "elephant", "fox", "giraffe", "goat", "horse", "hippopotamus", "hare", "hyena", "jackal", "kangaroo", "lion", "leopard", "monkey", "ox", "pig", "rhinoceros", "sheep", "tiger", "wolf", "yalk", "zebra", "bat", "cuckoo", "cock", "crow", "crane", "dock", "eagle", "hen", "heron", "hawk", "jay", "kite", "nightingale", "ostrich", "owl", "parrot", "pea-hen", "pigeon", "pea-cock", "sprrow", "stork", "vulture", "wood-pecker", "black", "blue", "brown", "crimson", "grey", "golden", "green", "indigo", "lemon", "maroon", "orange", "pink", "purple", "rosy", "red", "violet", "white", "yellow", "arum", "brinjal", "bittergourd", "bean", "coriander", "cauliflower", "carrot", "cucumber", "cabbage", "cucurbit", "chilli", "ginger", "garlic", "jackfruit", "ladyfinger", "lemon", "mushroom", "onion", "potato", "pumpkin", "pea", "radish", "spinach", "turnip", "tomato"]
fruits = ["apple", "apricot", "almond", "banana", "blackberry", "blueberry", "coconut", "cherry", "date", "guava", "gooseberry", "grape", "grapefruit", "jackfruit", "kiwifruit", "lemon", "lime", "lychee", "mango", "melon", "watermelon", "orange", "peach", "pear", "plum", "pineapple", "pomegranate", "raspberry", "strawberry", "tomato"]
animals = ["antelope", "ass", "ape", "bear", "bitch", "buffalo", "bull", "cow", "cat", "chimpanzee", "dog", "deer", "donkey", "elephant", "fox", "giraffe", "goat", "horse", "hippopotamus", "hare", "hyena", "jackal", "kangaroo", "lion", "leopard", "monkey", "ox", "pig", "rhinoceros", "sheep", "tiger", "wolf", "yalk", "zebra"]
birds = ["bat", "cuckoo", "cock", "crow", "crane", "duck", "eagle", "hen", "heron", "hawk", "jay", "kite", "nightingale", "ostrich", "owl", "parrot", "pea-hen", "pigeon", "pea-cock", "sprrow", "stork", "vulture", "wood-pecker"]
colors = ["black", "blue", "brown", "crimson", "grey", "golden", "green", "indigo", "lemon", "maroon", "orange", "pink", "purple", "rosy", "red", "violet", "white", "yellow"]
vegetables = ["arum", "brinjal", "bittergourd", "bean", "coriander", "cauliflower", "carrot", "cucumber", "cabbage", "cucurbit", "chilli", "ginger", "garlic", "jackfruit", "ladyfinger", "lemon", "mushroom", "onion", "potato", "pumpkin", "pea", "radish", "spinach", "turnip", "tomato"]

choice = "y"
while choice == "y":
 word = random.choice(mylists)
 mylist = ""

 if word in fruits:
    mylist += "Fruit"
 elif word in animals:
    mylist += "Animal"
 elif word in birds:
    mylist += "Bird"
 elif word in colors:
    mylist += "Color"
 elif word in vegetables:
    mylist += "Vegetable"

 print("\n<<<:::::::::::::::::::::::::::::::Welcome to Hangman:::::::::::::::::::::::::::::::>>>\n")
 print("--->Are you ready to accept the challenge? If you have confidence over your knowledge only then play me!")
 print("--->I am the most challenging game, you have never played before. So be careful!")
 print("--->Come on let's go.........Ready to |")
 print("                                      |")
 print("                                      O")
 print("                                      |")
 print("                                     /|\\")
 print("                                    | | |")
 print("                                      |")
 print("                                     / \\")
 print("                                    |   |\n")

 print("Guess the word: ")
 word_rep = ""
 for letter in word:
    if len(word) > 5:
        if word.index(letter) == len(word)-1 or word.index(letter) == (len(word)-1)//2:
            word_rep += letter
        else:
            word_rep += "*"
    else:
        word_rep += "*"

 print(word_rep)
 print("\nHint: It is a " + mylist)
 incorrect = 0
 tag = ""
 while incorrect < 5:
    ans = input("Guess a letter (in small case): ")
    if ans in "abcdefghijklmnopqrstuvwxyz-" and ans != "":
        if ans in word_rep:
            print("Already guessed! Please guess another letter.....")
            continue
        elif ans in word:
            print("Correct guess! Keep going......")
            for i in range(len(word)):
                word_rep = list(word_rep)
                if word[i] == ans:
                    word_rep[i] = word[i]
                word_rep = "".join(word_rep)
            print("\nWord guessed till now: " + word_rep)
            if word_rep == word:
                tag = "completed"
                break
        else:
            print("Incorrect guess! Try again......")
            incorrect += 1
            print("Hangman status: ", end=" ")
            if incorrect == 1:
                print("|")
                print("                 |")
                print("                 O")
            elif incorrect == 2:
                print("|")
                print("                 |")
                print("                 O")
                print("                 |")
            elif incorrect == 3:
                print("|")
                print("                 |")
                print("                 O")
                print("                 |")
                print("                / \\")
                print("               |   |")
            elif incorrect == 4:
                print("|")
                print("                 |")
                print("                 O")
                print("                 |")
                print("                /|\\")
                print("               | | |")
                print("                 |")
            elif incorrect == 5:
                print("|")
                print("                 |      -->You died!")
                print("                 O")
                print("                 |")
                print("                /|\\")
                print("               | | |")
                print("                 |")
                print("                / \\")
                print("               |   |")
            print("Number of chances left: " + str(5-incorrect))
            print("\nWord guessed till now: " + word_rep)
    else:
        print("Invalid guess! Please, guess a valid letter.........")

 print("The word was: " + word)
 if tag == "completed":
    print("Congratulations! You win the game................")
 else:
    print("Sorry! You lost the game................")
 choice = input("To play again press -y, otherwise any key: ")