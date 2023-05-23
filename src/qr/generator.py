import qrcode
from settings import QR_Background_Color, QR_Color, qr_image, QR_Image_Size,OUTPUT_LOCATION
from PIL import Image
from typing import List

# To give space for the logo


# Setting up the Image

# Also adjusting the image size to make it suitable for the QR Code
# image = image.resize((QR_Image_Size, hsize), Image.ANTIALIAS)

# NOTE: The configuration in generating the qr code can be found at ```settings.py```

class QRGenerator:
    # def k
    def __init__(self, data: str | List[str], **args):
        self.data = data
        self.image = args.pop('logo',None)
        self.color = args.pop('color', QR_Color)
        self.background_color = args.pop('background', QR_Background_Color)
        self.output = args.pop('output', OUTPUT_LOCATION)
        self.size = args.pop('size', QR_Image_Size)
    def start_generate(self):
        if self.image is None:
            return self.generate_from_list()
        else:
            return self.generate_with_logo()
    def generate_with_logo(self):
        wpercent = (QR_Image_Size/float(image.size[0]))
        hsize = int((float(image.size[1])*float(wpercent)))
        image = Image.open(self.image)
        image = image.resize((QR_Image_Size, hsize), Image.ANTIALIAS)
        
        for data in self.data:
            qr = self.generate(data)
            pos = ((qr.size[0] - image.size[0]) // 2,(qr.size[1] - image.size[1]) // 2)
            qr.paste(image, pos)
            qr.save(f'{self.output}{data}.png')
            yield data

    def generate_from_list(self):
        for data in self.data:
            qr = self.generate(data)
            qr.save(f'{self.output}/{data}.png')
            yield data

    def generate(self, data:None) -> Image:
        """QR Code Generator Function
        
        @params:
        - data - contains the string of data to be turn into a qr code
        - args - for additional options
        
        `Returns`
        This return the final image of qr code
        """
        if data is None:
            data = self.data
        QrCode = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H
        )
        # The data to convert, will insert
        QrCode.add_data(data)

        # Where the QR code start to generate
        QrCode.make(fit=True)

        # Start to generate the image
        QrImg = QrCode.make_image(
            fill_color=self.color, back_color=self.background_color
        ).convert('RGB')
        
        return QrImg






    