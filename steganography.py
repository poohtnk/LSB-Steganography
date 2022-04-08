# 1. Thanakorn Limpanawuthi 6288028 Sec.2
# 2. Wish      Suchalermkul 6288135 Sec.2

from PIL import Image,ImageOps

def changeNum(pixel):
    if pixel % 2 == 0:
        return pixel + 1
    else:
        return pixel - 1

# Convert message to ASCII
def string_to_ascii(text):
    # Add stop string
    text += "!!!!####"
    ascii_values = []
    for character in text:
        ascii_values.append(ord(character))
    return ascii_to_binary(ascii_values)

#Convert ASCII to binary
def ascii_to_binary(list):
    message = ''
    for i in list:
        message+=(format(i,'08b'))
    return message

def encrpyt(message):
    n = len(message)
    index= 0
    stopLoop = False
    for i in range(row):
        if stopLoop:
            break
        for j in range(col):
            if stopLoop:
                break
            tempList = list(px[i,j])
            # Loop through layers (R,G,B) or (R,G,B,A)
            for k in range(len(tempList)):
                if index >= n:
                    stopLoop = True
                    break
                # If the least significant bit (LSB) is different from the message bit
                # Then change the LSB to be the message bit
                if (tempList[k] % 2 != int(message[index])):
                    tempList[k] = changeNum(tempList[k])
                index+=1     
            px[i,j] = tuple(tempList)

def decode(decryptFile):
    img_decode = Image.open(decryptFile, mode='r')
    px_decode = img_decode.load()
    row_decode,col_decode= img_decode.size
    decode_message = ""
    #Loop through each pixel then each layers (R,G,B) or (R,G,B,A)
    data = ""
    position = -1
    for i in range(row_decode):
        for j in range(col_decode):
            for k in px_decode[i,j]:
                #Append the last significant bit
                decode_message += (format(k,'08b'))[-1]
                position += 1
                # Check if the binary length is equal to 8
                # If True then convert that Byte to Character
                if (position % 8 == 0 and position / 8 != 0):
                    # Extract byte
                    temp = decode_message[position-8:position]
                    # Convert from Binary to Integer
                    temp2 = int(temp,2)
                    # Convert Integer to Character
                    data += (chr(temp2))
                # If it found the stop string then stop converting
                # And return the converted data
                if data[-8:] == '!!!!####':
                    return data[:-8]

def calculateTotalbit():
    return row*col*len(px[0,0])

print("Please Select Mode:")
print("Encode: 1")
print("Decode: 2")
mode = int(input("Input: "))

if mode == 1:
    inputFile = input("Enter the Filename for encrpyt: ")
    img = Image.open(inputFile, mode='r')
    row,col= img.size
    px = img.load()
    totalBit = calculateTotalbit()
    text = input("Enter a message: ")
    if (totalBit/8 >= len(text) + 8):
        encrpyt((string_to_ascii(text)))
        outputFile = input("Enter the Filename for encrpyted file: ")
        img = img.save(outputFile)
        print("Done")
    else:
        print("Too Long Message")
elif mode == 2:
    decryptFile = input("Enter the Filename for decrypt: ")
    print("Decrypting file...")
    print("Decoded Text:",decode(decryptFile))



