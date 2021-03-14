import os

ch_set = open("char.txt", "r")
ch_array = ch_set.readlines()
    
def decrypted(ch_array, message, number):
    number = int(number)
    ms = [char for char in message]
    result_ms = [None] * len(ms)
    cursor = 0
    n_cursor = 0
    m_cursor = 0
    t_cursor = 0
    for l in ms:
        for k in ch_array:
            if len(set(k)) == len(set(l)):
                n_cursor += 1
                m_cursor = 25 - (abs(n_cursor - number))
                result_ms[cursor] = ch_array[m_cursor]
                m_cursor = 0
                cursor += 1                
    return result_ms
      
print("Input word : ")
ms = input()
print("Enter number of encrypt : ")
number = input()
test = decrypted(ch_array, ms, number)
print(test)