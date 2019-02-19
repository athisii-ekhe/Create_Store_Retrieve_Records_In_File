import pickle
import random
import os
from operator import attrgetter


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

    def get_key(self):
        '''
        Objective: To retrieve the key of the object.
        Input:
            self: Impicit object of the class Record.
        '''
        return self.key


def write_records_to_file(num):
    '''
    Objective: To create records to a file.
        Input Parameters:
        num : Number of record(s) to be created.
    '''
    file = open("File.txt", "wb")
    keyList = []
    i = 1
    while i <= num:
        key = random.randint(5000000, 7000000)
        # Storing only the unique keys(checking duplication)
        if key not in keyList:
            keyList.append(key)
            value = str(key)*10
            record = Record(key, value)
            pickle.dump(record, file)
            i += 1


def display_all():
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


def make_F1_and_F2():
    repeat = True
    blockSize = 4
    storeIn = True
    records = []
    file = open("File.txt", "rb")
    f1 = open("F1.txt", "wb")
    f2 = open("F2.txt", "wb")
    while repeat:
        try:
            for _ in range(1, blockSize+1):
                obj = pickle.load(file)
                records.append(obj)
        except EOFError:
            repeat = False

        sorted_records = sorted(records, key=attrgetter('key'))
        if storeIn:
            dumpTo = f1
        else:
            dumpTo = f2

        for el in sorted_records:
            pickle.dump(el, dumpTo)
        storeIn = not storeIn
        records = []

    file.close()
    f1.close()
    f2.close()


def retrieve_some_records(user_choice, lower_index, upper_index):
    '''
    Objective: To retreive number of records at a time.
    '''
    if user_choice == '1':
        file = open("F1.txt", "rb")
    else:
        file = open("F2.txt", "rb")
    try:
        obj = pickle.load(file)
        size = file.tell()
        file.seek((lower_index-1)*size)
        while lower_index <= upper_index:
            obj = pickle.load(file)
            print(lower_index, "->", obj)
            lower_index += 1
    except EOFError:
        print("\nNo more records to display")
    file.close()


def retrieve_single_record(user_choice,record_num):
    '''
    Objective: To retrieve specific record based on user request.
    '''
    if user_choice == '1':
        file = open("F1.txt", "rb")
    else:
        file = open("F2.txt", "rb")
    try:

        obj = pickle.load(file)
        size = file.tell()
        file.seek((record_num-1)*size)
        obj = pickle.load(file)
        print(obj)
    except EOFError:
        print("No such record found!")
    file.close()


def main():
    '''
    Objective: To print records according to the user request.
    '''
    total_record = int(input("Enter numbers of record to be created: "))
    write_records_to_file(total_record)
    make_F1_and_F2()
    while True:
        print("\n1. Print all the records.")
        print("2. Print a number of records.")
        print("3. Print a particular record.")
        print("3. Exit.")
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            display_all()

        elif user_choice == "2":
            print("\nSelect your file.")
            print("1. F1.txt")
            print("2. F2.txt")
            choice = input("Enter your choice: ")
            if choice == '1' or choice == '2':
                lower_index = int(input("Enter the lower index: "))
                upper_index = int(input("Enter the upper index: "))
                print()
                if lower_index <1:
                    print("Record number starts from 1.")
                else:
                    retrieve_some_records(choice,lower_index, upper_index)
            else:
                print("Invalid Input!")

        elif user_choice == "3":
            print("Select your file.")
            print("1. F1.txt")
            print("2. F2.txt")
            choice = input("Enter your choice: ")
            if choice == '1' or choice == '2':
                record_num = int(input("Enter the record number to retrieve: "))
                if record_num <1:
                    print("Record number starts from 1.")
                else:
                    print()
                    retrieve_single_record(choice,record_num)
            else:
                print("Invalid Input!")

        elif user_choice == "4":
            break

        else:
            print("Invalid input!")


if __name__ == "__main__":
    main()
