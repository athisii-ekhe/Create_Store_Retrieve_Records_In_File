import pickle
import random
import os


total_record = 100


class Record:
    '''
    Objective: To represent a record entity.
    '''

    def __init__(self, key, value):
        '''
        Objective: To initialise the object of class Record.
        Input:
            self: Implicit object of class Record.
            key: Key of the object.
            value: Value of the object.
        '''
        self.key = key
        self.value = value

    def __str__(self):
        '''
        Objective: To retrieve string of key and value.
        Input:
            self: Implicit object of class Record.
        '''
        return f'Key: {self.key}\n   Value: {self.value}'

    def getKey(self):
        '''
        Objective: To retrieve the key of the object.
        Input:
            self: Impicit object of the class Record.
        '''
        return self.key


def createRecord():
    '''
    Objective: To create records to a file.
    '''
    file = open("File.txt", "wb")
    keyList = []
    i = 1
    while i <= total_record:
        key = random.randint(5000000, 7000000)
        # Storing only the unique keys(checking duplication)
        if key not in keyList:
            keyList.append(key)
            value = str(key)*10
            record = Record(key, value)
            pickle.dump(record, file)
            i += 1
    file.close()


def displayAll():
    '''
    Objective: To display all records in file.
    '''
    file = open("File.txt", "rb")
    i = 1
    try:
        while file:
            obj = pickle.load(file)
            print(i, "::", obj)
            i += 1

    except EOFError:
        pass
    file.close()


def retrieveSomeRecords():
    '''
    Objective: To retreive number of records at a time.
    '''
    file = open("File.txt", "rb")
    lower_index = int(input("Enter the lower index: "))
    upper_index = int(input("Enter the upper index: "))
    obj = pickle.load(file)
    size = file.tell()
    file.seek((lower_index-1)*size)
    while lower_index <= upper_index:
        obj = pickle.load(file)
        print(lower_index, "->", obj)
        lower_index += 1
    file.close()


def retrieveSpecificRecord():
    '''
    Objective: To retrieve specific record based on user request.
    '''

    file = open("File.txt", "rb")
    user_input = int(input("Enter the record number to retrieve: "))
    obj = pickle.load(file)
    size = file.tell()
    file.seek((user_input-1)*size)
    obj = pickle.load(file)
    print(obj)
    file.close()


def main():
    '''
    Objective: To print records according to the user request.
    '''
    createRecord()
    while True:
        print("\n1. Print all the records.\n2. Print a number of records.\n3. Print a particular record\n4. Exit")
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            displayAll()

        elif user_choice == "2":
            retrieveSomeRecords()

        elif user_choice == "3":
            retrieveSpecificRecord()

        elif user_choice == "4":
            break

        else:
            print("Invalid input!")


if __name__ == "__main__":
    main()
