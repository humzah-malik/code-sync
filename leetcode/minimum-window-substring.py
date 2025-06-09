class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0

        if len(s) < len(t):
            return ""

        req = Counter(t)
        window = defaultdict(int)
        req2 = len(req) # NOT duplicates
        min_window = float("inf")
        start_index = 0
        formed = 0 # tracking length of unique chars within a window

        while right < len(s):
            c = s[right]
            window[c] += 1

            if c in req and window[c] == req[c]:
                formed += 1
            
            if formed == req2:
                while left <= right and formed == req2:
                    if (right - left + 1) < min_window:
                        min_window = right - left + 1
                        start_index = left

                    d = s[left]
                    window[d] -= 1
                    if d in req and window[d] < req[d]:
                        formed -= 1
                    left += 1

            right += 1

        if min_window == float("inf"):
            return ""
        else:
            return s[start_index:start_index + min_window]