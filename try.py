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
    print(k)
    r=[]
    if i.lower()=="movies":
        print("Your word is so length in a programmers way ,starting from 0 :) is :",len(k)-1)
        print(k)
        print (v)
        s1=len(k)
        k1='*'*s1
        r=list(k1)
        m1=check(k,' ')
        m2=check(k,'-')
        if m1!=[]:
            for i in m1:
                r.pop(i)
                r.insert(i,' ')
        if m2!=[]:
            for i in m2:
                r.pop(i)
                r.insert(i,'-')
        x1=check(k,'a')
        x2=check(k,'e')
        x3=check(k,'i')
        x4=check(k,'o')
        x5=check(k,'u')
        if x1 !=[]:
            for i in x1:
                r.pop(i)
                r.insert(i,'a')
        if x2 !=[]:
            for i in x2:
                r.pop(i)
                r.insert(i,'e')
        if x3 !=[]:
            for i in x3:
                r.pop(i)
                r.insert(i,'i')
        if x4 !=[]:
            for i in x2:
                r.pop(i)
                r.insert(i,'o')
        if x5 !=[]:
            for i in x2:
                r.pop(i)
                r.insert(i,'u')
        print(r)
        print("Space seen between *'s indicate a space in orginal sentence")
        for i in r:
            print(i,end=" ")
        
    elif i.lower()=="games":
        print (w)
    elif i.lower()=="places":
        print (x)
    elif i.lower()=="celebrities":
        print (y)
    elif i.lower()=="books":
        print (z)
