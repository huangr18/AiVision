import PIL.Image as Image
import io
import base64


with open("PoseVideos/v7.mp4", "rb") as file:
    byte = file.read() # read a byte (a single character in text)
    #byte_val = ord(byte) # convert the string character into a number
    byte_array = bytearray(byte)

videoB = base64.b64decode(byte_array)
#print(videoB)

video = Image.open(io.BytesIO(videoB))
video.show()