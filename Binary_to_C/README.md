# BINARY_TO_C
Binary_to_C is a script that takes any binary data from file and convert it to an array of char type.
This array can be used inside of a C program.  In totality, the data does not have to be strictly binary (music, image, etc),
it can also be text.  As a matter of fact, the data can be anything.

To run the script, a file containing the data (to which you wish to turn into a C array) is specified.
In the below examples, our input file is 'input.txt', output is 'output.txt' and 'binary.c' demonstrates use.

Running the script as below would create your array with default configurations.  The default configurations are:
'decimal char values', '10 columns' and 'output to the screen'.

'input.txt':
```text
This is a demonstration binary file.  It can be anything: music, image, document, etc.
If it can be stored in a file, binary_to_c.py can convert to a C array.
```

Simple run:
```bash
python binary_to_c.py input.txt
```

The above bash call would produce the following from 'input.txt' to the terminal screen:
```c
char binary [159] = {
	 84, 104, 105, 115,  32, 105, 115,  32,  97,  32, 
	100, 101, 109, 111, 110, 115, 116, 114,  97, 116, 
	105, 111, 110,  32,  98, 105, 110,  97, 114, 121, 
	 32, 102, 105, 108, 101,  46,  32,  32,  73, 116, 
	 32,  99,  97, 110,  32,  98, 101,  32,  97, 110, 
	121, 116, 104, 105, 110, 103,  58,  32, 109, 117, 
	115, 105,  99,  44,  32, 105, 109,  97, 103, 101, 
	 44,  32, 100, 111,  99, 117, 109, 101, 110, 116, 
	 44,  32, 101, 116,  99,  46,  10,  73, 102,  32, 
	105, 116,  32,  99,  97, 110,  32,  98, 101,  32, 
	115, 116, 111, 114, 101, 100,  32, 105, 110,  32, 
	 97,  32, 102, 105, 108, 101,  44,  32,  98, 105, 
	110,  97, 114, 121,  95, 116, 111,  95,  99,  46, 
	112, 121,  32,  99,  97, 110,  32,  99, 111, 110, 
	118, 101, 114, 116,  32, 116, 111,  32,  97,  32, 
	 67,  32,  97, 114, 114,  97, 121,  46,  10
};
```

We can change from decimal number to hexadecimal using the 'hex' command. 1 is for lower-case hex and 2 is for upper-case hex:

Running `python binary_to_c.py input.txt -hex=1` produces:
```c
char binary [159] = {
	0x54, 0x68, 0x69, 0x73, 0x20, 0x69, 0x73, 0x20, 0x61, 0x20, 
	0x64, 0x65, 0x6d, 0x6f, 0x6e, 0x73, 0x74, 0x72, 0x61, 0x74, 
	0x69, 0x6f, 0x6e, 0x20, 0x62, 0x69, 0x6e, 0x61, 0x72, 0x79, 
	0x20, 0x66, 0x69, 0x6c, 0x65, 0x2e, 0x20, 0x20, 0x49, 0x74, 
	0x20, 0x63, 0x61, 0x6e, 0x20, 0x62, 0x65, 0x20, 0x61, 0x6e, 
	0x79, 0x74, 0x68, 0x69, 0x6e, 0x67, 0x3a, 0x20, 0x6d, 0x75, 
	0x73, 0x69, 0x63, 0x2c, 0x20, 0x69, 0x6d, 0x61, 0x67, 0x65, 
	0x2c, 0x20, 0x64, 0x6f, 0x63, 0x75, 0x6d, 0x65, 0x6e, 0x74, 
	0x2c, 0x20, 0x65, 0x74, 0x63, 0x2e, 0x0a, 0x49, 0x66, 0x20, 
	0x69, 0x74, 0x20, 0x63, 0x61, 0x6e, 0x20, 0x62, 0x65, 0x20, 
	0x73, 0x74, 0x6f, 0x72, 0x65, 0x64, 0x20, 0x69, 0x6e, 0x20, 
	0x61, 0x20, 0x66, 0x69, 0x6c, 0x65, 0x2c, 0x20, 0x62, 0x69, 
	0x6e, 0x61, 0x72, 0x79, 0x5f, 0x74, 0x6f, 0x5f, 0x63, 0x2e, 
	0x70, 0x79, 0x20, 0x63, 0x61, 0x6e, 0x20, 0x63, 0x6f, 0x6e, 
	0x76, 0x65, 0x72, 0x74, 0x20, 0x74, 0x6f, 0x20, 0x61, 0x20, 
	0x43, 0x20, 0x61, 0x72, 0x72, 0x61, 0x79, 0x2e, 0x0a
};
```

Running `python binary_to_c.py input.txt -hex=2` produces:
```c
char binary [159] = {
	0x54, 0x68, 0x69, 0x73, 0x20, 0x69, 0x73, 0x20, 0x61, 0x20, 
	0x64, 0x65, 0x6D, 0x6F, 0x6E, 0x73, 0x74, 0x72, 0x61, 0x74, 
	0x69, 0x6F, 0x6E, 0x20, 0x62, 0x69, 0x6E, 0x61, 0x72, 0x79, 
	0x20, 0x66, 0x69, 0x6C, 0x65, 0x2E, 0x20, 0x20, 0x49, 0x74, 
	0x20, 0x63, 0x61, 0x6E, 0x20, 0x62, 0x65, 0x20, 0x61, 0x6E, 
	0x79, 0x74, 0x68, 0x69, 0x6E, 0x67, 0x3A, 0x20, 0x6D, 0x75, 
	0x73, 0x69, 0x63, 0x2C, 0x20, 0x69, 0x6D, 0x61, 0x67, 0x65, 
	0x2C, 0x20, 0x64, 0x6F, 0x63, 0x75, 0x6D, 0x65, 0x6E, 0x74, 
	0x2C, 0x20, 0x65, 0x74, 0x63, 0x2E, 0x0A, 0x49, 0x66, 0x20, 
	0x69, 0x74, 0x20, 0x63, 0x61, 0x6E, 0x20, 0x62, 0x65, 0x20, 
	0x73, 0x74, 0x6F, 0x72, 0x65, 0x64, 0x20, 0x69, 0x6E, 0x20, 
	0x61, 0x20, 0x66, 0x69, 0x6C, 0x65, 0x2C, 0x20, 0x62, 0x69, 
	0x6E, 0x61, 0x72, 0x79, 0x5F, 0x74, 0x6F, 0x5F, 0x63, 0x2E, 
	0x70, 0x79, 0x20, 0x63, 0x61, 0x6E, 0x20, 0x63, 0x6F, 0x6E, 
	0x76, 0x65, 0x72, 0x74, 0x20, 0x74, 0x6F, 0x20, 0x61, 0x20, 
	0x43, 0x20, 0x61, 0x72, 0x72, 0x61, 0x79, 0x2E, 0x0A
};
```

You can control the column.  Set any number for the column you want.  Setting 0 will
give a single row with many columns.  For the column example, we are gonna leave off 
the hex command (Leaving it off is the default and is equivalent to decimal or hex=0).
The default column is 10.

Running `python binary_to_c.py input.txt -column=0` produces:
```c
char binary [159] = {
	 84, 104, 105, 115,  32, 105, 115,  32,  97,  32, 100, 101, 109, 111, 110, 115, 116, 114,  97, 116, 105, 111, 110,  32,  98, 105, 110,  97, 114, 121,  32, 102, 105, 108, 101,  46,  32,  32,  73, 116,  32,  99,  97, 110,  32,  98, 101,  32,  97, 110, 121, 116, 104, 105, 110, 103,  58,  32, 109, 117, 115, 105,  99,  44,  32, 105, 109,  97, 103, 101,  44,  32, 100, 111,  99, 117, 109, 101, 110, 116,  44,  32, 101, 116,  99,  46,  10,  73, 102,  32, 105, 116,  32,  99,  97, 110,  32,  98, 101,  32, 115, 116, 111, 114, 101, 100,  32, 105, 110,  32,  97,  32, 102, 105, 108, 101,  44,  32,  98, 105, 110,  97, 114, 121,  95, 116, 111,  95,  99,  46, 112, 121,  32,  99,  97, 110,  32,  99, 111, 110, 118, 101, 114, 116,  32, 116, 111,  32,  97,  32,  67,  32,  97, 114, 114,  97, 121,  46,  10
};
```

Running `python binary_to_c.py input.txt -column=4` produces:
```c
char binary [159] = {
	 84, 104, 105, 115, 
	 32, 105, 115,  32, 
	 97,  32, 100, 101, 
	109, 111, 110, 115, 
	116, 114,  97, 116, 
	105, 111, 110,  32, 
	 98, 105, 110,  97, 
	114, 121,  32, 102, 
	105, 108, 101,  46, 
	 32,  32,  73, 116, 
	 32,  99,  97, 110, 
	 32,  98, 101,  32, 
	 97, 110, 121, 116, 
	104, 105, 110, 103, 
	 58,  32, 109, 117, 
	115, 105,  99,  44, 
	 32, 105, 109,  97, 
	103, 101,  44,  32, 
	100, 111,  99, 117, 
	109, 101, 110, 116, 
	 44,  32, 101, 116, 
	 99,  46,  10,  73, 
	102,  32, 105, 116, 
	 32,  99,  97, 110, 
	 32,  98, 101,  32, 
	115, 116, 111, 114, 
	101, 100,  32, 105, 
	110,  32,  97,  32, 
	102, 105, 108, 101, 
	 44,  32,  98, 105, 
	110,  97, 114, 121, 
	 95, 116, 111,  95, 
	 99,  46, 112, 121, 
	 32,  99,  97, 110, 
	 32,  99, 111, 110, 
	118, 101, 114, 116, 
	 32, 116, 111,  32, 
	 97,  32,  67,  32, 
	 97, 114, 114,  97, 
	121,  46,  10
};
```

Running `python binary_to_c.py input.txt -column=20` produces:
```c
char binary [159] = {
	 84, 104, 105, 115,  32, 105, 115,  32,  97,  32, 100, 101, 109, 111, 110, 115, 116, 114,  97, 116, 
	105, 111, 110,  32,  98, 105, 110,  97, 114, 121,  32, 102, 105, 108, 101,  46,  32,  32,  73, 116, 
	 32,  99,  97, 110,  32,  98, 101,  32,  97, 110, 121, 116, 104, 105, 110, 103,  58,  32, 109, 117, 
	115, 105,  99,  44,  32, 105, 109,  97, 103, 101,  44,  32, 100, 111,  99, 117, 109, 101, 110, 116, 
	 44,  32, 101, 116,  99,  46,  10,  73, 102,  32, 105, 116,  32,  99,  97, 110,  32,  98, 101,  32, 
	115, 116, 111, 114, 101, 100,  32, 105, 110,  32,  97,  32, 102, 105, 108, 101,  44,  32,  98, 105, 
	110,  97, 114, 121,  95, 116, 111,  95,  99,  46, 112, 121,  32,  99,  97, 110,  32,  99, 111, 110, 
	118, 101, 114, 116,  32, 116, 111,  32,  97,  32,  67,  32,  97, 114, 114,  97, 121,  46,  10
};
```

Instead of having the script print the array to the screen, you can print it to a file.  
You specify that file with the output command.  

Simply: `python binary_to_c.py input.txt -output=output.txt`

The source [binary.c](binary.c) demonstrates the use as shown below:

```c
#include <stdio.h>

//Copy the binary here
char binary [159] = {
	0x54, 0x68, 0x69, 0x73, 0x20, 0x69, 0x73, 0x20, 0x61, 0x20, 0x64, 0x65, 0x6d, 0x6f, 0x6e, 
	0x73, 0x74, 0x72, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x20, 0x62, 0x69, 0x6e, 0x61, 0x72, 0x79, 
	0x20, 0x66, 0x69, 0x6c, 0x65, 0x2e, 0x20, 0x20, 0x49, 0x74, 0x20, 0x63, 0x61, 0x6e, 0x20, 
	0x62, 0x65, 0x20, 0x61, 0x6e, 0x79, 0x74, 0x68, 0x69, 0x6e, 0x67, 0x3a, 0x20, 0x6d, 0x75, 
	0x73, 0x69, 0x63, 0x2c, 0x20, 0x69, 0x6d, 0x61, 0x67, 0x65, 0x2c, 0x20, 0x64, 0x6f, 0x63, 
	0x75, 0x6d, 0x65, 0x6e, 0x74, 0x2c, 0x20, 0x65, 0x74, 0x63, 0x2e, 0x0a, 0x49, 0x66, 0x20, 
	0x69, 0x74, 0x20, 0x63, 0x61, 0x6e, 0x20, 0x62, 0x65, 0x20, 0x73, 0x74, 0x6f, 0x72, 0x65, 
	0x64, 0x20, 0x69, 0x6e, 0x20, 0x61, 0x20, 0x66, 0x69, 0x6c, 0x65, 0x2c, 0x20, 0x62, 0x69, 
	0x6e, 0x61, 0x72, 0x79, 0x5f, 0x74, 0x6f, 0x5f, 0x63, 0x2e, 0x70, 0x79, 0x20, 0x63, 0x61, 
	0x6e, 0x20, 0x63, 0x6f, 0x6e, 0x76, 0x65, 0x72, 0x74, 0x20, 0x74, 0x6f, 0x20, 0x61, 0x20, 
	0x43, 0x20, 0x61, 0x72, 0x72, 0x61, 0x79, 0x2e, 0x0a
};

int main() {

	//You can now use it in your logic.
	//As you can see, you read it from you app, not a file.
	//You ofcourse, can change the variable name and remove the array initialization size
	for(unsigned int i = 0; i < 159; i++) {

		printf("%c", binary[i]);
	}

	return 0;
}
```

## License
This project is licensed under the Algodal License - see the [eula.txt](eula.txt) file for details.
In summary, Algodal is the sole proprietor of this project.

## Version
Details of the current version of this project can be seen in the [version.txt](version.txt) file.

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
