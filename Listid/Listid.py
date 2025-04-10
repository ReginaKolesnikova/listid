spisok=[] #pustoy spisok 
numbers=[1,2,3,4,5]
abc=['Abc','A','B','C']
slovo="Programmeerimine"
slovo_list=list(slovo)


# print(slovo)
# print(slovo_list)

while True:
  print(f"\n \nLists: \nnumbers=[1,2,3,4,5] \nabc=['Abc','A','B','C'] \nslovo=",slovo_list)
  print("1 - repeat string\n2 - find letter by i- position") #s1 3 #s i
  print("3 - get certain part of list \n4 - show string length") #s i j step # len s
  print("5 - find first encounter\n6 - split list with symbol") #s find str start end # s split
  print("7 - find out whether there is only letters in string or not \n8 - makes caps letters") # s isalpha # s upper
  print("9 - captalize only first leter of word in string\n10 - swap uppercase letters with lowercase ones\n \n") # s capitalize # s swapcase


  #S-spisok
  #i-position
 
  valik=int(input("Choose operation: "))
  if valik==1: #repeat string
      print ("You chose 1-st operation. It is used to repeat list:numbers.")
      a=int(input("How much repeats do you want: "))
      repe=numbers*a
      print (f"Repeated {a} times: ", repe)
  elif valik==2: #find letter by i- position
    print ("You chose 2-nd operation. It is used to find letter by its position in list:slovo.")
    a=int(input("Enter position number (0-15): "))
    n=slovo_list[a]
    print (f"On position {a} located letter:", n)
  elif valik==3: #get certain part of list
    print ("You chose 3-rd operation. It is used to get certain part of list. You must enter first encounter, last encounter and step length. List:slovo")
    a=int(input("Enter first encounter (0-15): "))
    b=int(input("Enter last encounter (0-15): "))
    c=int(input("Enter step length (0,1,2...)"))
    n=slovo_list[a:b:c]
    print(n)
  elif valik==4: #show string length
       print ("You chose 4-th operation. It is used to show length of certain list.")
       a=int(input("Choose list to count its length (1-word, 2-letters or 3-numbers): "))
       if a==1:
          b=len(slovo_list)
          print(f"In list {slovo_list} - {b} symbols")
       elif a==2:
          b=len(abc)
          print(f"In list {abc} - {b} symbols")
       elif a==3:
          b=len(numbers)
          print(f"In list {numbers} - {b} symbols")
       else:
           print("wrong number")
  elif valik==5: #find first encounter
      print ("You chose 5-th operation. It is used to find first encounter of certain letter in word Programmeerimine.")
      stirt=input("Enter letter you want to find: ")
      a = slovo.find(stirt, 0, 15)
      print(a)
  elif valik==6: #split list by symbol
     print ("You chose 6-th operation. It is used to split word Programmeerimine to list on positions of certain symbol.")
     stirt=input("Enter letter which you want to use as splitter: ")
     a = slovo.split(stirt)
     print(a)
  elif valik==7: #find out whether there is only letters in string or not
  # add chance to make list false by inputting another symbol
    print ("You chose 7-th operation. It is used to find out whether there is only letters in string or not.")
    slovo="Programmeerimine"
    a = slovo.isalpha()
    print(f"It is",a,"that in",slovo,"used only letters")
  elif valik==8: #makes all letters in caps
     print ("You chose 8-th operation. It is used to make all letters in (phrase to test function) capital.")
     phrs="phrase to test function"
     a = phrs.upper()
     print(a)
  elif valik==9: #captalize only first leter of word in string
     print ("You chose 9-th operation. It is used to captalize only first leter in a sentence (phrase to test function).")
     phrs="phrase to test function"
     a = phrs.capitalize()
     print(a)
  elif valik==10: #captalize only first leter of word in string
     print ("You chose 10-th operation. It is used to swap uppercase letters with lowercase ones in a sentence (phRAse TO teST fuNCtiON).")
     phrs="phRAse TO teST fuNCtiON"
     a = phrs.swapcase()
     print(a)    
  else:
    print("There is no such operation, try to chose again")
