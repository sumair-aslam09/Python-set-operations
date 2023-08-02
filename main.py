import argparse
import sys
import time


def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()
            rl= [line for line in lines if line.strip()]
        if len(rl) == 0:
            raise Exception(f"File {file_name} present but data is missing, set operations can't be performed")
        return rl
    except FileNotFoundError:
        print("{0} not found".format(file_name))
        sys.exit(1)


def is_valid_email(a):
    dic = {}
    for i in a:
        if '@' in i:
            parts = i.split('@')
            if len(parts) == 2 and '.' in parts[1]:
                dic[i] = True
    return dic


def union(ls1, ls2):
    ls3 = {}
    ls3.update(ls1)
    ls3.update(ls2)
    union_op = {}
    for i in ls3:
        if i not in union_op:
            union_op[i] = True
    return list(union_op.keys())


def intr(ls1, ls2):
    if len(ls1) <= len(ls2):
        intrsec = {}
        for i in ls1:
            if i in ls2 and i not in intrsec:
                intrsec[i] = True
        return list(intrsec.keys())
    else:
        intrsec = {}
        for i in ls2:
            if i in ls1 and i not in intrsec:
                intrsec[i] = True
        return list(intrsec.keys())


def minus(ls1, ls2):
    if len(ls1) <= len(ls2):
        minus_op = {}
        for i in ls1:
            if i not in ls2:
                minus_op[i] = True
        return list(minus_op.keys())
    else:
        for i in ls2:
            if i in ls1:
                del ls1[i]
        return list(ls1.keys())


def write_file(file, res):
    with open(file, 'w') as f:
        f.write(''.join(res))



def main(args):
    try:
        start_time = time.time()
    # Checking a File is present or not, if present then reading a file and giving result as  list
        l1 = read_file(args.file1)
        l2 = read_file(args.file2)

    # checking list has valid emails, all valid emails are converted in to dictonary
        valid_l1 = is_valid_email(l1)
        valid_l2 = is_valid_email(l2)

    # performing set operations based on user requirement
        if sys.argv[0] == 'union.py':
            result = union(valid_l1, valid_l2)
        elif sys.argv[0] == 'intersection.py':
            result = intr(valid_l1, valid_l2)
        elif sys.argv[0] == 'minus.py':
            result = minus(valid_l1, valid_l2)

    # writing result in a output file
        write_file(args.output, result)
        end_time = time.time()

        print(f"Output: {args.file1}: {len(valid_l1)} emails, {args.file2}: {len(valid_l2)} emails, {args.output}: {len(result)} emails; Time taken: {int(end_time - start_time)} seconds.")
    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Perform set operations on two input files containing email addresses.')
    parser.add_argument('file1', help='First input file')
    parser.add_argument('file2', help='Second input file')
    parser.add_argument('output', help='Output file')
    args = parser.parse_args()
    main(args)




































































































































'''import sys
import time

def read_file(file_name):
   # try:
        with open(file_name, 'r') as f:
            lines = f.readlines()
        return [line.strip() for line in lines]
    #except FileNotFoundError:
        print("{0} not found".format(file_name))
        # sys.exit(1)


def union(l1, l2):
    l3 = l1 + l2
    union_op = {}
    for i in l3:
        if i not in union_op:
            union_op[i] = True
    return list(union_op.keys())


def intr(l1, l2):
    intrsec = {}
    for i in l1:
        if i in l2 and i not in intrsec:
            intrsec[i] = True
    return list(intrsec.keys())


def minus(l1, l2):
    minus_op = {}
    for i in l1:
        if i not in l2:
            minus_op[i] = True
    return list(minus_op.keys())


def write_file(file, res):
    open(file, 'w').writelines(res)


if __name__ == '__main__':
    try:
        start_time = time.time()
        file_name_1,file_name_2 = sys.argv[1],sys.argv[2]

        l1 = read_file(file_name_1)
        l2 = read_file(file_name_2)


        if len(l1) or len(l2) is 0:
            print("Files present but data is missing,set operations can't be performed")
            sys.exit(1)

        result = union(l1, l2)
        #result = intr(l1, l2)
        #result = minus(l1, l2)
        print(l2)
        write_file(sys.argv[3], result)
        end_time = time.time()

        print(f"Output: {file_name_1}: {len(l1)} emails, {file_name_2}: {len(l2)} emails, {sys.argv[3]}: {len(result)} emails; Time taken: {int(end_time - start_time)} seconds.")
    except Exception as e:
        print("Error: {}".format(e))
        sys.exit()'''