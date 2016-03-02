#!/usr/bin/env python

#
# -*- coding: utf-8 -*-
#
# 2016-02-01
# Author: Tong Zhang
#
from __future__ import division
from decimal import *
getcontext().prec = 16

"""
python package to handle RPN issues
RPN: Reverse Polish Notation

USAGE:
    rpnstr = '10 1 2 + sin *'
    rpnins = Rpn(rpnstr)
    result = rpnins.solve()

    Or:
    result = Rpn.solve_rpn(rpnstr)
"""
__AUTHOR__ = "Tong Zhang"
__VERSION__ = "1.0.0"


import math

class Rpn(object):
    def __init__(self, istr, delimiter = None):
        self.opslist = istr.lower().replace('pi',str(math.pi)).split(delimiter)
        self.opslist.reverse()
        
        oprts = ['+', '-', '*', '/', 'sin', 'cos', 'tan']
        opfun = [self.fadd, self.fsub, self.fmul, self.fdiv,
                 self.fsin, self.fcos, self.ftan]
        self.opdic = dict(zip(oprts, opfun))

    def fadd(self):
        a = float(self.tmpopslist.pop())
        b = float(self.tmpopslist.pop())
        return b + a

    def fsub(self):
        a = float(self.tmpopslist.pop())
        b = float(self.tmpopslist.pop())
        return b - a 

    def fmul(self):
        a = float(self.tmpopslist.pop())
        b = float(self.tmpopslist.pop())
        return  b * a

    def fdiv(self):
        a = float(self.tmpopslist.pop())
        b = float(self.tmpopslist.pop())
        return b / a

    def fsin(self):
        a = float(self.tmpopslist.pop())
        return math.sin(a)

    def fcos(self):
        a = float(self.tmpopslist.pop())
        return math.cos(a)

    def ftan(self):
        a = float(self.tmpopslist.pop())
        return math.tan(a)

    def __str__(self):
        return ' '.join(reversed(self.opslist))
        
    @classmethod
    def solve_rpn(cls, istr):
        """ solve rpn expression

            USAGE: solve_rpn(rpnstr)
            :param rpnstr: rpn string
            return: calculated result
        """
        return cls(istr).solve()

    def solve(self):
        popflag = True
        self.tmpopslist = []
        while len(self.opslist) > 1:

            while popflag:
                try:
                    op = self.opslist.pop()
                    self.tmpopslist.append(op)
                    try:
                        float(op)
                    except:
                        popflag = False
                except IndexError:
                    return 0

            try:
                oprt = self.tmpopslist.pop()
                tmpr = self.opdic[oprt]()
            except (IndexError, ValueError, KeyError):
                return 0
            self.opslist.append('{result:.20f}'.format(result = tmpr))

            popflag = True

        return float(self.opslist[0])
                
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
    print rpnins4
    print rpnins4.solve()

    istr5 = '0.2 10.24 pi * 180 / * 10.24 pi * 180'
    rpnins5 = Rpn(istr5)
    print rpnins5
    print rpnins5.solve()

def main():
    test()

if __name__ == '__main__':
    main()
