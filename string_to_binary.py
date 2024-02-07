class low_high_low:
    def __init__(self): # constructor
        pass
    def to_8bit_binary(self,num):
        binary_str=''
        # print("Ascii = ",num)
        while num>0:
            binary_str=str(num%2)+binary_str
            num=int(num/2)
            # print(num)
        # print("\n\nBinary ",binary_str)
        while len(binary_str)<8:
            binary_str='0'+binary_str
        return binary_str
    def low_high(self,str):
        binary_val_sum=''
        for char in str:
            asci_val=ord(char)
            binary_val_sum+=self.to_8bit_binary(asci_val)
        return binary_val_sum
    def to_string(self,binary_str):
        # asci_char=0
        # binary_len=len(binary_str)
        # alpha=0
        # # for char in binary_str:
        # int_val=int(binary_str)
        # while int_val>0:
        #     asci_char+=(int_val%10)*2**alpha
        #     alpha=alpha+1
        #     int_val=int(int_val/10)
        return chr(int(binary_str,2))
    def high_low(self,binary_str):
        ascii_string=''
        for i in range(0,len(binary_str),8):
            binary_8bit=binary_str[i:i+8]
            # print(binary_8bit,len(binary_8bit))
            # print(int(binary_str,2))
            # ascii_string+=self.to_string(binary_8bit)
            ascii_string+=chr(int(binary_8bit,2))
        return ascii_string
c1=low_high_low()
binary=c1.low_high("My Name is Tamal Mallick")
print("Binary \n>>",binary)
str=c1.high_low(binary)
print("Decimal\n>>",str)

