import heapq

class Heap():
    myList = [4, 6, 8, 5, 1, 3, 7, 2]

    def choices(self):
        print('what do you wnat to do:\n 1) create list\n 2)sort List - Heap method\n')
        choice = int(input('Enter choice: '))
        if choice==1:
            self.create_heap()
        elif choice==2:
            self.sort_heap()
        else:
            print('invalid choice')
    
    def create_heap(self):
        heapq.heapify(self.myList)
        print(self.myList)
        self.choices()
    
    def sort_heap(self):
        heap=[]
        sorted_heap = []
        for element in self.myList:
            heapq.heappush(heap,element)

        while heap:
            sorted_heap.append(heapq.heappop(heap))
        print(sorted_heap)
        self.choices
        

if __name__ == '__main__':
    Heap().choices()