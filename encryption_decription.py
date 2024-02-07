class BasicCryptology:
    def __init__(self,start,end) -> None:
        self.start=ord(start)
        self.end=ord(end)  
        self.k=self.end-self.start+1  #   no of characters
    def Encription(self,string,key):
        # print(string,self.k)
        charmap={}
        cyphermap={}
        cypher=''        
        # for ch in string:
        #     val=ord(ch)
        #     charmap[ch]=val-self.start
        # print(charmap)
        for ch in string:
            charmap[ch]=((ord(ch)-self.start)+key)%self.k + self.start
        # print(charmap)
        # convertiong character to cypher     
        for ch in string:
            cych=chr(charmap[ch])
            # print(cych)
            cyphermap[ch]=cych
            cypher+=cyphermap[ch]
        # print(cypher)
        return cypher,key
    
    def Decription(self,cypher,key):
        string=''
        stringmap={}
        for cy in cypher:
            stringmap[cy]=chr(((ord(cy)-self.start)-key)%self.k+self.start)
            string+=stringmap[cy]
        return string

ende=BasicCryptology(start=chr(0),end=chr(126))
cypher,key=ende.Encription('TAMAL MaLLIcK700 88',18)
print("Encripted = ",cypher)
string=ende.Decription(cypher,key)
print("Decripted = ",string)


