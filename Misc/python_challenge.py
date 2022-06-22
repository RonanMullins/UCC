def main(): #level 1
    
    
    #raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    raw ="http://www.pythonchallenge.com/pc/def/map.html"
    result = ""
    
        
    for c in raw:
            
            if c >= 'a' and c <= 'z':
                
                result += chr(((ord(c) + 2) - ord('a')) % 26 + ord('a'))
            
            else:
                
                result += c

    print(result)


if __name__ == "__main__":
    
    main()
 
