#a class that simply holds the letter and position of said letter (if it has a position)

class letterObject():
  letter = ""
  position = None


#A function which simply just reads from the words.txt file and puts it into an array lol
def createList():

  wordList = []
  
  file = open("words.txt", "r")
  
  for word in file:
    wordList.append(word.strip())
  
  return wordList
  

#This function takes the array of the letters, and the array of all the 5 letter words, and then finds words with matching letters and positions and prints them
#it's a mess.
def wordFinder(letters, wList):

  print("The word might be:\n")


  #this gets really messy here, but basically this segment loops through all words, and has two smaller segments
  for word in wList:


    #this bit loops through the letters given by user, then for each of those through the word's letters and makes sure they are all there, if not, turns a boolean false
    allLetters = True

    for letter in letters:
      letterFound = False
      for let in word:
        if letter.letter == let:
          letterFound = True
      if letterFound != True:
        allLetters = False

    if allLetters == True:


      #this bit loops through words that have matching letters, and then checks if any positions match (if a position has been given)
      positionMatch = True
      
      for letter in letters:
        if letter.position != "":

          position = int(letter.position)

          if word[(position - 1): position] != letter.letter:
            positionMatch = False

      if positionMatch == True:
        print(word)


    

#This function just asks the user how many letters they have, then gets each letter and takes the position if they have a known position
def getLets(wordList):

  
  lets = []
  numLets = int(input("How many letters have you found?: "))
  for x in range(numLets):
    letter = letterObject()
    letter.letter = input(f"What is letter number {x+1}?: ")
    letter.position = input(f"What is the position of {letter.letter}? - leave blank if unknown: ")
    lets.append(letter)

  wordFinder(lets, wordList)




#calling the functions :)

list = createList()
getLets(list)
