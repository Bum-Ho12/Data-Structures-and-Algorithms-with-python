class QuickSort():
    myList = [4, 6, 8, 5, 1, 3, 7, 2]

    def choices(self):
        print('what do you wnat to do:\n 1) create list\n 2)sort List - Quick Sort method\n')
        choice = int(input('Enter choice: '))
        if choice==1:
            self.create_list()
        elif choice==2:
            self.display()
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

    def quicksort(self,arr):
        if len(arr)<2:
            return arr
        curr_pos = 0

        for i in range(1, len(arr)):
            if arr[i]<=arr[0]:
                curr_pos +=1
                arr[i],arr[curr_pos] = arr[curr_pos], arr[i]

        arr[0],arr[curr_pos] = arr[curr_pos], arr[0]

        left = self.quicksort(arr[:curr_pos])
        right = self.quicksort(arr[curr_pos + 1:])
        arr = left +[arr[curr_pos]] + right
        
        return arr
    
    def display(self):
        arr = self.myList
        print(self.quicksort(arr))
        self.choices()

if __name__ == '__main__':
    QuickSort().choices()
