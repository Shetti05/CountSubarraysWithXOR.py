import qrcode

img = qrcode.make("Hello World")
img.save("qr.png")