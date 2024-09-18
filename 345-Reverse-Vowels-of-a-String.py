class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        #grabs all vowels

        for i in range(len(s)):
            if s[i] == 'A' or s[i] == 'a' or s[i] == 'E' or s[i] == 'e' or s[i] == 'I' or s[i] == 'i' or s[i] == 'O' or s[i] == 'o' or s[i] == 'U' or s[i] == 'u':
                vowels.append(s[i])

        vowels.reverse()
        index = 0
        sol = ""

        #switches vowels
        for i in range(len(s)):
            if s[i] == 'A' or s[i] == 'a' or s[i] == 'E' or s[i] == 'e' or s[i] == 'I' or s[i] == 'i' or s[i] == 'O' or s[i] == 'o' or s[i] == 'U' or s[i] == 'u':
                sol += vowels[index]
                index += 1
            else:
                sol += s[i]
        
        return sol