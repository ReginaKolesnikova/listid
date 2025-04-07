spisok=[] #pustoy spisok 
numbers=[1,2,3,4,5]
abc=['Abc','B','C']
slovo="Programmeerimine"
slovo_list=list(slovo)


# print(slovo)
# print(slovo_list)

while True:
  print(f"\n \nLists: \nnumbers=[1,2,3,4,5] \nabc=['Abc','B','C'], \nslovo=",slovo_list)
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
    print ("You chose 3-rd operation. It is used to get certain part of list. You must enter first encounter, last encounter and step length")
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
      stirt=input("enter letter ")
      x = slovo.find(stirt, 0, 15)
      print(x)
  elif valik==6:
    stirt=input("letter to split ")
    x = slovo.split(stirt)
    print(x)


  # elif valik==7:
  # elif valik==8:
  # elif valik==9:
  # elif valik==10:
  # else:
  #    print("There is no such letter, try enter again")
  # print(slovo_list)



  # valik=int(input())
  # if valik==1:
  #    a=input("Enter letter: ")
  #    slovo_list.append(a)
  #    print (f"Added {a} in new list", slovo_list)
  # elif valik==2:
  #   slovo_list.extend(abc)
  #   print(slovo_list)
  # elif valik==3:
  #   a=input("Enter letter, which you want to add: ")
  #   i=int(input("Enter number of position, where you want to add letter: "))
  #   slovo_list.insert(i-1,a) #0,1,2...
  #   print(slovo_list)
  # elif valik==4:
  #   a=input("Enter letter, which you want to delete: ")
  #   n=slovo_list.count(a)
  #   if n>0:
  #      for i in range(n):
  #        slovo_list.remove(a)
  # else:
  #        print("There is no such letter, try again")
  # print(slovo_list)
