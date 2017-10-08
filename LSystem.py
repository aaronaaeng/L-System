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
                a = self.ruleSet[j].get_a()
                if a == currentCharacter :
                    replacementStr = self.ruleSet[j].get_b()
                    break

            nextGen += replacementStr

        self.sentence = str(nextGen)

        self.generationInt += 1

    def get_sentence (self):
        return self.sentence

    def get_generation (self):
        return self.generationInt
