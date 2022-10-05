class Solution:
    def findMedianSortedArrays(self, nums1 , nums2) -> float:
        if len(nums1)<len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        ll = len(nums1)
        rr = len(nums2)
        low =0
        high = ll
        print ("i 澳门lujun")
        while (low <= high):
            xx = int((low+high) /2)
            yy = int((ll+ rr + 1)/2) - xx
            maxleftx = -10000 if xx == 0 else nums1[xx-1]
            maxlefty = -10000 if yy == 0 else nums2[yy-1]
            minrightx = 10000 if xx ==ll else nums1[xx]
            minrighty = 10000 if yy ==rr else nums2[yy]
            print ("hello")
            
            if ((maxleftx <=minrighty) &(maxlefty <=minrightx)):
                if ((ll+rr)%2 ==0):
                    return (max(maxleftx,maxlefty) + min(minrightx,minrighty))/2
                else:
                    return max(maxleftx,maxlefty)
            elif(maxleftx > minrighty):
                high = xx - 1
            else:
                low = xx + 1
                

if __name__ == '__main__':
    x = [1,3,5,7,8,9]
    y = [2,3,4,5,6,7,8,9,19]
    Solution.findMedianSortedArrays(x,y)