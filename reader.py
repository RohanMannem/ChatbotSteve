import nltk
from collections import defaultdict
import word2int as convert
import inflect
import spellCheck
import warnings
import spacy


warnings.filterwarnings("ignore")
nlp = spacy.load('en_coref_sm') # load small size coreference resolution model 


# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# walk 10 --> walk 10 times
# turn 3 --> turn 3 times to the right

class Reader:
    def __init__(self):
        command = input("enter your command: ")
        articles = ["them", "it"]

        command = nlp(command)  
        # print("Has coref: ", command._.has_coref)

        if command._.has_coref: # check if have coreference 
            command = str(command._.coref_resolved) # coreference resolution
        else:
            command = str(command)

        command.lower()


        spellChecker = spellCheck.spellCheck()
        spellCheckedCommand = ""
        commandSpellCheck = command.split(" ")
        for i in range(0, len(commandSpellCheck) - 1):
            if type(commandSpellCheck[i]) != int:
                spellCheckedCommand += spellChecker.correction(commandSpellCheck[i]) + " "
        if (commandSpellCheck[len(commandSpellCheck) - 1]):
            spellCheckedCommand += spellChecker.correction(commandSpellCheck[len(commandSpellCheck) - 1])

        command = "I want you to " + spellCheckedCommand
        self.tags = command
        self.currentVerb = ""
        self.currentNum = 1
        self.flag = 0
        self.basic = 0
        self.basicWord = ""
        self.result = defaultdict(list)

    def getDict(self):
        p = inflect.engine()
        tokens = nltk.word_tokenize(self.tags)
        tags = nltk.pos_tag(tokens)

        basicActions = ["walk", "jump", "turn", "crouch", "attack"]
        for word, POS in tags:
            if word not in basicActions:
                s1 = set(word.split("-"))
                s2 = set(convert.american_number_system.keys())
                if s1 & s2:
                    self.currentNum = convert.word_to_num(word)
                    continue
                if word in convert.american_number_system.keys():
                    self.currentNum = convert.american_number_system[word]

                if POS == "VB" or POS == "VBD":
                    self.flag = 1
                    self.currentVerb = word
                if POS == "CD":
                    try:
                        self.currentNum = convert.word_to_num(word)
                    except ValueError:
                        self.currentNum = 1
                if self.flag == 1 and (POS == "NN" or POS == "NNS"):
                    if p.singular_noun(word):
                        self.result[self.currentVerb].append([p.singular_noun(word), self.currentNum])
                    else:
                        self.result[self.currentVerb].append([word, self.currentNum])
                    self.currentNum = 1
            elif word in basicActions:
                self.basic = 1
                self.basicWord = word
                self.result[word] = [1]
            if self.basic == 1:
                if POS == "CD":
                    self.result[self.basicWord] = (convert.word_to_num(word))
                self.basic == 0
        return dict(self.result)
