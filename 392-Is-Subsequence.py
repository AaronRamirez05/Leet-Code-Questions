class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        testString = ""

        #check if string is empty
        if len(s) == 0:
            return True
        
        #check if string is an individual letter
        if len(s) == 1:
            if t.find(s) == True:
                return True
            else:
                return False

        #check if string contains substring with security measure in the case its the last character
        for i in range(len(t)):
            if len(testString) == len(s):
                return True

            if t[i] == s[index]:
                print(s[index])
                testString += s[index]
                index += 1
            
        if len(testString) == len(s):
                return True
        else:
            return False