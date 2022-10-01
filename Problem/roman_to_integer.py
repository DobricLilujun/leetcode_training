class Solution(object):
    def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        dic = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        flag = False
        for k in range(len(s)):
            if flag:
                flag = False
                continue
            substr = s[k:k+2]
            if substr in dic:
                result += dic[substr]
                flag = True
            else:
                result += value[substr[0]]
        return result


if __name__ == '__main__':
    print (Solution.romanToInt("MCMXCIV"))