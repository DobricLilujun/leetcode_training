class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_index = {}
        start_window_index = 0
        max_lenth = 0
        i = 0
        for c in s:
            if c in last_index:
                start_window_index = max(start_window_index, last_index[c]+1)
            max_lenth = max(max_lenth,i-start_window_index+1)
            last_index[c] = i
            i = i+1
        return max_lenth