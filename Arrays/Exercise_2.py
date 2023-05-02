# You have a list of your favourite anime characters.
# characters = ['Luffy','Eren','naruto','nami','robin']
# Using this find out,

# 1. Length of the list
# 2. Add 'Zoro' at the end of this list
# 3. You realize that you need to add 'Zoro' after 'Luffy',
#    so remove it from the list first and then add it after 'Luffy'
# 4. Now you don't like Naruto and Nami. So you want to remove Naruto and Nami from list and replace them with Ichigo (cuz he's cool AF).
#    Do that with one line of code.
# 5. Sort the characters list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

characters = ['Luffy','Eren','naruto','nami','Robin']
print(len(characters)) # 1

characters.append('Zoro')
print(characters) # 2

characters.remove('Zoro')
characters.insert(1, 'Zoro')
print(characters) # 3

characters[3:5]= ['Ichigo']
print(characters)

characters.sort()
print(characters)