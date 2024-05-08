#Code for Main.py file

from LinearProbing import hashTable
from record import Record
from Doubletry import doubleHashTable
def input_record():
    
    record = Record()
    name = input("Enter Name:")
    number = int(input("Enter Number:"))
    record.set_name(name)
    record.set_number(number)
    return record
   

choice1 = 0
while(choice1 != 3):
    print("************************")
    print("1. Linear Probing      *")
    print("2. Double Hashing      *")
    print("3. Exit                *")
    print("************************")

    choice1 = int(input("Enter Choice"))
    if choice1>3:
        print("Please Enter Valid Choice")

    if choice1 == 1:
        
        h1 = hashTable()
        choice2 = 0
        while(choice2 != 4):
            print("************************")
            print("1. Insert              *")
            print("2. Search              *")
            print("3. Display             *")
            print("4. Back                *")
            print("************************")

            choice2 = int(input("Enter Choice"))
            if choice2>4:
                print("Please Enter Valid Choice")

            if(choice2==1):
                record = input_record()
                h1.insert(record)

            elif(choice2 == 2):
                record = input_record()
                position = h1.search(record)

            elif(choice2 == 3):
                h1.display()
            
     
    elif choice1 == 2:
  
        h2 = doubleHashTable()
        choice2 = 0
        while(choice2 != 4):
            print("************************")
            print("1. Insert              *")
            print("2. Search              *")
            print("3. Display             *")
            print("4. Back                *")
            print("************************")

            choice2 = int(input("Enter Choice"))
            if choice2>4:
                print("Please Enter Valid Choice")

            if(choice2==1):
                record = input_record()
                h2.insert(record)

            elif(choice2 == 2):
                record = input_record()
                position = h2.search(record)

            elif(choice2 == 3):
                h2.display()
#Record.py file

class Record:
    def __init__(self):
        self._name = None
        self._number = None

    def get_name(self):
        return self._name

    def get_number(self):
        return self._number

    def set_name(self,name):
        self._name = name

    def set_number(self,number):
        self._number = number

    def __str__(self):
        record = "Name: "+str(self.get_name())+"\t"+"\tNumber: "+str(self.get_number())
        return record
#LinearProbing.py file

from record import Record
 
class hashTable:
    # initialize hash Table
    def __init__(self):
        self.size = int(input("Enter the Size of the hash table : "))
        # initialize table with all elements 0
        self.table = list(None for i in range(self.size))
        self.elementCount = 0
        self.comparisons = 0
   
   
    # method that checks if the hash table is full or not
    def isFull(self):
        if self.elementCount == self.size:
            return True
        else:
            return False
   
   
    # method that returns position for a given element
    def hashFunction(self, element):
        return element%self.size
   
  
  # method that inserts element into the hash table
    def insert(self, record):
        # checking if the table is full
        if self.isFull():
            print("Hash Table Full")
            return False
           
        isStored = False
        num=record.get_number()
        position = self.hashFunction(num)
       
        # checking if the position is empty
        if self.table[position] == None:
            self.table[position] = record
            isStored = True
            self.elementCount += 1
       
        # collision occured hence we do linear probing
        else:
            
            while self.table[position] != None:
                position =(position+1)%self.size           
            self.table[position] = record
            isStored = True
            self.elementCount += 1
        return isStored
       
    
    # method that searches for an element in the table
    # returns position of element if found
    # else returns False
    def search(self, record):
        found = False
        
        position = self.hashFunction(record.get_number())
        
        if(self.table[position] != None):
            #print(self.table[position].get_name())
            if(self.table[position].get_name() == record.get_name() and self.table[position].get_number() == record.get_number()):
                isFound = True
                print("Phone number found at position {} ".format(position) + " and total comparisons are " + str(1))
                return position
            
            while self.table[position] != None or self.comparisons <= self.size:
                    
                    if(self.table[position].get_name() == record.get_name() and self.table[position].get_number() == record.get_number()):
                        isFound = True
                        #i=0
                        i = self.comparisons +1
                        print("Number found at position {} ".format(position) + " and total comparisons are " + str(i) )
                        return position 

                    position = (position+1)%self.size
                    self.comparisons += 1
                    
                    
                    if isFound == False:
                        print("Record not found")
                        return false

                               
 
    # method to display the hash table
    def display(self):
        print("\n")
        for i in range(self.size):
            print("Hash Value: "+str(i) + "\t\t" + str( self.table[i]) )
        print("The number of phonebook records in the Table are : " + str(self.elementCount))

        




    
    





        
                
                
                
            
            
        








