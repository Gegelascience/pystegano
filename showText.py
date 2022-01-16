from PIL import Image


def getMsgFromColor(filePath, colorSearch):

    im = Image.open(filePath)

    r, g, b = im.split()

    if colorSearch == "red":
        rBytes = r.tobytes()
    elif colorSearch == "green":
        rBytes = g.tobytes()
    else:
        rBytes = b.tobytes()

    listLowerBit = []

    for bit in rBytes:
        binValueStr = str(bin(bit))
        listLowerBit.append(binValueStr[len(binValueStr) - 1])

    msg = ""
    for i in range(0, len(listLowerBit) - 1, 8):
        try:
            listChar = ""
            for index in range(i, i + 8):
                listChar += listLowerBit[index]

            if listChar == "00000000":
                break
            else:
                msg += chr(int(listChar, 2))

        except Exception as e:
            print(e)
            break

    return msg

if __name__ == "__main__":
    msg = getMsgFromColor("./test.png", "red")
    print(msg)
