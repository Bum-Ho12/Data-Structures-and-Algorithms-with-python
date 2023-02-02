class Depth:
    mygraph = {
        'A':['B','C','D'],
        'B':['E'],
        'C': ['G','F'],
        'D':['H'],
        'E':['I'],
        'F':['J'],
        'G':['K']
    }
    path= set()

    def display(self):
        try:
            entry = input('Enter Letter to search path: ')
            self.search(entry)
            print('\n')
            self.display()
        except:
            # print('Empty or invalid input e.g A, B, C correct input')
            print('\n')
            self.display()

    def search(self,node):
        
        if node not in self.path:
            print(node, end=', ')
            self.path.add(node)

            for v in self.mygraph[node]:
                self.search(v)

if __name__ == '__main__':
    Depth().display()
