class stack:
    def __init__(self,matrix : list = []):
        self.matrix = matrix
    
    def __repr__(self) -> str:
        return f'{self.matrix}'
    
    def Push(self,other):
        if type(other) == list:
            self.matrix.extend(other)
        else:
            self.matrix.append(other)

    def Pop(self):
        if len(self.matrix)==0:
            raise ValueError("List Is Empty : ")
        else:
            return self.matrix.pop()
    
    
# STK = Stack()
# while True:
#     print ("\nPush -> 1")
#     print ("Pop -> 2")
#     print ("Display-Stack −> 3") 
#     print ("Exit -> 4\n")
#     b= int(input("Enter your choice: "))

#     if b ==1:
#         element = input("Enter a list or a value : ")
#         if "," in  element:
#             element = element.split(",")
#         STK.Push(element)
#         continue

#     if b ==2:
#         print(f"Popped Element : {STK.Pop()}")
#         continue

#     if b ==3:
#         print(STK)
#         continue

#     else:
#         break