import Rule

class LSystem:
    sentence = None
    ruleSet = None
    generationInt = None

    def __init__(self, axiom, rules):
        self.sentence = axiom
        self.ruleSet = rules
        self.generationInt = 0

    def generate (self):
        nextGen = ""

        for i in range (0, len (self.sentence)):
            currentCharacter = self.sentence[i]
            replacementStr = "" + currentCharacter

            for j in range (0, len (self.ruleSet)):
                a = self.ruleSet[j].getA()
                if a == currentCharacter :
                    replacementStr = self.ruleSet[j].getB()
                    break

            nextGen += replacementStr

        self.sentence = str(nextGen)

        self.generationInt += 1

    def getSentence (self):
        return self.sentence

    def getGeneration (self):
        return self.generationInt

