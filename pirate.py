speech = {"hello":"arrrrr", "friend": "matey", "scallywags": "people", "water": "rum" ,"food": "turkey leg"}


def engtopirate(englishstring):
    

    #need dictonary, e.g speech = {'hello':'arrrrr'}

    #split english string into list of words
    englishlist = englishstring.split(" ")

    piratees = ""
         
    #fro every word in that list,
    for word in englishlist:
        #print("Right now, I'm looking at word <%s>" %word)
    #check if wird in dictonary
    # if word in dictonary, use that value if word in speech:
        if word in speech:
              #print(" I found the word! The word is now:")
              piratees = piratees + " " + speech[word]
             # print(piratees)
    #if word not in dictonary,use same word looked up.
        if word not in speech:
             piratees = piratees + " " + word
    #return the pirate sentence
    return piratees


piratephrase = engtopirate(" Hello good friend")
print(piratephrase)



    
   
    
