class Solution(object):
    def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """
        right = len (s)-1
        
        flag = False
        for i in range(right,-1,-1):
            if s[i]==' ':
               if flag:
                   left = i
                   return (right - left)
            else:
                if not flag:
                    right = i
                    flag = True

if __name__ == "__main__":
    print (Solution.lengthOfLastWord("Hello world"))