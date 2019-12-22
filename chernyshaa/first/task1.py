'''
Вивести усі великі букви, які містяться в тексті, введеному користувачем
'''

text=str(input("Введіть будь-який текст: "))
words=text.split()
i=0
bigletter=[]
for word in  words :
    for letter in word:
        if letter.upper() == True:
            bigletter[i]=len.words
            i+=1
