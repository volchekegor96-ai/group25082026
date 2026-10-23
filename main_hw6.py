import pyotp
import qrcode

user_name = "VolchekEgor"
issuer_name = "hillel"

secret = pyotp.random_base32()
totp_auth_url = pyotp.totp.TOTP(secret).provisioning_uri(name=user_name, issuer_name=issuer_name)

qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(totp_auth_url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("otp_qr_code.png")
img.show()
