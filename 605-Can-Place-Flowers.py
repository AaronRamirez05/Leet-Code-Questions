class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ones = 0
        zeros = 0
        validcheck = False
        checkIndex = 0

        #Calculate numbers of 1's and zeros
        for x in flowerbed:
            if x == 1:
                ones += 1
            else:
                zeros += 1
        
        #Checks whether the current flowerbed number 
        if ones+n > zeros+1:
            return False

        #if flowerbed is only 1
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True

        for i in range(len(flowerbed)-1):
            if n == 0:
                break
            if i == 0:
                if flowerbed[i+1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n-=1
            if i > 1:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n -= 1
            if i == len(flowerbed)-2:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i+1] = 1
                    n -= 1
    
        if n == 0:
            return True
        else:
            return False
