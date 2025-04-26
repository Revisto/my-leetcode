class Solution:
    def minWindow(self, s: str, t: str) -> str:
        p1 = 0
        p2 = 0
        min_window = ""
        current_slide = {}
        essential_slide = dict()
        
        def is_t_in():
            for essential_letter in essential_slide:
                if current_slide.get(essential_letter, 0) < essential_slide[essential_letter]:
                    return False
            return True
        
        for letter in t:
            essential_slide[letter] = essential_slide.get(letter, 0) + 1
        while p2 < len(s) or is_t_in() is True:
            if is_t_in() is True:
                if ((min_window != "" and ((p2 - p1) < len(min_window))) or min_window == ""):
                    min_window = s[p1: p2]
                current_slide[s[p1]] -= 1
                p1 += 1
            else:
                current_slide[s[p2]] = current_slide.get(s[p2], 0) + 1
                p2 += 1
            
        return min_window

print(Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))