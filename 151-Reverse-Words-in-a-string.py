class Solution:
    def reverseWords(self, s: str) -> str:
        splitS = s.split()
        
        splitS.reverse()
        reversedWord = ""
        
        for i in range(len(splitS)):
            reversedWord += splitS[i]
            if i < len(splitS)-1:
                reversedWord += " "

        return reversedWord