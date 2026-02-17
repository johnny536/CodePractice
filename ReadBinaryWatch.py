class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hour0 = ["0:"]
        hour1 = ["8:","4:","2:","1:"]
        hour2 = ["10:","9:","6:","5:","3:"]
        hour3 = ["11:","7:"]

        min0 = ["00"]
        min1 = ["01","02","04","08","16","32"]
        min2 = ["48","40","36","34","33","24","20","18","17","12","10","09","06","05","03"]
        min3 = ["56","52","50","49","44","42","41","38","37","35","28","26","25","22","21","19","14","13","11","07"]
        # missing 27 before
        min4 = ["58","57","54","53","51","46","45","43","39","30","29","23","15","27"]
        min5 = ["59","55","47","31"]
        
        if turnedOn == 9 or turnedOn == 10:
            return []

        elif turnedOn == 0:
            return ["0:00"]

        elif turnedOn == 1:
            return ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]       

        elif turnedOn == 8:
            res = []
            for i in hour3:
                for j in min5:
                    res.append(i+j)

            return res

        elif turnedOn == 7:
            res = []
            for i in hour3:
                for j in min4:
                    res.append(i+j)

            for i in hour2:
                for j in min5:
                    res.append(i+j)
            
            return res

        elif turnedOn == 6:
            res = []
            for i in hour3:
                for j in min3:
                    res.append(i+j)
            
            for i in hour2:
                for j in min4:
                    res.append(i+j)
            
            for i in hour1:
                for j in min5:
                    res.append(i+j)
            
            return res

        elif turnedOn == 5:
            res = []
            for i in hour3:
                for j in min2:
                    res.append(i+j)
            for i in hour2:
                for j in min3:
                    res.append(i+j)
            for i in hour1:
                for j in min4:
                    res.append(i+j)
            for i in hour0:
                for j in min5:
                    res.append(i+j)
            return res
        
        elif turnedOn == 4:
            res = []
            for i in hour3:
                for j in min1:
                    res.append(i+j)
            for i in hour2:
                for j in min2:
                    res.append(i+j)
            for i in hour1:
                for j in min3:
                    res.append(i+j)
            for i in hour0:
                for j in min4:
                    res.append(i+j)
            return res

        elif turnedOn == 3:
            res = []
            for i in hour3:
                for j in min0:
                    res.append(i+j)
            for i in hour2:
                for j in min1:
                    res.append(i+j)
            for i in hour1:
                for j in min2:
                    res.append(i+j)
            for i in hour0:
                for j in min3:
                    res.append(i+j)

            return res

        elif turnedOn == 2:
            res = []
            for i in hour2:
                for j in min0:
                    res.append(i+j)
            for i in hour1:
                for j in min1:
                    res.append(i+j)
            for i in hour0:
                for j in min2:
                    res.append(i+j)
            return res

        return []