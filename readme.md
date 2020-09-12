# Date Calculator (Python3)

### Table of Contents

- [Project Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [License](#license)
- [Author Info](#author-info)

---

## Project Description

The objective of this project is to create a program (using Python programming language) 
to calculate the number of full days elapsed in between two events. 

A user enters two separate dates and the program calculates a number of full days between those dates.

#### Design Constraints
The first and the last day are considered partial days and never counted. Following this
logic, the distance between two related events on 03/08/2018 and 04/08/2018 is 0,
since there are no fully elapsed days contained in between those, and 01/01/2000 to
03/01/2000 should return 1.

#### Technologies

Running this program requires Python (version 3.6 and above) interpreter installed 
on their system. If you see a version of Python earlier than Python 3.6, you
may download the latest Python interpreter from https://python.org/

- The repository contains all the necessary files to run the program and 
does not require any external libraries to be downloaded.

#### Contents

**main.py** is used to run the program 
**packages** folder contains a module with the necessary function and class definitions
**test.py** contains a small *unittest* based script to test the program for various input dates
**.gitignore** file contains a list of superfluous files and can be ignore

[Back To The Top](#read-me-template)

---

## How To Use

#### Installation
Once you have the correct Python interpreter installed, open your preferred terminal and change the working directory to the downloaded **date_calculator**.
Once inside the directory, run the following command:

```
python main.py
```
You will be prompted to enter two dates. Please use the following format when entering dates: DD/MM/YYYY

Below is an example of running the programm using a command line.
```html
Enter 'q' at any time to quit.
Please enter First Date using the DD/MM/YYYY format: 20/11/1985
Please enter Second Date using the DD/MM/YYYY format: 11/09/2020
20/11/1985 - 11/09/2020 = 12712 days
```
[Back To The Top](#read-me-template)

---

## Limitations
-- Only valid dates between 01/01/1901 and 31/12/2999 are accepted for input


[Back To The Top](#read-me-template)

---

## License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#read-me-template)