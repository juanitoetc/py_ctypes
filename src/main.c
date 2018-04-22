#include <stdio.h>
/*
 * Returns a int value, result of the addition of all element in the int array given.
 */

typedef struct strPolarXY {
	int x;
	int y;
}PolarXY;

int our_function(int num_numbers, int *numbers) {
    int i;
    int sum = 0;
    for (i = 0; i < num_numbers; i++) {
        sum += numbers[i];
    }
    return sum;
}

/*
 * Given an double type array in, of lenght "n" and base pointer "ina", this function return the square value
 * of each element in the pointer of another given base pointer "outa"
 */
void square_array(int n, double* ina, double* outa)
{
    int i;
    for (i=0; i<n; i++){
        outa[i] = ina[i]*ina[i];
    }
}

void structFill (PolarXY* plVariable){
	//Generates a void pointer to the structure
	//PolarXY* plVariable = (PolarXY*) vpArg;
	plVariable->x = 5;
	plVariable->y = 6;
}


