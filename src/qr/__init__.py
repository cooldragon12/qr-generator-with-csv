import qrcode
from settings import QR_Background_Color, QR_Color, qr_image, QR_Image_Size,OUTPUT_LOCATION
from PIL import Image


# To give space for the logo


# Setting up the Image
image = Image.open(qr_image)
# Also adjusting the image size to make it suitable for the QR Code
wpercent = (QR_Image_Size/float(image.size[0]))
hsize = int((float(image.size[1])*float(wpercent)))
image = image.resize((QR_Image_Size, hsize), Image.ANTIALIAS)

# NOTE: The configuration in generating the qr code can be found at ```settings.py```
def qr_generator(data, *args, **kwargs):
    """QR Code Generator Function
    
    @params:
    - data - contains the string of data to be turn into a qr code
    - args - for additional options
    
    `Returns`
    This return the final image of qr code
    """
    QrCode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    
    )
    # The data to convert, will insert
    QrCode.add_data(data)

    # Where the QR code start to generate
    QrCode.make()

    QrImg = QrCode.make_image(
        fill_color=QR_Color, back_color=QR_Background_Color
    ).convert('RGB')

    # set the size of the qr code
    pos = ((QrImg.size[0] - image.size[0]) // 2,
       (QrImg.size[1] - image.size[1]) // 2)

    QrImg.paste(image,pos)
    
    # Return the qr code
    # Not the main image but the data.
    # # Need to use .save method of the qrcode to get the exported image. 
    return QrImg






    