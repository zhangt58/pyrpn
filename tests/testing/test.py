from pyrpn.rpn import Rpn

def test():
    istr1 = '1 2 + 3 * sin'
    rpnins1 = Rpn(istr1)
    print rpnins1
    print rpnins1.solve()

    istr2 = '1 2 + 3 * cos'
    rpnins2 = Rpn(istr2)
    print rpnins2
    print rpnins2.solve()

    istr3 = '10,3,1,2,/,*,-,tan'
    rpnins3 = Rpn(istr3, ',')
    print rpnins3
    print rpnins3.solve()

    istr4 = '0.2 10.24 pi * 180 / * 10.24 pi * 180 / sin /'
    rpnins4 = Rpn(istr4)
    print rpnins4.solve()

    istr5 = '0.2 10.24 pi * 180 / * 10.24 pi * 180 / sin /'
    print Rpn.solve_rpn(istr5)

test()
