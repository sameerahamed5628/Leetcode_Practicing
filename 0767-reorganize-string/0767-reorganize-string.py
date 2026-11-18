class Solution(object):
    def reorganizeString(self, s):
        build={}
        for x in s:
            if x in build:
                build[x]+=1
            else:
                build[x]=1

        threshold=(len(s)+1)//2
        if max(build.values())>threshold:
            return ""
        
        new={}
        while build:
            maax=max(build,key=build.get)
            new[maax]=build[maax]
            del build[maax]

        out=[]
        while new:
            best=None
            for z in new:
                if out and z==out[-1]:
                    continue
                if best is None or new[z]>new[best]:
                    best=z
            out.append(best)
            new[best]-=1
            if new[best]==0:
                del new[best]
        return "".join(out)