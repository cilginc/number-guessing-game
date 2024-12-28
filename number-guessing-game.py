from random import randint
low = 1
high = 100
answer = randint(low, high)

def difficulty_level():
    while True:
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        difficult = input("Please select the difficulty level:")
        if difficult == "1":
            print("Great! You have selected the Easy difficulty level.")
            return 10
        elif difficult == "2":
            print("Great! You have selected the Medium difficulty level.")
            return 5
        elif difficult == "3":
            print("Great! You have selected the Hard difficulty level.")
            return 3
        else:
            print("Please give number for difficulty level!")


def main():
    print(f"I'm thinking of a number between {low} and {high}.")
    level = difficulty_level()
    tries = 0
    while True:
        userinput = int(input("Enter your guess:"))
        if tries == level:
            print("You lose!")
            break
        elif answer == userinput:
            print(f"Congratulations! Answer was {answer}")
            print(f"You guessed the correct number in {tries} attempts..")
            break
        elif userinput > answer:
            print(f"Incorrect! The number is less than {userinput}.")
            tries += 1
        else:
            print(f"Incorrect! The number is greater than {userinput}..")
            tries += 1

if __name__ == "__main__":
    main()