class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                count += 1
                flowerbed[0] = 1
        else:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                count += 1
                flowerbed[0] = 1
            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                count += 1
                flowerbed[-1] = 1

            for i in range(1, len(flowerbed) - 1):
                prev = flowerbed[i - 1]
                curr = flowerbed[i]
                succ = flowerbed[i + 1]
                if prev == 0 and curr == 0 and succ == 0:
                    count += 1
                    flowerbed[i] = 1

        if count >= n:
            return True
        else:
            return False
