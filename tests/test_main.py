# -*- coding: utf-8 -*-

import unittest
import math

from pyrpn.rpn import Rpn


NPRC = 12

class TestRpn(unittest.TestCase):
    def test_repr(self):
        istr1 = '1 2 + 3 * sin'
        rpnins1 = Rpn(istr1)
        self.assertEqual(istr1, str(rpnins1))

    def test_rpn_simple1(self):
        self.assertAlmostEqual(2, Rpn('1 1 +').solve(), places=NPRC)

    def test_rpn_simple2(self):
        self.assertAlmostEqual(1.5, Rpn('0.5 1 2 + *').solve(), places=NPRC)

    def test_rpn_func1(self):
        istr1 = '1 2 + 3 * sin'
        rpnins1 = Rpn(istr1)
        self.assertAlmostEqual(rpnins1.solve(), math.sin(3*3), places=NPRC)

    def test_rpn_func2(self):
        istr3 = '10 3 1 2 / * - tan'
        rpnins3 = Rpn(istr3)
        self.assertAlmostEqual(rpnins3.solve(), math.tan(10-3*(1.0/2.0)), places=NPRC)

    def test_rpn_sep(self):
        istr3 = '10,3,1,2,/,*,-,tan'
        rpnins3 = Rpn(istr3, ',')
        self.assertAlmostEqual(rpnins3.solve(), math.tan(10-3*(1.0/2.0)), places=NPRC)

    def test_rpn_complex(self):
        istr4 = '0.2 10.24 pi * 180 / * 10.24 pi * 180 / sin /'
        rpnins4 = Rpn(istr4)
        self.assertAlmostEqual(rpnins4.solve(),
                0.2*(10.24*math.pi)/180/math.sin(10.24*math.pi/180), places=NPRC)

    def test_rpn_const_pi(self):
        self.assertAlmostEqual(Rpn('1 pi *').solve(), 3.14159265359, places=NPRC)
        self.assertAlmostEqual(Rpn('1 PI *').solve(), 3.14159265359, places=NPRC)

    def test_rpn_solve_str(self):
        self.assertAlmostEqual(Rpn.solve_rpn('2 cos'), math.cos(2), places=NPRC)

    def test_rpn_sqrt(self):
        self.assertAlmostEqual(Rpn('4.0 sqrt').solve(), math.sqrt(4.0), places=NPRC)
        self.assertAlmostEqual(Rpn('2.0 sqrt').solve(), math.sqrt(2.0), places=NPRC)
        self.assertIsNone(Rpn('-1.0 sqrt').solve())

    def test_rpn_sto(self):
        self.assertAlmostEqual(Rpn('1 2 + sto three').solve(), 3, places=NPRC)
        self.assertAlmostEqual(Rpn('1 2 + sto three pop three sin').solve(), 0.141120008059867, places=NPRC)

