class Solution:
    def intToRoman(self, num: int) -> str:
        val=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        a=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        R=""
        i=0
        while num>0:
            count=num//val[i]
            R+=a[i]*count
            num-=val[i]*count
            i+=1
        return R               