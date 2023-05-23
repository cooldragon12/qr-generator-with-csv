import pathlib
from os import path
# Base Path
BASE_PATH = pathlib.Path(__file__).parent.absolute()
# Here is the configuration of the QR code
# The Size of image indicated here not the Main qr code
QR_Image_Size = 150

# The main QR Code Size
QR_SIZE = 10 # Implemented yet 

# QR Code Color
# Set the default color here
QR_Color = 'black' # This can be a word or hex value

# QR Code Background Color
# Set your background color here
QR_Background_Color = 'white'

# Usually Empty
QR_Prefix ="https://gulamanentertainment.com/link/"

# Image to insert in the QR Code
# Specify the path here
qr_image = 'src/assets/default.png'

# List or Array of Data to Iterate / File to use
file_path = "./GEStaff.csv"

# Exported Qr Code path
OUTPUT_LOCATION = path.join(BASE_PATH.parent, "export")

LOG_FILE = "logs/qr.log"
