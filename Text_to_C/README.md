# text_to_c.py
Python Script that converts any text given to it into a string that can be used directly in C program.

* for help/info, run: python text_to_c.py
* to use, run: python text_to_c.py [file] ;replace [file] with your actual filename, duh
all run will write to a file called 'output.txt' in the working directory

For instance, using the following file, 'input.txt', as our input file and for the text, we will us this C program as its content:
```c
#include <stdio.h>

int main() {
    int intType;
    float floatType;
    double doubleType;
    char charType;

    // sizeof evaluates the size of a variable
    printf("Size of int: %ld bytes\n", sizeof(intType));
    printf("Size of float: %ld bytes\n", sizeof(floatType));
    printf("Size of double: %ld bytes\n", sizeof(doubleType));
    printf("Size of char: %ld byte\n", sizeof(charType));
    
    return 0;
}
```
We will expect these results from these examples:

Example using(default)
```bash
python text_to_c.py input.txt
```
results:
```c
"#include <stdio.h>\n"
"\n"
"int main() {\n"
"    int intType;\n"
"    float floatType;\n"
"    double doubleType;\n"
"    char charType;\n"
"\n"
"    // sizeof evaluates the size of a variable\n"
"    printf(\"Size of int: %ld bytes\\n\", sizeof(intType));\n"
"    printf(\"Size of float: %ld bytes\\n\", sizeof(floatType));\n"
"    printf(\"Size of double: %ld bytes\\n\", sizeof(doubleType));\n"
"    printf(\"Size of char: %ld byte\\n\", sizeof(charType));\n"
"    \n"
"    return 0;\n"
"}"

```
Example using(define=on)
```bash
python text_to_c.py input.txt define=on
```
results:
```c
"#include <stdio.h>\n" \
"\n" \
"int main() {\n" \
"    int intType;\n" \
"    float floatType;\n" \
"    double doubleType;\n" \
"    char charType;\n" \
"\n" \
"    // sizeof evaluates the size of a variable\n" \
"    printf(\"Size of int: %ld bytes\\n\", sizeof(intType));\n" \
"    printf(\"Size of float: %ld bytes\\n\", sizeof(floatType));\n" \
"    printf(\"Size of double: %ld bytes\\n\", sizeof(doubleType));\n" \
"    printf(\"Size of char: %ld byte\\n\", sizeof(charType));\n" \
"    \n" \
"    return 0;\n" \
"}"

```
Example using(define=on, param=on)
```bash
python text_to_c.py input.txt define=on param=on
```
results:
```c
"#include <stdio.h>\n" \
"\n" \
"int main() {\n" \
"    int intType;\n" \
"    float floatType;\n" \
"    double doubleType;\n" \
"    char charType;\n" \
"\n" \
"    // sizeof evaluates the size of a variable\n" \
"    printf(\"Size of int: %%ld bytes\\n\", sizeof(intType));\n" \
"    printf(\"Size of float: %%ld bytes\\n\", sizeof(floatType));\n" \
"    printf(\"Size of double: %%ld bytes\\n\", sizeof(doubleType));\n" \
"    printf(\"Size of char: %%ld byte\\n\", sizeof(charType));\n" \
"    \n" \
"    return 0;\n" \
"}"

```

Example using(escape=off)
```bash
python text_to_c.py input.txt escape=off
```
results
```c
"#include <stdio.h>\n"
"\n"
"int main() {\n"
"    int intType;\n"
"    float floatType;\n"
"    double doubleType;\n"
"    char charType;\n"
"\n"
"    // sizeof evaluates the size of a variable\n"
"    printf(\"Size of int: %ld bytes\n\", sizeof(intType));\n"
"    printf(\"Size of float: %ld bytes\n\", sizeof(floatType));\n"
"    printf(\"Size of double: %ld bytes\n\", sizeof(doubleType));\n"
"    printf(\"Size of char: %ld byte\n\", sizeof(charType));\n"
"    \n"
"    return 0;\n"
"}"
```

## License
This project is licensed under the Zlib License - see the [eula.txt](eula.txt) file for details.
In summary, permission is granted to anyone to use this software for any purpose, including commercial 
applications, and to alter it and redistribute it freely, subject to the specified restrictions.

## Acknowledgments
* Alrick Grandison - Innovative Director
* Almato Godami - Marketing and Finance Director

## Algodal™
[![www.algodal.com](https://i.pinimg.com/originals/94/8e/0b/948e0b76fe239d745ff08d2481b66a4c.png)](https://www.algodal.com)
<br/>
looking towards the creator
<br/><br/><br/>

<a href="https://www.facebook.com/algodalinnovations/"> <img src="https://i.pinimg.com/originals/27/8c/b4/278cb4f35386c4ce87bbc30504c55225.png" width="24" height="24"> </a>
<a href="http://projects-algodal.blogspot.com/"> <img src="https://i.pinimg.com/originals/a2/17/81/a217812576868675ff43d236a84cdde1.png" width="24" height="24"> </a>
<a href="https://github.com/Rickodesea"> <img src="https://i.pinimg.com/originals/d3/b7/39/d3b7395399c3cf77213ed21db8dad572.png" width="24" height="24"> </a>
<br/>
alrickgrandison@algodal.com
<br/><br/>


© All rights reserved.