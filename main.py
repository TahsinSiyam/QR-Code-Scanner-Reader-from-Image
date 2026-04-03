import cv2
import qrcode as qr


inp = input("1. Encode                2. Decode")


def createQR():
    try:
        data = input("Enter Data: ")
        img = qr.make(data=data)
        img.save("qrcode.png")
    except:
        print("An Error Occured!")


def scanQR():
    try:
        img = input("Enter Image path here: ")
        imgReader = cv2.imread(f'r"{img}"')
        detector = cv2.QRCodeDetector()
        data, bbox, staright_code = detector.detectAndDecode(img=imgReader)
        if data:
            print(f"Decoded Data: {data}")
        else:
            print("Something went Wrong!")

    except :
        print("Error Occured!")

if inp == "1":
    createQR()
elif inp == "2":
    scanQR()
else:
    print("An Error Occured!")