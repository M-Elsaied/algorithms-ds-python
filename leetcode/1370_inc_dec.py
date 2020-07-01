    def sortString(self, s: str) -> str:
        ### Why are we searching for Max? There is no need. 
        ### The problem constraints say that all letters are small
        str = list(s)
        maxx = str[0]
        # print(ord(maxx))
        for i in str:
            # print(i,maxx)
            if i > maxx:
                maxx = i
        ### Max is not even being used. 
        maxx = ord(maxx) -  ord('a')
        countList = [0] * 26
        for i in str:
            idx = ord(i) - ord('a')
            countList[idx]+=1
        final_list=[]
        
        """ The Condition on this while loop is a dangerous one
            Calculating the sum of a list takes O(n) under the hood 
            The while loop loops n times, so total is O(n2)
            you can say The following
                while len(final_list) < len(s)
           
        """
        while sum(countList) >0:
            # print(countList)
            for i in range(len(countList)):
                """
                    When you get an if else statement like this write it as follows
                    if countList !=0:
                        final_list.append(chr(i+97))
                        countList[i]-=1
                    
                    So you don't need an else or a continue
               """     
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
