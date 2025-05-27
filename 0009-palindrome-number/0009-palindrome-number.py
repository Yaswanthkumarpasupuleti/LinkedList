class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_string = str(x)
        reversed_num = num_string[::-1]
        if num_string == reversed_num:
            return True
        return False
        