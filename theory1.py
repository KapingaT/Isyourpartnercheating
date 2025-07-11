class Theory_one(): #Father class
    def __init__(cheat,frequent_messages,current_messages):
        cheat.frequent_messages=int(frequent_messages)
        cheat.current_messages=int(current_messages)


class Theory_two(Theory_one): #Mother class
    def __init__(cheat,frequent_messages,current_messages,cfollowing_list,ofollowing_list):
        super().__init__(int(frequent_messages),int(current_messages))
        cheat.cfollowing_list=int(cfollowing_list)
        cheat.ofollowing_list=int(ofollowing_list)


class Theory_three(Theory_two): #Oldest sibling
    def __init__(cheat, frequent_messages, current_messages, cfollowing_list, ofollowing_list,cmeet_freq,omeet_freq):
        super().__init__(int(frequent_messages), int(current_messages), int(cfollowing_list), int(ofollowing_list))
        cheat.cmeet_freq=int(cmeet_freq)
        cheat.omeet_freq=int(omeet_freq)


    def model(cheat):
        count=0
        if cheat.current_messages<cheat.frequent_messages:
            count+=1
        elif cheat.cfollowing_list>cheat.ofollowing_list:
            count+=1
        elif cheat.cmeet_freq<cheat.ofollowing_list:
            count+=1
        
        if count>2:
            print("\nHe might be cheating on you, but give him a chance.")
        elif count>1:
            print("\nMaybe he might be cheating, 'if you're guessing his cheating'")
        else:
            print("\nYou're safe for... now")

def main():
    print("Only insert numbers like 1-9per day or 1-1000per day")

    fm=input("\n\nHow often did he/she message you in the past: ")
    cm=input("How often does he or she message you now: ")
    if fm>cm:
        print("find GOD my friend").rjust(40)
    else:
        print(" ")
    cf=input("What is his/her current following count: ")
    of=input("What was their old following count: ")
    if cf>of:
        print("see what youve become checking follwer list").rjust(40)
    cm=input("how fequent is she/he meeting up with you now: ")
    om=input("how frequent did he/she use to meet up with you: \n") 
    if cm>om:
        print(" STAND UP this is not you").rjust(40)
    questions=Theory_three(fm,cm, cf, of, cm, om,
                          print("Helping others is our mission"))
    
    questions.model()

if __name__=="__main__":
    main()

