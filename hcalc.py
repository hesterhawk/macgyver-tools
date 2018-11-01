import sys

class HCalc:

    def toBin(self,value):
        print("""
{}
        """.format(bin(int(value, 16))[2:]))

    def toHex(self,value):
        print("""
{}
        """.format(hex(int(value, 2))))

    def addToHex(self,hexval,value):
        print("""
{}
        """.format(hex(int(hexval, 16) + int(value))))

    def subFromHex(self,hexval,value):
        print("""
{}
        """.format(hex(int(hexval, 16) - int(value))))        

def info():
    print("""
Usage: hc [option] [value] *[value2]

b   convert value to binary e.g. 805D
h   convert value to hex e.g. 1000000001011101
ah  add value2(int) to value(hex)
sh  sub value2(int) from value(hex)
    """)

if __name__ == '__main__':
    args = sys.argv[1:]

    if [] == args: info() ; quit()

    hc = HCalc()

    if 'b' == args[0] and 2 == len(args):
        hc.toBin(args[1])
    elif 'h' == args[0] and 2 == len(args):
        hc.toHex(args[1])
    elif 'ah' == args[0] and 3 == len(args):
        hc.addToHex(args[1], args[2])        
    elif 'sh' == args[0] and 3 == len(args):
        hc.subFromHex(args[1], args[2])
    else:
        info() ; quit()