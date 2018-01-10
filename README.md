## pyrpn
![travisci](https://travis-ci.org/archman/pyrpn.svg?branch=master)
![python2.7](https://img.shields.io/badge/Python-2.7-green.svg)
![python3.5](https://img.shields.io/badge/Python-3.5-green.svg)
![python3.6](https://img.shields.io/badge/Python-3.6-green.svg)

Reverse Polish Notation calculator by python.

* Builtin operations:
  * `+`, `-`, `*`, `/`, `sin`, `cos`, `tan`, `sqrt`
* Constants:
  * `pi`
* Other operations could be added (development)
* Shell script command: `pyrpn`

### Examples

* Use `pyrpn` in Python (2.7, 3.5, 3.6) terminal:

```Python
>>> from pyrpn.rpn import Rpn
>>> Rpn('1 2 +').solve()
3.0
>>> Rpn('30 180 / pi * cos').solve()
0.8660254037844214
>>> Rpn('0.2 10.24 pi * 180 / * 10.24 pi * 180 / sin /').solve()
0.20106869612225164
>>> Rpn.solve_rpn('1 2 +')
3.0
```

* Use `pyrpn` in Linux terminal:
```Shell
$ pyrpn
Welcome to RPN calculator, powered by Python, created by Tong Zhang (2016-02).
pyrpn shell > 1 2 +
pyrpn shell > 3.0000000000000000
```
