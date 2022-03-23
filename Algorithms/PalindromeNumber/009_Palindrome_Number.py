# Source : https://leetcode.com/problems/palindrome-number
# Author : Md. Shohanur Islam Sobuj
#  Time : 03/23/2022 13:46

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        reverse_x = 0
        temp = x
        while temp:
            reverse_x *= 10
            reverse_x += temp % 10
            temp /=10
        return x==reverse_x
    
if __name__ == "__main__":
    print Solution().isPalindrome(132321)
