import argparse
import pyAesCrypt

parser = argparse.ArgumentParser(description='Crypt/Decrypt your file like a pro using AES. Provided by Neek')
parser.add_argument('-m','--mode', help='Select mode (enc|dec)', required=True)
parser.add_argument('-i','--input', help='Path of the source file', required=True)
parser.add_argument('-o','--output', help='Path of the destination file (it will an AES file)', required=False)
parser.add_argument('-p','--password', help='Encrypt/decrypt password', required=True)
args = vars(parser.parse_args())

bufferSize = 64 * 1024
password = str(args['password'])
src = str(args['input'])
if args['output'] is not None:
    dst = str(args['output'])
else:
    if args['mode'] == 'enc':
        dst = src + ".aes"
    elif args['mode'] == 'dec':
        dst = src[:-4]

if args['mode'] == 'enc':
    # code here
    print("Encrypting..")
    pyAesCrypt.encryptFile(src, dst, password, bufferSize)

elif args['mode'] == 'dec':
    # code here
    print("Decrypting..")
    pyAesCrypt.decryptFile(src, dst, password, bufferSize)

else:
    print ("Invalid mode selection, retry")