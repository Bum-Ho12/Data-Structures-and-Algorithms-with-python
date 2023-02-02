class BubbleSort():
    myList = [4, 6, 8, 5, 1, 3, 7, 2]

    def choices(self):
        print('what do you wnat to do:\n 1) create list\n 2)sort List\n 3) bubble sort - boolean sort\n')
        choice = int(input('Enter choice: '))
        if choice==1:
            self.create_list()
        elif choice==2:
            self.sort_list()
        elif choice==3:
            self.boolean_sort()
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
        iterations = 0
        for i in range(0,len(self.myList)-1):
            for j in range(len(self.myList)-1):
                if self.myList[j]>self.myList[j+1]:
                    self.myList[j],self.myList[j+1] = self.myList[j+1],self.myList[j]
                iterations +=1
        print('number of iterations: '+ str(iterations))
        print(self.myList)
        self.choices()

    def boolean_sort(self):
        swapped = True
        iterations = 0
        while(swapped):
            swapped = False
            for i in range(len(self.myList)-iterations-1):
                if self.myList[i]>self.myList[i+1]:
                    self.myList[i],self.myList[i+1] = self.myList[i+1],self.myList[i]
                    swapped = True
                iterations +=1
        print('number of iterations: '+ str(iterations))
        print(self.myList)
        self.choices()
if __name__ == '__main__':
    BubbleSort().choices()