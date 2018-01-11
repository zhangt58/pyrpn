#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
python package to handle RPN calculation.
RPN: Reverse Polish Notation
"""

from __future__ import division, print_function
import decimal
import math

decimal.getcontext().prec = 20


class Rpn(object):
    """Class to handle RPN calculation.

    Parameters
    ----------
    istr : str
        String of rpn expression.
    delimiter : str
        Delimiter of *istr*.

    Examples
    --------
    >>> from rpn import Rpn
    >>> rpnstr = '10 1 2 + sin *'
    >>> rpnins = Rpn(rpnstr)
    >>> result = rpnins.solve()
    1.4112000805986722
    >>> # or:
    >>> result = Rpn.solve_rpn(rpnstr)
    """
    def __init__(self, istr, delimiter=None):
        self.opslist = istr.lower().replace('pi',str(math.pi)).split(delimiter)
        self.opslist.reverse()

        oprts = ['+', '-', '*', '/', 'sin', 'cos', 'tan', 'sqrt']
        opfun = [self.fadd, self.fsub, self.fmul, self.fdiv,
                 self.fsin, self.fcos, self.ftan, self.fsqrt]
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
        if a == 0:
            print("The dividend must not be zero.")
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

    def fsqrt(self):
        a = float(self.tmpopslist.pop())
        if a < 0:
            print('Input of sqrt must be a positive number.')
        return math.sqrt(a)

    def __str__(self):
        return ' '.join(reversed(self.opslist))

    @classmethod
    def solve_rpn(cls, istr):
        """Solve rpn expression.

        USAGE: solve_rpn(rpnstr)
        
        Parameters
        ----------
        rpnstr : str
            String o rpn expression.

        Returns
        -------
        ret : float
            Calculated result.
        """
        return cls(istr).solve()

    def solve(self):
        """Solve rpn expression, return None if not valid."""
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
                    return None
            try:
                oprt = self.tmpopslist.pop()
                tmpr = self.opdic[oprt]()
            except (IndexError, ValueError, KeyError, ZeroDivisionError):
                return None
            self.opslist.append('{result:.20f}'.format(result = tmpr))

            popflag = True

        try:
            return float(self.opslist[0])
        except:
            return None
                
def test():
    istr1 = '1 2 + 3 * sin'
    rpnins1 = Rpn(istr1)
    print(rpnins1)
    print(rpnins1.solve())

    istr2 = '1 2 + 3 * cos'
    rpnins2 = Rpn(istr2)
    print(rpnins2)
    print(rpnins2.solve())

    istr3 = '10,3,1,2,/,*,-,tan'
    rpnins3 = Rpn(istr3, ',')
    print(rpnins3)
    print(rpnins3.solve())

    istr4 = '0.2 10.24 pi * 180 / * 10.24 pi * 180 / sin /'
    rpnins4 = Rpn(istr4)
    print(rpnins4)
    print(rpnins4.solve())

    istr5 = '0.2 10.24 pi * 180 / * 10.24 pi * 180'
    rpnins5 = Rpn(istr5)
    print(rpnins5)
    print(rpnins5.solve())

def main():
    test()

if __name__ == '__main__':
    main()
