class LinearSearch:
    mylist = [4, 6, 8, 5, 1, 3, 7, 2]
    def search(self):
        entry = int(input('Enter number to be searched: '))

        for i in range(0, len(self.mylist)):
            if self.mylist[i]==entry:
                print('index position of the number '+ str(entry)+ ' is '+str(i))
                self.search()
        


if __name__ =='__main__':
    LinearSearch().search()