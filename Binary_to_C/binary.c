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