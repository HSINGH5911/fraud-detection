acc = []
pres = []
recall = []
f1 = []
conf_mat = []

condensed ={}

def get_all_values(file):
    lines = file.readlines()

    i = 0

    while i < len(lines):
        line = lines[i]

        if line.startswith("Accuracy"):
            acc.append(line.split()[1])

        elif line.startswith("Precision"):
            pres.append(line.split()[1])

        elif line.startswith("Recall"):
            recall.append(line.split()[1])

        elif line.startswith("F1"):
            f1.append(line.split()[1])

        elif line.startswith("Confusion Matrix"):
            row1 = lines[i + 1].strip()
            row2 = lines[i + 2].strip()

            conf_mat.append([row1, row2])

        i += 1

def make_map(file):
    i = 0

    for line in file:
        if line.startswith("Using"):
            condensed[line.strip()] = [acc[i], pres[i], recall[i], f1[i], conf_mat[i]]
            i += 1

    for key, values in condensed.items():
        print(key)
        print(f"  Accuracy : {values[0]}")
        print(f"  Precision: {values[1]}")
        print(f"  Recall   : {values[2]}")
        print(f"  F1       : {values[3]}")
        print(f"  Confusion Matrix: {values[4]}")
        print()
    return condensed


def get_highest_accuracy():
   highest = -1
   name = ""

   for x in condensed:
       if float(condensed[x][0]) > highest:
           highest = float(condensed[x][0])
           name = x

   print(name)
   print(highest)

def get_highest_precision():
    highest = -1
    name = ""

    for x in condensed:
        if float(condensed[x][1]) > highest:
            highest = float(condensed[x][1])
            name = x

    print(name)
    print(highest)

def get_highest_recall():
    highest = -1
    name = ""

    for x in condensed:
        if float(condensed[x][2]) > highest:
            highest = float(condensed[x][2])
            name = x

    print(name)
    print(highest)

def get_highest_f1():
    highest = -1
    name = ""

    for x in condensed:
        if float(condensed[x][3]) > highest:
            highest = float(condensed[x][3])
            name = x

    print(name)
    print(highest)


with open("results.txt", "r") as file:
    get_all_values(file)
    # Storing for later implementation
    # print(acc)
    # print(pres)
    # print(recall)
    # print(f1)

    file.seek(0)

    make_map(file)

    file.seek(0)
    get_highest_accuracy()

    file.seek(0)
    get_highest_precision()

    file.seek(0)
    get_highest_recall()

    file.seek(0)
    get_highest_f1()
