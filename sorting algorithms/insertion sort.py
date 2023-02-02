class Insertion():
    myList = [4, 6, 8, 5, 1, 3, 7, 2]

    def choices(self):
        print('what do you wnat to do:\n 1) create list\n 2)sort List - insertion method\n')
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
        for i in range(1,len(self.myList)):
            key = self.myList[i]
            j = i-1
            while j>=0 and key <self.myList[j]:
                self.myList[j+1] = self.myList[j]
                j-=1
            self.myList[j+1] = key
        print(self.myList)

if __name__ == '__main__':
    Insertion().choices()