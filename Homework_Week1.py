

print("Hello World")

for i in range(2):
    print("For Loop Example")
 
class Person: # Class example
    def __init__(self,age=18,income=5500):
        self.age=age
        self.income=income
       
    def getAttr(self):
        return self
         
persons=[] # array example
i=0;
inputs="yes"

while(inputs=="yes"): #while loop example
    print(f"enter Person's #{i+1} age and income")
    persons.append(Person())
    persons[i].age,persons[i].income=int(input()),int(input())
    
    i+=1
    
    print("do you want to enter another person's information?")
    
    inputs=input()
    if (inputs == "yes"):
        continue
    elif(inputs=="no"):
        break
         
    else:
        
        while(inputs!= "yes" and inputs!="no"):
            print("only enter yes or no to continue")
            inputs=input()
    
print("the age and income of the people you entered are as follows")
i=0
for person in persons:
    i=i+1
    print(f"Person #{i} age is: {person.age} and income is: {person.income}")
    

    
def calculateAverage(persons): # function example
    sum=0
    for i in range(len(persons)) :
        sum=persons[i].income+sum
    return sum/len(persons)
    
print(f"average of income is: {calculateAverage(persons)}")
    
