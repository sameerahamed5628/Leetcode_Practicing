class Solution(object):
    def compress(self, chars):
        new=[]
        i=0
        while i<len(chars):
            s=chars[i]
            count=0
            while i<len(chars) and chars[i]==s:
                count+=1
                i+=1
            new.append(s)
            if count>1:
                new+=list(str(count))
        chars[:]=new
        return len(new)
            

        
        
                

