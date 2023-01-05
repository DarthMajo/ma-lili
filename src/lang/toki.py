#Generator for creating toki-pona-ish words

class TokiPona:
    def __init__(self):
        self.allowedSyllables = self.AllowableSyllables()

    def AllowableSyllables():
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
