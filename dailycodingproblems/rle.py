
class RLE(object):
    def __init__(self) -> None:
        super().__init__()

    def encode(self, string:str) -> str:
        last_char: str = ''
        count: int = 1
        encoded_str: str = ''
        for char in string:
            if last_char and last_char == char:
                count += 1
            else:
                if last_char:
                    encoded_str += last_char + str(count)
                last_char = char
                count = 1
        if last_char:
                encoded_str += last_char + str(count)
        return encoded_str

    def decode(self, encoded_str:str) -> str:
        decoded_str: str = ''
        length = len(encoded_str)
        index = 0
        while index < length:
            decoded_str += encoded_str[index]*int(encoded_str[index+1])
            index += 2
        return decoded_str

if __name__ == '__main__':
    input_str = input("Enter string to first encode & then decode")
    rle = RLE()
    encoded_str = rle.encode(input_str)
    print('Encoded : ', encoded_str, 'Decoded : ', rle.decode(encoded_str))