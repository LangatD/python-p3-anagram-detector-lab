# your code 
class Anagram():
    def __init__(self,wordlist):
        self .wordlist = wordlist.lower()
    def match(self,word):
        sorted_word = sorted(self.wordlist)
        result = []
        for item in word:
            if sorted(item.lower()) == sorted(self.wordlist) and item.lower() != self.wordlist:
                result.append(item)
        return result
