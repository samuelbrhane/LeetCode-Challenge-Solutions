class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        hex_chars = "0123456789abcdef"
        result = ""
    
        num &= 0xFFFFFFFF 
        
        while num:
            result = hex_chars[num & 0xF] + result  
            num >>= 4  
        
        return result