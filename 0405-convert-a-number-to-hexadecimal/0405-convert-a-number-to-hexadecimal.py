class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num = int(2 ** 32 + num)
        elif(num == 0):
            return "0"

        hexString = ""

        while(num != 0):

            remainder = num % 16
            
            if(remainder < 10):
                hexString += str(remainder)
            elif(remainder == 10):
                hexString += 'a'
            elif(remainder == 11):
                hexString += 'b'
            elif(remainder == 12):
                hexString += 'c'
            elif(remainder == 13):
                hexString += 'd'
            elif(remainder == 14):
                hexString += 'e'
            elif(remainder == 15):
                hexString += 'f'

            num //= 16
        
        return hexString[-1::-1]