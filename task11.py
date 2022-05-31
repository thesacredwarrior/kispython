import struct


def structD(data, pointer):
    float_d, = struct.unpack(">f", data[pointer:pointer + 4])
    float_d_2, = struct.unpack(">f", data[pointer + 4:pointer + 8])
    array_d, = struct.unpack(">i", data[pointer + 8:pointer + 12])
    array_d_2, = struct.unpack(">i", data[pointer + 12:pointer + 16])
    array_d_3, = struct.unpack(">i", data[pointer + 16:pointer + 20])
    d = []
    d.append(array_d)
    d.append(array_d_2)
    d.append(array_d_3)
    int8_d, = struct.unpack(">b", data[pointer + 20:pointer + 21])
    uint16_d, = struct.unpack(">H", data[pointer + 21:pointer + 23])
    return {'D1': float_d, 'D2': float_d_2, 'D3': d,
            'D4': int8_d, 'D5': uint16_d}


# H - uint16 2
# h - int16 2
# I - uint32 4
# i - int32 4
# b - int8 1
# B - uint8 1
# q - int64 8
# Q - uint64 8
# f - float 4
# c - char 1

def structC(data, pointer):
    int32_c, = struct.unpack(">i", data[pointer:pointer + 4])
    int64_c, = struct.unpack(">q", data[pointer + 4:pointer + 12])
    uint8_c, = struct.unpack(">B", data[pointer + 12:pointer + 13])
    uint32_c, = struct.unpack(">I", data[pointer + 13:pointer + 17])
    uint64_c, = struct.unpack(">Q", data[pointer + 17:pointer + 25])
    return {'C1': int32_c, 'C2': int64_c, 'C3': uint8_c,
            'C4': uint32_c,
            'C5': uint64_c}


def structB(data, pointer):
    float_b, = struct.unpack(">f", data[pointer:pointer + 4])
    int16_b, = struct.unpack(">h", data[pointer + 4:pointer + 6])
    int16_b_2, = struct.unpack(">h", data[pointer + 6:pointer + 8])
    f2 = struct.unpack('>II', data[pointer + 8:pointer + 16])
    b2 = list(struct.unpack(f'>{f2[0]}c', data[f2[1]:f2[1] + f2[0]]))
    b = ''
    for i in range(len(b2)):
        b += chr(b2[i][0])
    f_uint16, = struct.unpack(">H", data[pointer + 16:pointer + 18])
    uint32_c = structC(data, f_uint16)
    return {'B1': float_b, 'B2': int16_b, 'B3': int16_b_2,
            'B4': b, 'B5': uint32_c}


def structA(data, pointer):
    int8_a, = struct.unpack(">b", data[pointer:pointer + 1])
    f2 = struct.unpack('>HI', data[pointer + 1:pointer + 7])
    a2 = list(struct.unpack(f'>{f2[0]}c', data[f2[1]:f2[1] + f2[0] * 1]))
    a = ''
    for i in range(len(a2)):
        a += chr(a2[i][0])
    int16_a, = struct.unpack(">h", data[pointer + 7:pointer + 9])
    strB = structB(data, pointer + 9)
    f1 = struct.unpack(">IH", data[pointer + 27:pointer + 33])
    a1 = []
    adr_c = struct.unpack('>H', data[f1[1]:f1[1] + 2])
    count = f1[0]
    for i in range(count):
        f3 = structD(data, adr_c[0] + (i * 23))
        a1.append(f3)
    double_a, = struct.unpack(">d", data[pointer + 33:pointer + 41])
    double_a_2, = struct.unpack(">d", data[pointer + 41:pointer + 49])
    return {'A1': int8_a, 'A2': a, 'A3': int16_a, 'A4': strB,
            'A5': a1, 'A6': double_a, 'A7': double_a_2}


def main(data):
    return structA(data, 4)


print(main(b'ZSAix\x00\x03\x00\x00\x005\xabV>\xe3%\xc5\x99>\x9c\x1f\x00\x00\x00'
           b'\x03\x00\x00\x008\x00;\x00\x00\x00\x04\x00\xb0\xbf\xaa\xd1\x82\xa1\xbdG'
           b'\xe0\xbf\xe0\xf2b\xfcM\x88\xd0blrzpiV~\xe2b\x18\xfb\x07\x81\xf2`\x03\x0cx'
           b'\xf2\xfe\xcc\xfc\xd6\x97\xbb\x9a\x15\n\x99\x92>\xa9\t\xdc>\xab\x1c\xd6'
           b'\xda\xa0\xedY,w!\x88\x9d\x97}n\xc5\\\x99\xbe\xa4\xe0\x8e?d\xec\xbb='
           b'\xcaP\x0b\xf2\xc3#\xb2\xf9\xb7)\x07x=v\xbfM\x03\xcf>`h\xec\xe8y=HX\xc1'
           b'W{y\x9bd|\xc2ag?[\x0c\x86>\xbb5\xc6C9\x05\xf7m\xe4\x05]\x18\xf9\xb1'
           b'R\xbb\xd99\x00T\x00k\x00\x82\x00\x99'))
