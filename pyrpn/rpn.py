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

try:
    basestring
except NameError:
    basestring = str


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
        self.opslist = istr.lower().split(delimiter)
        self.opslist.reverse()

        # initial stored constants
        self.pi = math.pi

        # initial stored operations
        self.operators = ['+', '-', '*', '/',
                          'sin', 'cos', 'tan',
                          'sqrt',
                          'pop', 'swap',
                          'sto',
        ]
        opfun = [self.fadd, self.fsub, self.fmul, self.fdiv,
                 self.fsin, self.fcos, self.ftan, self.fsqrt,
                 self.fpop, self.fswap, self.fsto,
        ]
        self.opdict = dict(zip(self.operators, opfun))

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

    def fpop(self):
        self.tmpopslist.pop()
        return None

    def fswap(self):
        a = self.tmpopslist.pop()
        b = self.tmpopslist.pop()
        self.tmpopslist.append(a)
        self.tmpopslist.append(b)
        return None

    def fsto(self):
        """sto operation.
        """
        a = float(self.tmpopslist.pop())
        var = self.opslist.pop()
        if isinstance(var, basestring):
            setattr(self, var, a)
            return a
        else:
            print("Can only sto into a variable.")
            return 'ERROR'

    def __str__(self):
        return ' '.join(reversed(self.opslist))

    @classmethod
    def solve_rpn(cls, istr):
        """Solve rpn expression.

        USAGE: solve_rpn(rpnstr)

        Parameters
        ----------
        rpnstr : str
            String of rpn expression.

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
        while True:
            while self.opslist and popflag:
                op = self.opslist.pop()
                if self.is_variable(op):
                    op = getattr(self, op)
                if self.is_operator(op):
                    popflag = False
                    break
                self.tmpopslist.append(op)

            # operations
            tmpr = self._get_temp_result(op)
            if tmpr == 'ERROR':
                return None

            if tmpr is not None:
                self.opslist.append('{r:.20f}'.format(r=tmpr))

            if len(self.tmpopslist) > 0 or len(self.opslist) > 1:
                popflag = True
            else:
                break

        return float(self.opslist[0])

    def _get_temp_result(self, op):
        try:
            tmpr = self.opdict[op]()
        except (IndexError, ValueError, KeyError, ZeroDivisionError):
            tmpr = 'ERROR'
        return tmpr

    def is_operator(self, s):
        """Test if *s* is a valid operation.
        """
        return s in self.operators

    def is_variable(self, s):
        """Test if *s* is a defined variable (attribute).
        """
        return hasattr(self, s)


def solve_rpn(istr):
    """Solve rpn expression.

    USAGE: solve_rpn(rpnstr)

    Parameters
    ----------
    rpnstr : str
        String of rpn expression.

    Returns
    -------
    ret : float
        Calculated result.
    """
    return Rpn(istr).solve()


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
