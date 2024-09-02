import qrcode
import qrcode.constants

#basic most simple way
# img = qrcode.make("hi this is shalva, how are you?")
# img.save("firstqrcode.png")

qr = qrcode.QRCode(box_size=50, border=10)
#link to website
qr.add_data("")
qr.make()

img = qr.make_image(fill_color="black", back_color="white")
img.save("hello.png")