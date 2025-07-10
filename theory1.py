class Theory_one():
    def __init__(cheat,frequent_messages,current_messages):
        cheat.frequent_messages=frequent_messages
        cheat.current_messages=current_messages

    def model(cheat):
        if cheat.current_messages<cheat.frequent_messages:
            print("He might be cheating on you, but give him a chance.")
        elif cheat.current_messages==cheat.frequent_messages:
            print("There is a 50/50 chance.")
        else:
            print("He is definetly not cheating ")

def main():
    print("Only insert numbers like 1-9per day or 1-1000per day")
    theory_one=Theory_one(input("How often did he/she use to message you: "),input("How often does he or she message you now: "))
    theory_one.model()

if __name__=="__main__":
    main()