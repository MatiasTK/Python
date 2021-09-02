""" def firstNotRepeatingCharacter(s):
    for i in range(len(s)):
        repeated = False
        for j in range(len(s)):
            if s[i] == s[j] and j != i:
                repeated = True
        
        if repeated == False:
            return s[i]

    return "_" """

#Forma correcta:

def first_non_repeating_character(s):
  ordenado = []
  dic = {}
  for char in s:
    if char in dic:
      dic[char] += 1
    else:
      dic[char] = 1 
      ordenado.append(char)
  for c in ordenado:
    if dic[c] == 1:
      return c
  return "_"

                
s = "abacabad"

print(first_non_repeating_character(s))

