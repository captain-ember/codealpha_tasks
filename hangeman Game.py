import random
word_list = ["apple", "peace", "laugh", "fruit", "route"]

random_word = random.choice(word_list)

print("Hangemen Game")
print('''----Rules----
1. The Word Contains 5 Letters
2. × Means the wrong Letter
3. ● Means Right Letter But Worng Place
4. √ Means Right Letter at The Right Place\n\n''')

Right=['√','√','√','√','√']
word=[]
for w in random_word:
    word.append(w)

count=0
con=False  
for x in range(0,6):
    RW=[]
    for i in range(0,5):
        temp=input(f" Enter Letter {i+1}  :")
        if temp==word[i]:
            RW.append("√")
        elif temp in word:
            RW.append("●")
        else:
            RW.append("×")

    count+=1
    print("\n",RW,"\n")
    if RW==Right:
        print("You Guessed The Word in -",count,"Attempts")
        con = True
        break

if con==False:
    print("You Loose , The Word is - ",random_word)
