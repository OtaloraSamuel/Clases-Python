#Ejercicio 1
'''
str1 = "James"
print("Original String is", str1)

# Get first character
first_char = str1[0]

# Get middle character
# Calculate index by dividing length by 2
res = len(str1)
middle_index = int(res / 2)
mid_char = str1[middle_index]

# Get last character
last_char = str1[-1]

# Combine characters
res_str = first_char + mid_char + last_char
print("New String:", res_str)
'''
# Ejercicio 2
'''
def get_middle_three_chars(str1):
    print("Original String is", str1)

    # Find middle index
    mi = int(len(str1) / 2)

    # Slice string from (mid - 1) to (mid + 2)
    res = str1[mi - 1:mi + 2]
    print("Middle three chars are:", res)

get_middle_three_chars("JhonDipPeta")
get_middle_three_chars("JaSon")
'''
#Ejercicio 3
'''
def append_middle(s1, s2):
    print("Original Strings are", s1, s2)

    # Find middle index of first string
    mi = int(len(s1) / 2)

    # Get character from 0 to middle index
    x = s1[:mi]
    # Get character from middle index to end
    y = s1[mi:]

    # Combine all three
    res = x + s2 + y
    print("After appending new string in middle:", res)

append_middle("Ault", "Kelly")
'''