#include <stdlib.h>
#include <stdio.h>
#include <string.h>

//Paste String Here (using default options)
//you could of paste the string starting here if you wanted; C does not care
char stringVar[] = 
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
"}"; //Remember to add ';' for variables

//Paste String Here (define=on)
//paste string starting here or use a trailing slash (like in this case)
#define stringDef \
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

//Paste String Here (param=on, define=on)
//'param=on' doubles '%'; this allows me to use the string in a format without clashing with any '%' format symbols
//C prefers defines, rather than variables, to be used as format strings
#define comment \
"/*** This is a format string\nYou will see '%%%%' turn to '%%' when used as format string:\n" /** manually inserted **/ \
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
"}" /*remember to add an extra backslash*/ \
"\n***/\n\n" /** manually inserted **/
; //remember to add for variables

int main() {

	FILE* fv = fopen("stringvar.c", "w");
	if(fv) {

		fprintf(fv, comment);
		fwrite(stringVar, sizeof(char), strlen(stringVar), fv);
		fclose(fv);
	}

	FILE* fd = fopen("stringdef.c", "w");
	if(fv) {

		fprintf(fv, comment);
		fwrite(stringDef, sizeof(char), strlen(stringDef), fd);
		fclose(fd);
	}

	return 0;
}


