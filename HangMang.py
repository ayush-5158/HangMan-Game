import random

words=['minute','practice','policy','police','stock','commission','finance']

word=random.choice(words)

total_chance = 7

total_point=100

guessed_word = '_'*len(word)

while (total_chance!=0):
    print(guessed_word)
    letter = input("Enter the guessed word : ")
    if letter in word:
        for index in range(len(word)):
            if word[index]==letter:
                guessed_word=guessed_word[:index]+letter+guessed_word[index+1:]

        if guessed_word==word:
            print()
            print("-------------You guessed the word right-------------")
            print()
            print("Total point is :",total_point)
            print()
            break

    else:
        total_chance-=1
        total_point=total_point-10
        print("You guessed the wrong letter and now total remaning chances are",total_chance)
if (total_chance==0):
    print("Game Over as your all chances are exchausted...")
    print('The correct word is ', word)

