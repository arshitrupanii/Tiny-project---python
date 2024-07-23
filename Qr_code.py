import qrcode as qr

img = qr.make("https://www.xhmaster.com/")
img.save("Qr_code.png")