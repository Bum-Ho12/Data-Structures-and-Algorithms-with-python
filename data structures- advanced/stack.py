class Stack():
    stack = []
    def choices(self):
        print('what do you wnat to do:\n -press type 1 to display\n - press 2 to push/add item to stack\n - press 3 to pop last number from stack')
        choice = int(input('Enter choice: '))
        if choice==1:
            self.display()
        elif choice==2:
            self.push()
        elif choice == 3:
            self.pop()
        else:
            print('invalid choice')
        
    def display(self):
        for i in range(len(self.stack)):
            print(str(i) + '. ' + str(self.stack[i]))
        self.choices()

    def pop(self):
        last_pos = len(self.stack)
        self.stack.remove(last_pos)
        self.display()
        self.choices()
        
    def push(self):
        print('To break, type exit\n to continue type continue')
        entry = input()
        if entry == 'exit':
            pass
        elif entry =='continue':
            entries = int(input('How many numbers to insert: '))
            for count in range(entries):
                print('enter number '+ str(count) + ': ')
                new_entry = int(input())
                self.stack.append(new_entry)
            self.display()
        self.choices()


if __name__ == '__main__':
    Stack().choices()