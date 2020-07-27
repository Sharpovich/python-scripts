'''
Move the first letter of each word to the end of it, 
then add "ay" to the end of the word. 
Leave punctuation marks untouched.
Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''

# Solution:
def pig_it(text):
    strr= text.split(" ")
    lst=[]
    lst2=["!",".","?","|"]
    for i in strr:
        if i in lst2:
            lst.append(i)
            break
        else:
            i = str(i[1:] + i[0])
            lst.append(str(i) + "ay")
    return " ".join(lst)
