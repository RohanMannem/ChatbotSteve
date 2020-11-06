import nltk
from collections import defaultdict
import word2int as convert
import inflect


# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

class Reader:
    def __init__(self):
        command = input("enter your command: ")
        command = command.lower()
        self.tags = command
        self.currentVerb = ""
        self.currentNum = 1
        self.flag = 0
        self.result = defaultdict(list)

    def getDict(self):
        p = inflect.engine()
        tokens = nltk.word_tokenize(self.tags)
        tags = nltk.pos_tag(tokens)
        actions = ["walk", "jump", "turn", "crouch"]
        for noun, i in tags:
            if noun not in actions:
                s1 = set(noun.split("-"))
                s2 = set(convert.american_number_system.keys())
                if s1 & s2:
                    self.currentNum = convert.word_to_num(noun)
                    continue
                if noun in convert.american_number_system.keys():
                    self.currentNum = convert.american_number_system[noun]
                if i == "VB" or i == "VBD":
                    self.flag = 1
                    self.currentVerb = noun
                if i == "CD":
                    try:
                        self.currentNum = convert.word_to_num(noun)
                    except ValueError:
                        self.currentNum = 1
                if self.flag == 1 and (i == "NN" or i == "NNS"):
                    if p.singular_noun(noun):
                        self.result[self.currentVerb].append([p.singular_noun(noun), self.currentNum])
                    else:
                        self.result[self.currentVerb].append([noun, self.currentNum])
                    self.currentNum = 1
            elif noun in actions:
                self.result[noun] = []
        return self.result
