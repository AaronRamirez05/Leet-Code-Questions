class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a = len(str1)
        b = len(str2)
        
        #switch strings around if 2nd is bigger than first
        if a < b:
            temp = a
            a = b
            b = temp
            temp = str1 
            str1 = str2
            str2 = temp

        #Check if str2 is the same 
        if str1+str2 != str2+str1:
            return ""

        remainder= a%b
        if remainder == 0:
            index = b
        else:
            index = 0
      
        #calculates GCD
        while remainder != 0:
            if a%b == 0:
                break
            remainder = a%b
            a = b
            b = remainder
            index = b

        merged = ""
        if index > 0:
            if len(str1) > len(str2):
                for i in range(index):
                    merged += str1[i]
            elif len(str1) < len(str2):
                for i in range(index):
                    merged += str2[i]
            else:
                for i in range(index):
                    merged += str1[i]
        else:
            return ""
        
        return merged
        

            
