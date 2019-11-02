class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        a = 0
        for i in coordinates:
            b = i[0] / i[1]
            if a == 0:
                a = b

            if a != b:
                return False


