#include <stdio.h>
#include <math.h>
#include <string.h>

int main()
{
	char seq[ 1000 ]; 
	int length;
	int count = 0;
	int i;

	scanf("%s", seq );
	length = strlen( seq );

		for ( i = 0; i < length; i++ )
		{
			if ( seq[ i ] == 'G' || seq[ i ] == 'C' )
			{
				count++;
			}
		}
		printf("=> %f\n", (100.0*count) / length );


}


