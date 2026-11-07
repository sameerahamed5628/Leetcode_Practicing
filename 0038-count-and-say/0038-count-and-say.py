class Solution(object):
    def countAndSay(self, n):
        first="1"
        for x in range(n-1):
            RLE=[]
            count=1
            for i in range(1,len(first)):
                if first[i]==first[i-1]:
                    count+=1
                else:
                    RLE.append(str(count))
                    RLE.append(first[i-1])
                    count=1
            RLE.append(str(count))
            RLE.append(first[-1])
            first= "".join(RLE)
        return first