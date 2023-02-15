class BinarySearch:
    mylist = [1, 2, 3, 4, 5, 6, 7, 8]

    def search(self, entry,low, high):
        print(low,high)
        if high >= low:
            mid = low +(high-low)//2
            print('mid is ',mid)
            if self.mylist[mid] == entry:
                return mid
            elif self.mylist[mid] > entry:
                return self.search(entry,low,mid-1)
            else:
                return self.search(entry,mid+1,high)
        return -1

    def display(self):
        low = 0
        high = len(self.mylist)-1
        try:
            entry = int(input('Enter number to be searched: '))
        except:
            print('not an integer number')
            self.display()

        binary_search = self.search(entry,low,high)
        if binary_search != -1:
            print('number is at index ', str(binary_search))
        else:
            print('Not found')

        self.display()

if __name__ == '__main__':
    BinarySearch().display()