#Условие задачи: дано две строки:  s1 и s2.
#Требуется осуществить проверку, может ли строка s1 быть получена путем использования букв из строки s2.
#Одна буква из s2 может быть исопльзована единажды в s1.

def check(s1, s2):
    symbols_count = {}
    for i in s2:
        if i in symbols_count_count:
            symbols_count[i] += 1
        else:
            symbols_count[i] = 1
    
    for i in s1:
        if i in symbols_count and symbols_count[i] > 0:
            symbols_count[i] -= 1
        else:
            return False
    
    for i in symbols_count.values():
        if count > 0:
            return False
    
    return True 

print(check("a", "b"))  
print(check("aa", "ab"))  
print(check("aa", "aab"))