import random
import pickle


class Record:
    '''
    Objective: To represent a Record entity.
    '''

    def __init__(self):
        '''
        Objective: To instantiate a Record object
        Input:
            self: Implicit object of class Record
        '''
        self.key = random.randint(1000000, 2000000)
        self.value = str(self.key)*random.randint(50, 250)

    def __str__(self):
        '''
        Objective: To override string function
        Input:
            self: Implicit parameter
        Return: STring representation of object
        '''
        return 'Key: {} \nValue: {}'.format(self.key, self.value)

    def getKey(self):
        '''
        Objective: To return key value of a record
        Input:
            self: Implicit paramter
        Return: Key value
        '''
        return self.key


def main():
    '''
    Objective: To create records in a file.
    '''
    file = open("File.txt", "wb")

    # Generating Unique keys
    temp_keys = []
    keys = []
    while True:
        record = Record()
        temp_keys.append(record.getKey())
        if len(keys) == 100:
            break
        for key in temp_keys:
            if key not in keys:
                keys.append(key)
                if len(keys) == 100:
                    break

    for key in keys:
        pickle.dump(key, file)

    print("\nUnsorted Records: \n")
    for i in range(0, len(keys)):
        print('{}: {}'.format(i+1, keys[i]))

    file.close()

    separateRecord()
    displayRecords()
    mergeAndSortRecord()


def separateRecord():
    '''
    Objective: To make two files using Record file.
    '''

    file = open("File.txt", "rb")
    f1 = open("F1.txt", "wb")
    f2 = open("F2.txt", "wb")
    count = 1
    lst1 = []
    lst2 = []
    try:
        while file:
            if count < 5:
                obj = pickle.load(file)
                lst1.append(obj)
                if count == 4:
                    lst1 = sorted(lst1)
                count += 1

            else:
                obj = pickle.load(file)
                lst2.append(obj)
                if count == 8:
                    lst2 = sorted(lst2)
                count += 1
                if count == 9:
                    count = 1
    except EOFError:
        # print("Completed")
        pass

    for obj in lst1:
        pickle.dump(obj, f1)

    for obj in lst2:
        pickle.dump(obj, f2)

    file.close()
    f1.close()
    f2.close()


def displayRecords():
    '''
    Objective: To Display records in F1 and F2.
    '''
    f1 = open("F1.txt", "rb")
    print("\nRecords in F1:\n")
    try:
        while f1:
            obj = pickle.load(f1)
            print(obj)

    except EOFError:
        print("Completed")

    # Displaying records in F1.txt
    f2 = open("F2.txt", "rb")
    print("\nRecords in F2:\n")
    try:
        while f2:
            obj = pickle.load(f2)
            print(obj)

    except EOFError:
        print("Completed")


def mergeAndSortRecord():
    '''
    Objective: To sort and merge the two record files.
    Return Value: Return the sorted list.
    '''
    f1 = open("F1.txt", "rb")
    lst1 = []
    try:
        while f1:
            obj = pickle.load(f1)
            lst1.append(obj)

    except EOFError:
        pass

    f2 = open("F2.txt", "rb")
    lst2 = []
    try:
        while f2:
            obj = pickle.load(f2)
            lst2.append(obj)

    except EOFError:
        pass

    lst = []
    i = j = 0
    while True:
        if lst1[i] < lst2[j]:
            lst.append(lst1[i])
            i += 1
        if i == len(lst1):
            for c in range(j, len(lst2)):
                lst.append(lst2[c])
            break

        if lst1[i] > lst2[j]:
            lst.append(lst2[j])
            j += 1
        if j == len(lst2):
            for c in range(i, len(lst1)):
                lst.append(lst1[c])
            break

    i = 1
    print("\nSorted Records:\n")
    for k in lst:
        print(i, ":", k)
        i += 1


if __name__ == "__main__":
    main()

