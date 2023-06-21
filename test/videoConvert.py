started = 0
hash_val = 0

with open("PoseVideos/v7.mp4", "rb") as file:
    byte = file.read() # read a byte (a single character in text)
    #byte_val = ord(byte) # convert the string character into a number
    byte_array = bytearray(byte)

#print(byte_array)