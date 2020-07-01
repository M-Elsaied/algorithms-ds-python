    def sortString(self, s: str) -> str:
        str = list(s)
        maxx = str[0]
        # print(ord(maxx))
        for i in str:
            # print(i,maxx)
            if i > maxx:
                maxx = i
        maxx = ord(maxx) -  ord('a')
        countList = [0] * 26
        for i in str:
            idx = ord(i) - ord('a')
            countList[idx]+=1
        final_list=[]
        while sum(countList) >0:
            # print(countList)
            for i in range(len(countList)):
                if countList[i] ==0:
                    continue
                else:
                    final_list.append(chr(i+97))
                    countList[i]-=1
            # print(countList)
            for i in reversed(range(len(countList))):
                if countList[i] == 0:
                    continue
                else:
                    final_list.append(chr(i+97))
                    countList[i]-=1
            #  print(sum(countList))

        return "".join(final_list)