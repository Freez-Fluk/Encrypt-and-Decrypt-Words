import os
import numpy as np

ch_set = open("char.txt", "r")
ch_array = ch_set.readlines()

def encrypted(ch_array, message, number):
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
                n_cursor = n_cursor + 1
                m_cursor = (n_cursor + number) - 1             
                if m_cursor >= number:
                    t_cursor = (m_cursor%26)
                    result_ms[cursor] = ch_array[t_cursor]
                    m_cursor = 0
                cursor += 1
    return result_ms
        
print("Input word : ")
ms = input()
print("Enter number of encrypt : ")
number = input()
test = encrypted(ch_array, ms, number)
print(test)