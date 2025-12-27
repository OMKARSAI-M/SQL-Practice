# Last updated: 12/26/2025, 6:37:27 PM
class Solution:
    def isValid(self, s: str) -> bool:
        left_0 = s.count("(")
        left_1 = s.count("[")
        left_2 = s.count("{")
        right_0 = s.count(")")
        right_1 = s.count("]")
        right_2 = s.count("}")
        if left_0 == right_0 and left_1 == right_1 and left_2 == right_2:
            temp_list = []
            str_list = [ item for item in s]
            for i in range(len(str_list)):
                if str_list[i] == "(" or str_list[i] =="[" or str_list[i] == "{":
                    temp_list.append(str_list[i])
                else:
                    if str_list[i] == ")":
                        if not temp_list:
                            return False
                        if temp_list[-1] == "(":
                            temp_list.pop()
                        else:
                            return False
                    elif str_list[i] == "]" :
                        if not temp_list:
                            return False
                        if temp_list[-1] == "[":
                            temp_list.pop()
                        else:
                            return False
                    elif str_list[i] == "}":
                        if not temp_list:
                            return False
                        if temp_list[-1] == "{":
                            temp_list.pop()
                        else:
                            return False
                    else:
                        return False
                    
            if temp_list:
                return False
            else:
                return True
        else:
            return False