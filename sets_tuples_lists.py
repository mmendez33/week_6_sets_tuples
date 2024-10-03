#collections = single variable used to store multiple variables
#list = [] ordered and changeable. Duplicates OK
# set = {} unordered and immutable, but Add/Remove  OK. NO duplicates
# Table = () ordered and unchangeable. Duplicates OK. FASTER


#LISTS

#fruits =["apple", "orange", "banana", "conconut"]

# print(fruits[::2])

# print(dir(fruits)) 

# print(help(fruits))

#print(len(fruits))

# print("pineapple"in fruits)

# for fruit in fruits
#print(fruit)

# fruits[1]= "pineapple"  #i can reassign values using this 

#fruits.remove{"apple"} #removes value
#fruits.insert("pineapple")#inserts a value
#fruits.sort()# sorts it
#fruits.reverse() #reverses it 
#fruits.clear()


#SETS
fruits = {"apple", "orange", "banana", "conconut"}

#print(dir{fruits})
#print(helpfruits})

#print(fruits[0])

#fruits.add("pineapple") #adds a value 
#fruits.remove("apple") #removes a value
#print(fruits)
#fruits.pop()  #removes the last item
#print(fruits)

#TUPLES

fruits = ("apple", "orange", "banana", "coconut")

#print(fruits.index("apples")) #gives you the placement of a value 
print(fruits.count("coconut"))

#print(fruits)
for fruit in fruits:
    print(fruit)



#DICTIONARIES 
    
#dictionary- a collection of {key:value} pairs ordered and changeable. No duplicates
    
capitals = {"USA": "Washington D.C" ,
            "India":"New Dehli" ,
            "China" :"Beijing",
            "Russia" : "Moscow"}
    
#print(dir(capitals))

#Print(capitals.get("India"))

#If capitals.get ("Japan"):
#print("That capital exists")
#else:
#print{"That capital doesn't exist"}

#capitals.update({"germany" : "Berlin"}) # adds a value 

#capitals.pop("China") #removes china 
#capitals.popitem() #removes latests added value 
#capitals.clear()

#keys = capitals.keys()

#for key in capitals.keys():
 #for key in capitals.keys():
   # print(key)

#values = capitals.values():
#for value in capitals.values():
 #  print(value)


items = capitals.items()
for key, value in capitals.items():
    print(f"{key}:{value}")