#Generator for creating toki-pona-ish words
import random

class TokiPona:
    def __init__(self):
        self.syls = self.AllowableSyllables()

    def AllowableSyllables(self):
        """Generates a list of all allowed syllables in toki pona.
        
        Returns:
            A list of strings of all allowed syllables in toki pona.
        """
        allowed = []
        vowels = ['a', 'e', 'i', 'u', 'o']
        cons = ['j', 'k', 'l', 'm', 'n', 'p', 's', 't', 'w']

        #Generate all syllables without an onset
        for v in vowels:
            allowed.append(str(v))
            allowed.append(str(v) + 'n')

        #Generate all allowable syllables with an onset
        for c in cons:
            for v in vowels:
                #Reject any forbidden syllables
                if(v == 'i'):
                    if(c == 'j' or c == 't'):
                        continue
                elif(c == 'w'):
                    if(v == 'o' or v == 'u'):
                        continue
                
                #Add the allowable syllables
                allowed.append(str(c) + str(v))
                allowed.append(str(c) + str(v) + 'n')

        return allowed

    def GenerateWord(self):
        """Generates a string based on toki pona stats.
        
        Returns:
            A string that resembles a toki pona word.
        """
        #Init variables
        syllableCount = -1
        randomNumber = random.randint(0, 123)
        word = ""

        #Toki pona has 124 words, 26 of 1 syl, 85 of 2 syls, and 13 of 3 syls
        if(randomNumber < 26):
            syllableCount = 1
        elif(randomNumber >= 110):
            syllableCount = 3
        else:
            syllableCount = 2

        #Append random syllables
        for _ in range(syllableCount):
            word += self.syls[random.randint(0, len(self.syls))]

        return word