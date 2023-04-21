from fastapi import FastAPI, Response
import qrcode
from io import BytesIO

app = FastAPI()


@app.get("/generate/QR")
def generate(url: str) -> bytes:
    """
    This function is responsible for generating qr code for the url inputed

    Args:
        url (str): url you want generate a qr code for

    Returns:
        bytes: image in a form of bytes
    """

    qr = qrcode.QRCode(version=1,
                       box_size=10,
                       border=5)

    # Adding data to the instance 'qr'
    qr.add_data(url)

    qr.make(fit=True)
    img = qr.make_image(fill_color='black',
                        back_color='white')

    # Convert the PIL image object to bytes
    img_bytes = BytesIO()
    img.save(img_bytes)
    img_bytes = img_bytes.getvalue()

    # Create a FastAPI response object with the image bytes and content type
    response = Response(content=img_bytes, media_type="image/png")

    return response
