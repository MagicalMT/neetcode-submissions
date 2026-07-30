class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_left = 1
        k_right = max(piles)
        while k_left < k_right:
            k_mid = k_left + (k_right - k_left) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i / k_mid)
            finish = hours <= h
            if finish:
                k_right = k_mid
            else:
                k_left = k_mid + 1
        return k_left
