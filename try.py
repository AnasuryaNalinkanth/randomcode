import random
a=input("Are you ready for a game of Hangman?[Yes/No]: ")
def check(a,b):
    indices=[]
    for k ,c in enumerate(a):
        if c == b:
            indices.append(k)
    return indices
if a.lower()=="yes":
    i=input("Select a topic:[Movies, Games, Places, Celebrities, Books]: ")
    m=['Spider-Man','Iron Man','Titanic','Avatar','The Matrix','John Wick','The Avengers','The Batman','The Super Mario Bros.','Puss in Boots: The Last Wish','Minions','Wreck-It Ralph']
    g=['Fortnite','PUBG','Valorant','Batman Arkham Knight','Red Dead Redemption 2','The Last of Us','Dying Light',"Assassin's Creed",'DOOM','Grand Theft Auto','Tomb Raider','Halo']
    p=['Dubai','Paris','Tokyo','Berllin','London','Mumbai','New Delhi','Hong Kong','Thailand']
    c=['Ronaldo','Messi','Leonardo DiCaprio','Johnny Depp','Kylie Jenner','Roger Federer','Kanye West','Neymar','Lebron James','Dywane Johnsson','Howard Stern']
    b=['The Diary of a Wimpy Kid','The Great Gatsby','The Catcher in the Rye','To Kill a Mockingbird','The Lord of the Rings','Invisible Man','Great Expectations',"Harry Potter and the Philosopher's Stone","Gulliver's travels"]
    v=random.choice(m)
    w=random.choice(g)
    x=random.choice(p)
    y=random.choice(c)
    z=random.choice(b)
    k=list(v)
    r=[]
    if i.lower()=="movies":
        print (v)
        print("Your word is so length in a programmers way ,starting from 0 :) is :",len(k)-1)
        print(k)
        x1=check(k,'a')
        x2=check(k,'e')
        x3=check(k,'i')
        x4=check(k,'o')
        x5=check(k,'u')
        print(x1,x2,x3,x4,x5)
        if x1 !=[]:
            print("The word contains the letter 'a' with its position being at ",x1)
        else:
            pass
        if x2 !=[]:
            print("The word contains the letter 'e' with its position being at ",x2)
        else:
            pass
        if x3 !=[]:
            print("The word contains the letter 'i' with its position being at ",x3)
        else:
            pass
        if x4 !=[]:
            print("The word contains the letter 'o' with its position being at ",x4)
        else:
            pass
        if x5 !=[]:
            print("The word contains the letter 'u' with its position being at ",x5)
        else:
            pass
        
        
        
    elif i.lower()=="games":
        print (w)
    elif i.lower()=="places":
        print (x)
    elif i.lower()=="celebrities":
        print (y)
    elif i.lower()=="books":
        print (z)