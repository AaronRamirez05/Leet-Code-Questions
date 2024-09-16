class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = 0
        bool_list = []
        for x in candies:
            if x > max:
                max = x
        
        for x in candies:
            if max <= (x+extraCandies):
                bool_list.append(True)
            else:
                bool_list.append(False)
        
        return bool_list
        