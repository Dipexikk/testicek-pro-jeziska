def pocet_dvojic(cisla, n, cil):
    pocet = 0
    
    for i in range(0, n - 1): 
        
        for j in range(i + 1, n):
            
            soucet = cisla[i] + cisla[j]
            
            if soucet == cil:
                pocet = pocet + 1
                
    return pocet

print("Test 1:", pocet_dvojic([1, 4, 2, 3], 4, 5))    # Očekávám 2
print("Test 2:", pocet_dvojic([2, 2, 2], 3, 4))       # Očekávám 3
print("Test 3:", pocet_dvojic([-1, 0, 1, 2], 4, 1))   # Očekávám 2
print("Test 4:", pocet_dvojic([1, 2, 3], 3, 9))       # Očekávám 0
print("Test 5:", pocet_dvojic([], 0, 5))              # Očekávám 0
print("Test 6:", pocet_dvojic([5], 1, 10))            # Očekávánm 0
