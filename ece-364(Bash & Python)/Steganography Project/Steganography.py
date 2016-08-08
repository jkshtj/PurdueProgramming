import numpy
import scipy
import zlib
import base64
import re
import copy

class Payload:

    def __init__(self, img=None, compressionLevel=-1, xml=None):
        if img is None and xml is None:
            raise ValueError('Invalid arguments given for img and xml')
        if compressionLevel > 9 or compressionLevel < -1:
            raise ValueError('Invalid argument given for compressionLevel-must be b/w 0 and 9')
        if img is not None and type(img) != numpy.ndarray or xml is not None and type(xml) != str:
            raise TypeError('Invalid type for img or xml')


        if(xml):
            self.xml = xml
            self.img = self.genImg(self.xml, compressionLevel)
        else:
            self.img = img
            self.xml = self.genXml(self.img, compressionLevel)


    '''Given a color or a black and white image in the form of a ndarray, this function returns an xml string '''
    def genXml(self, img, compressionLevel):
        size = img.shape
        compressed = False

        if type(img[0][0]) == numpy.ndarray:  # color img
            r=[]; g=[]; b=[]
            for x in img:
                for y in x:
                    r.append(y[0]); g.append(y[1]); b.append(y[2])
            pixels = r+g+b
            pixels = numpy.asarray(pixels)

            if compressionLevel != -1:
                compressed = True
                pixels = zlib.compress(pixels,compressionLevel)

            pixels = base64.b64encode(pixels)
            pixels = str(pixels).split("'")[1]

            xml = '<?xml version="1.0" encoding="UTF-8"?>\n<payload type="Color" size="' + str(size[0]) + ',' + str(size[1]) +'" compressed="' + str(compressed) + '">\n' + pixels + '\n</payload>'

            return xml

        else:
            pixels = [y for x in img for y in x]
            pixels = numpy.asarray(pixels)

            if compressionLevel != -1:
                compressed = True
                pixels = zlib.compress(pixels,compressionLevel)

            pixels = base64.b64encode(pixels)
            pixels = str(pixels).split("'")[1]

            xml = '<?xml version="1.0" encoding="UTF-8"?>\n<payload type="Gray" size="' + str(size[0]) + ',' + str(size[1]) +'" compressed="' + str(compressed) + '">\n' + pixels + '\n</payload>'

            return xml


    '''Given an xml string this function constructs an ndarray from the string and returns an image'''
    def genImg(self,xml,compressionLevel):
        xml = re.split('\n',xml)
        img_data = re.split('"',xml[1])

        type = img_data[1]
        size = [int(x) for x in img_data[3].split(',')]
        compressed = img_data[5]
        pixels = xml[2]

        pixels = base64.b64decode(pixels)       # decode base 64 encoding

        if compressed == 'True':
            pixels = zlib.decompress(pixels)    # if data was compressed, decompress it

        pixels = list(pixels)                   # converting byte data into a list, which will give us the actual numbers of ndarray(i.e. the image)

        if type == 'Gray':                      # Based on image type, reconstruct numpy.ndarray
            return numpy.resize(pixels,tuple(size))

        else:
            r = pixels[:size[0]*size[1]]
            g = pixels[size[0]*size[1]:2*size[0]*size[1]]
            b = pixels[2*size[0]*size[1]:3*size[0]*size[1]]
            image = []
            for i in range(size[0] * size[1]):
                image.append(r[i])
                image.append(g[i])
                image.append(b[i])

            size.append(3)
            return numpy.resize(image,tuple(size))


class Carrier:

    def __init__(self,img):
        if type(img) != numpy.ndarray:
            raise TypeError('Invalid argument given for img')
        self.img = img

    '''Given a carrier this function checks if a payload has been embedded into its image'''
    def payloadExists(self):
        if type(self.img[0][0]) == numpy.ndarray:           # color image
            pixels = [y[0] for x in self.img for y in x]
            pixels = pixels[0:24]
            first_3 = []                                    # first 3 bytes, to be checked for payload existence, constructed from the first 24 bytes of the image

            for x in pixels:
                if x%2 == 0:
                    first_3.append('0')
                else:
                    first_3.append('1')
            first = chr(int("".join(first_3[:8]),2))
            second = chr(int("".join(first_3[8:16]),2))
            third = chr(int("".join(first_3[16:]),2))
            if first == '<' and second == '?' and third == 'x':
                return True

            return False
        else:
            pixels = [y for x in self.img for y in x]
            pixels = pixels[0:24]
            first_3 = []

            for x in pixels:
                if x%2 == 0:
                    first_3.append('0')
                else:
                    first_3.append('1')
            first = chr(int("".join(first_3[:8]),2))
            second = chr(int("".join(first_3[8:16]),2))
            third = chr(int("".join(first_3[16:]),2))

            if first == '<' and second == '?' and third == 'x':
                return True

            return False

    '''If a payload has been embedded into the image of a carrier this function resets all the lsb of all the pixels of the image of the carrier and clears the payload'''
    def clean(self):
        new_img = copy.deepcopy(self.img)
        if type(new_img[0][0]) == numpy.ndarray:              # color img
            for i in range(len(new_img)):
                for j in range(len(new_img[i])):
                    for k in range(len(new_img[i][j])):
                        if new_img[i][j][k] % 2 == 0:
                            continue
                        else:
                            new_img[i][j][k] &= 0xFE
            return new_img

        else:
            for i in range(len(new_img)):
                for j in range(len(new_img[i])):
                    if new_img[i][j] % 2 == 0:
                        continue
                    else:
                        new_img[i][j] &= 0xFE
            return new_img


    ''' This function embeds the payload into the image of the carrier by replacing the least significant bits of all its pixels with the corresponding bits of the xml string'''
    def embedPayload(self, payload, override=False):
        if type(payload) != Payload:
            raise TypeError('Invalid type of argument given for payload')
        if override == False and self.payloadExists():
            raise Exception('Carrier already contains a payload')

        new_img = copy.deepcopy(self.img)
        xml_str = list(payload.xml)

        xml_bits = ""                                           # xml string in bits
        for x in xml_str:
            n = ord(x)
            xml_bits += format(n,'08b')

        if type(new_img[0][0]) == numpy.ndarray:               # color img

            if len(xml_bits) > len(new_img)*len(new_img[0])*3:
                raise ValueError('Image size is not big enough for embedding payload')

            r=[]; g=[]; b=[]
            for x in new_img:
                for y in x:
                    r.append(y[0]); g.append(y[1]); b.append(y[2])
            pixels = r+g+b

            ctr = 0

            for i in range(len(pixels)):
                if pixels[i] % 2 == 0 and xml_bits[ctr] == '1':
                    pixels[i] += 1

                elif pixels[i] % 2 == 1 and xml_bits[ctr] == '0':
                    pixels[i] -= 1

                ctr += 1

                if ctr+1 > len(xml_bits):
                    break

            r = pixels[:len(new_img)*len(new_img[0])]
            g = pixels[len(new_img)*len(new_img[0]):2*len(new_img)*len(new_img[0])]
            b = pixels[2*len(new_img)*len(new_img[0]):3*len(new_img)*len(new_img[0])]
            image = []
            for i in range(len(new_img)*len(new_img[0])):
                image.append(r[i])
                image.append(g[i])
                image.append(b[i])

            return numpy.resize(image,(len(new_img),len(new_img[0]),3))

        else:

            if len(xml_bits) > len(new_img)*len(new_img[0]):
                raise ValueError('Image size is not big enough for embedding payload')

            pixels = [y for x in new_img for y in x]

            ctr = 0

            for i in range(len(pixels)):
                if pixels[i] % 2 == 0 and xml_bits[ctr] == '1':
                    pixels[i] += 1

                elif pixels[i] % 2 == 1 and xml_bits[ctr] == '0':
                    pixels[i] -= 1

                ctr += 1

                if ctr + 1 > len(xml_bits):
                    break

            return numpy.resize(pixels,(len(new_img),len(new_img[0])))


    '''Given a carrier, this function extracts the payload from its image'''
    def extractPayload(self):
        if self.payloadExists() == False:
            raise Exception('Carrier does not contain any payload')

        bits = ""
        xml_str = ""

        if type(self.img[0][0]) == numpy.ndarray:              # color img

            r=[]; g=[]; b=[]
            for x in self.img:
                for y in x:
                    r.append(y[0]); g.append(y[1]); b.append(y[2])
            pixels = r+g+b

            for x in pixels:
                if x % 2 == 0:
                    bits += '0'
                else:
                    bits += '1'

                if len(bits) == 8:
                    xml_str += chr(int(bits,2))
                    bits = ""

                if "</payload>" == xml_str[len(xml_str)-10 : len(xml_str)]:
                    break

        else:

            pixels = [y for x in self.img for y in x]

            for x in pixels:
                if x % 2 == 0:
                    bits += '0'
                else:
                    bits += '1'

                if len(bits) == 8:
                    xml_str += chr(int(bits,2))
                    bits = ""

                if "</payload>" == xml_str[len(xml_str)-10 : len(xml_str)]:
                    break

        payload = Payload(xml = xml_str)
        return payload

