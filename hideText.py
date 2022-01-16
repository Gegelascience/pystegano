from PIL import Image


def getMsgBin(msg: str):
    msg_bin = [bin(ord(x))[2:].rjust(8, "0") for x in msg]
    msg_bin.append("0" * 8)
    return msg_bin


def hideMessage(msg_bin: list[str], colorBytes: bytes, width: int, height: int):
    listMofifiedBits = []
    for i, bit in enumerate("".join(msg_bin)):
        try:
            test = colorBytes[i] // 2 * 2 + int(bit)
            listMofifiedBits.append(test)
        except:
            break

    listRestructuredBytes = []
    for index, bit in enumerate(colorBytes):
        if index < len(listMofifiedBits):
            listRestructuredBytes.append(listMofifiedBits[index])
        else:
            listRestructuredBytes.append(colorBytes[index])

    rBytesModifed = bytes(listRestructuredBytes)

    r2 = Image.new("L", (width, height))
    r2.frombytes(rBytesModifed)
    return r2


def steganographyLsb(filePath: str, msg: str, modifiedColor: str):

    # im = Image.open("./derriere_pierre_rosette.jpg")
    im = Image.open(filePath)

    w, h = im.size

    r, g, b = im.split()

    # myMessage = "Voir au recto"

    msg_bin = getMsgBin(msg)

    if len(msg_bin) <= w * h:
        if modifiedColor == "red":
            rBytes = r.tobytes()
            r2 = hideMessage(msg_bin, rBytes, w, h)
            res = Image.merge("RGB", (r2, g, b))
            res.save("test.png")
        elif modifiedColor == "green":
            gBytes = g.tobytes()
            g2 = hideMessage(msg_bin, gBytes, w, h)
            res = Image.merge("RGB", (r, g2, b))
            res.save("test.png")
        else:
            bBytes = b.tobytes()
            b2 = hideMessage(msg_bin, bBytes, w, h)
            res = Image.merge("RGB", (r, g, b2))
            res.save("test.png")

    else:
        print("message too long")



if __name__ == "__main__":
    steganographyLsb("./derriere_pierre_rosette.jpg", "Voir au recto de la pierre de rosette", "red")
