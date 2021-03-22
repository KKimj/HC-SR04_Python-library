# HC-SR04_Python-library
HC-SR04_Python-library for PyPi

https://pypi.org/project/HC-SR04

## Getting Started

### Prerequisites

* Arduino board
* HC_SR04 sensors
* #### [porting arduino code to arduino board](https://github.com/KKimj/HC-SR04)
    * https://github.com/KKimj/HC-SR04

### Installation
```
$ pip install HC-SR04
```

## Usage

### Import
```python
from HC_SR04 import HC_SR04 as hc
from HC_SR04 import HC_SR04_fair as hc_fair

tmp = hc()
tmp_fair = hc_fair()
```

```python
import HC_SR04

tmp = HC_SR04.HC_SR04()
tmp_fair = HC_SR04.HC_SR04_fair()
```

```python
from HC_SR04 import HC_SR04_fair
from HC_SR04 import HC_SR04

tmp = HC_SR04()
tmp_fair = HC_SR04_fair()
```

### Examples
```python
from HC_SR04 import HC_SR04 as hc # single board with HC_SR04(1 to many)

my_arduino = hc(channel = 3, open=True) # if open is set True then open Serial connection, default open is False

print(my_arduino.get())
```

```python
from HC_SR04 import HC_SR04_fair # single board with HC_SR04(1 to many)

my_arduino_fair = HC_SR04_fair(channel = 3, port_left = '/dev/ttyUSB3', port_right = '/dev/ttyUSB4')
# call open_serial() before using .get* method()
# or set open = True, e.g., my_arduino_fair = HC_SR04_fair(channel = 3, open = True)
my_arduino_fair.open_serial()

print(my_arduino_fair.get())
print(my_arduino_fair.get_leftside())
print(my_arduino_fair.get_left_sensors())

# print out status of instance
my_arduino_fair.test()
# switch left <-> right 
my_arduino.switch()
# print out status of instance
my_arduino_fair.test()

my_arduino_fair.close_serial()
```


## Dev

### Build
```
$ python3 -m build
```

### Local test
```
$ pip install -e .
```

#### Build and Local test
```
$ python3 -m build && pip install -e . && python
```

### Release
```
$ python -m twine upload dist/*
```
