import random
a=input("Are you ready for a game of Hangman?[Yes/No]: ")
def check(a,b):#two values will be receieved here a and b , from line 30 basically list k and ' '
    indices=[]
    for k ,c in enumerate(a): #enumerate basically is a tuple with indices and value  , so is our list was [0,1,0] , enumerate would make it like ((0,0),(1,1),(2,1))
        if c == b:#k value from above will be our index and our c value will be the letter , this just compares with our argument b which we passed through
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
    k=list(v)#we covert to list for comparision later on
    r=[]
    if i.lower()=="movies":
        print("Your word is so length in a programmers way ,starting from 0 :) is :",len(k)-1)
        print(k)
        print (v)
        s1=len(k)#finding the length of our list to multiply with *
        k1='*'*s1 #multiples * with the number of letters in the word , * acts as unknow value
        r=list(k1) #coverts it to a list
        m1=check(k,' ') # check for specific value in our list and returns list of all indices with that specific value
        m2=check(k,'-')#calls the check function which is defined on top (line 3)
        m3=check(k,':')
        m4=check(k,'.')
        if m1!=[]: #iniciates only if value is found and list is returned
            for i in m1: # for the number presents in list , we pop the * with the index then insert the value in that specific place
                r.pop(i)
                r.insert(i,'_')
        if m2!=[]:
            for i in m2:
                r.pop(i)
                r.insert(i,'-')
        if m3!=[]:
            for i in m3:
                r.pop(i)
                r.insert(i,':')
        if m4!=[]:
            for i in m4:
                r.pop(i)
                r.insert(i,'.')
        x1=check(k,'a') # this checks for vowels and does the same thing
        x2=check(k,'e')
        x3=check(k,'i')
        x4=check(k,'o')
        x5=check(k,'u')
        if " " in k: # this just checks for value and replaces space with '_'
            a=k.index(" ")
            k[a]="_"
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
            for i in x4:
                r.pop(i)
                r.insert(i,'o')
        if x5 !=[]:
            for i in x5:
                r.pop(i)
                r.insert(i,'u')
        print(" _ in your sentence , indicates space")
        for i in r:#for each element in list r , it prints that elements with each element close by
            print(i,end=" ")
        
    elif i.lower()=="games":
        print (w)
    elif i.lower()=="places":
        print (x)
    elif i.lower()=="celebrities":
        print (y)
    elif i.lower()=="books":
        print (z)
