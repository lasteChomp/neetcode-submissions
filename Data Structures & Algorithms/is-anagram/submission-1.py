class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        bool_values = {"True": 0, "False": 0}

        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1
        
        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1

        for key in s_dict:
            if key in t_dict and s_dict[key] == t_dict[key]:
                bool_values["True"] += 1

        if len(s_dict) == len(t_dict) and len(s_dict) == bool_values["True"]:
            return True
        return False