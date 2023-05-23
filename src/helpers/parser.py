from argparse import ArgumentParser, Action
from genericpath import exists
import regex as re
from .exceptions import DirectoryNotFoundError

def parse_args():
    parse = ArgumentParser()
    file_subparse = parse.add_subparsers(dest="file", description="Read File and generate the data on each line, to qrcode`")
    file_parse = file_subparse.add_parser("file")
    file_parse.add_argument("-f", "--file",action=DirectoryCheckOutput, help="File to read")

    parse.add_argument("-d", "--data", nargs="*" , help="Data to generate")
    parse.add_argument("-o", "--output",action=DirectoryCheckOutput, help="Output file, where to save the generated qrcode")
    # parse.add_argument("-t", "--type", help="Type of qrcode to generate", default="png", required=False)
    parse.add_argument("-s", "--size", help="Size of the qrcode to generate", default=500, required=False)
    parse.add_argument("-c", "--color",action=HexColorCheck, help="Color of the qrcode to generate", default="black", required=False)
    parse.add_argument("-b", "--background", action=HexColorCheck,help="Background of the qrcode to generate", default="white", required=False)
    parse.add_argument("-l", "--logo", help="Logo of the qrcode to generate", required=False, default=None)
    # parse.add_argument("-p", "--position", help="Position of the logo of the qrcode to generate", required=False)
    parse.add_argument("-r", "--radius", help="Radius of the logo of the qrcode to generate", required=False)
    parse.add_argument("-a", "--align", help="Align of the logo of the qrcode to generate", required=False)
    parse.add_argument("-m", "--margin", help="Margin of the logo of the qrcode to generate", required=False)

    parse.add_argument("-v", "--version", help="Version of the qrcode to generate", default=1, required=False)

    return parse.parse_args()

class HexColorCheck(Action):
    # Checks if the color hex is valid or exist
    def __call__(self, parser, namespace, values, option_string=None):
        # Check if the value is a hex color
        if re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', values):
            raise ValueError("Invalid Hex Color")
        setattr(namespace, self.dest, values)

class DirectoryCheckOutput(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        # Chaeck if the directory exist
        if not exists(values):
            raise DirectoryNotFoundError("Directory specified not exist "+ values)
        setattr(namespace, self.dest, values)