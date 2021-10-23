from os import walk

filenames = next(walk("datasets/"), (None, None, []))[2]


def getPointsData(filename):
    pointsArray = []
    with open(f'datasets/{filename}', "r") as f:
        line = f.readline()
        while line:
            pointsArray.append(line.strip().split())
            line = f.readline()

    return pointsArray


while True:
    try:
        for i in range(len(filenames)):
            print(f'{i+1}. {filenames[i]}')
        choice = int(input("Choose dataset number: "))
    except ValueError:
        print("Invalid input, try again\n")
        continue
    else:
        if choice < 1 or choice > len(filenames):
            print("Invalid input, try again\n")
            continue
        break


print(getPointsData(filenames[choice-1]))