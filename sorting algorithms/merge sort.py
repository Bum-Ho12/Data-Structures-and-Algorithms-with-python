class Merge():
    myList = [4, 6, 8, 5, 1, 3, 7, 2]

    def choices(self):
        print('what do you wnat to do:\n 1) create list\n 2)sort List - insertion method\n')
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

    def mergesort(self,mylist):
        if len(mylist)>1:
            middle = len(mylist)//2
            left_list = mylist[:middle]
            right_list = mylist[middle:]

            self.mergesort(left_list)
            self.mergesort(right_list)

            l_index = 0
            r_index = 0
            sorted_index = l_index

            while l_index<len(left_list) and r_index<len(right_list):
                if left_list[l_index]<=right_list[r_index]:
                    mylist[sorted_index] = left_list[l_index]
                    l_index +=1
                else:
                    mylist[sorted_index] = right_list[r_index]
                    r_index +=1
                    
                sorted_index +=1

            while l_index<len(left_list):
                mylist[sorted_index] = left_list[l_index]
                l_index +=1
                sorted_index +=1

            while r_index<len(right_list):
                mylist[sorted_index] = right_list[r_index]
                r_index +=1
                sorted_index +=1
        return mylist
    def display(self):
        arr = self.myList
        print(self.mergesort(arr))
        self.choices()


if __name__ == '__main__':
    merge = [4, 6, 8, 5, 1, 3, 7, 2, 9, 12, 15, 13, 14]
    # mergesort(merge)
    Merge().choices()
