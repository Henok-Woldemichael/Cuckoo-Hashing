class CuckooHash:
    def __init__(self,data):
        self.data = data
        self.size = len(data)
        self.hashArrayOne = [None] * self.size * 2
        self.hashArrayTwo = [None] * self.size * 2

    def getKey(self,val,diction):
        for key, value in diction.items():
            if value == val:
                return key
        return "Key Does Not Exist"
       
    def cuckoo(self):
        counter = 0
        for key in self.data:
            if(isinstance(key,int) == False):
                for element in key:
                    letter = ord(element)
                    counter+= letter
                indexHashOne = counter % self.size
            else:
                indexHashOne = key % self.size
            if(self.hashArrayOne[indexHashOne] != None):
                hold = self.hashArrayOne[indexHashOne]
                self.hashArrayOne.pop(indexHashOne)
                self.hashArrayOne[indexHashOne] = self.data[key]
                #Funtion returns the key based on the value
                deletedKey = self.getKey(hold,self.data)
                indexHashTwo = (hash(deletedKey) * 100) % self.size
                self.hashArrayTwo[indexHashTwo] = self.data[deletedKey]
           
            else:
                self.hashArrayOne[indexHashOne] = self.data[key]
       
        print(self.hashArrayOne)
        print(self.hashArrayTwo)