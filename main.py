import reader
import SteveControls
import spellCheck

if __name__ == "__main__":
    """Sample Inputs"""
    # find a pig and five cats, kill two cows, and then walk and crouch, and finally feed a cow
    # find forty-five cows and kill ninety-nine pigs and find forty cows
    # kill three-million cats and one billion cows
    # walk 5 and turn 2 and crouch then jump 6
    while True:
        commands = reader.Reader().getDict()
        print(commands)
        # read = dict(reader.Reader().getDict())
        # if not bool(read):
        #     break
        # print(read)



        # Spell Checker Evaluation
        def loopSpellChecker(listOfTypos, trueCommand):
            spellChecker = spellCheck.spellCheck()
            counter = 0
            total = 0
            for typoCommand in listOfTypos:
                spellCheckedCommand = ""
                commandSpellCheck = typoCommand.split(" ")
                for i in range(0, len(commandSpellCheck) - 1):
                    if type(commandSpellCheck[i]) != int:
                        spellCheckedCommand += spellChecker.correction(commandSpellCheck[i]) + " "
                if (commandSpellCheck[len(commandSpellCheck) - 1]):
                    spellCheckedCommand += spellChecker.correction(commandSpellCheck[len(commandSpellCheck) - 1])

                if spellCheckedCommand == trueCommand:
                    counter += 1
                total += 1
            return (counter, total)


        trueCommand = input("enter your command WITHOUT TYPOS: ")
        trueCommand = trueCommand.lower()
        command = trueCommand
        letters = "abcdefghijklmnopqrstuvwxyz"
        singleTypos = []
        doubleTypos = []
        
        for letter in letters:
            for i in range(len(command)):
                if command[i] != " " and command[i].isdigit() != True:
                    command = command[:i] + letter + command[i + 1:]
                    singleTypos.append(command)
                    command = trueCommand

        for letter in letters:
            for i in range(len(command)):
                for j in range(len(command)):
                    if i != j and j > i:
                        if command[i] != " " and command[j] != " " and not command[j].isdigit() and not command[i].isdigit():
                            command = command[:i] + letter + command[i + 1:j] + letter + command[j + 1:]
                            doubleTypos.append(command)
                            command = trueCommand
                    if i != j and i > j:
                        if command[i] != " " and command[j] != " " and not command[j].isdigit() and not command[i].isdigit():
                            command = command[:j] + letter + command[j + 1:i] + letter + command[i + 1:]
                            doubleTypos.append(command)
                            command = trueCommand
        
        singleAccuracy = loopSpellChecker(singleTypos, trueCommand)
        print("One typo:", singleAccuracy, "=", singleAccuracy[0]/singleAccuracy[1])

        doubleAccuracy = loopSpellChecker(doubleTypos, trueCommand)
        print("Two typos:", doubleAccuracy, "=", doubleAccuracy[0]/doubleAccuracy[1])

        print("Total accuracy:", (singleAccuracy[0] + doubleAccuracy[0])/(singleAccuracy[1] + doubleAccuracy[1]))
