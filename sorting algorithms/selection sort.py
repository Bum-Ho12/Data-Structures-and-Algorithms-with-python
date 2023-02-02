class Selection():

    myList = [4, 6, 8, 5, 1, 3, 7, 2]
    def choices(self):
        print('what do you wnat to do:\n 1) create list\n 2)sort List - Selection method\n')
        choice = int(input('Enter choice: '))
        if choice==1:
            self.create_list()
        elif choice==2:
            self.sort_list()
        else:
            print('invalid choice')
    
    def create_list(self):
        entry = int(input('total numbers to add: '))
        self.myList.clear()
        for i in range(entry):
            new_entry = int(input('Enter Number: '))
            self.myList.append(new_entry)
        print(self.myList)
        self.choices()
    
    def sort_list(self):
        for i in range(len(self.myList)-1):
            min_index = i
            for j in range(i+1,len(self.myList)):
                if self.myList[j]<self.myList[min_index]:
                    min_index = j
            self.myList[i],self.myList[min_index] = self.myList[min_index],self.myList[i]
        print(self.myList)
        self.choices()

if __name__ == '__main__':
    Selection().choices()
