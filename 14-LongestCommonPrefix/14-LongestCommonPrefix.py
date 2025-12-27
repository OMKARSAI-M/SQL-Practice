# Last updated: 12/26/2025, 6:37:26 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        dict_1 = {i:{item:0} for i, item in enumerate(strs[0])}
        for i in range(len(strs)):
            index = 0
            for j,element in enumerate(strs[i]):
                if index < len(dict_1):
                    if element in dict_1[j]:
                        index += 1
                        dict_1[j][element] += 1
                    else:
                        break
        temp = []
        for key, value in dict_1.items():
            for char, val in value.items():
                if val == len(strs):
                    temp.append(char)
                else:
                    break
        if temp is not None:
            return "".join(temp)
        else:
            return ""

                
        