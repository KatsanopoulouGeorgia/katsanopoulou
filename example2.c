#include <stdio.h>
#include <math.h>
#include <string.h>

int main()
{
	char seq[ 1000 ]; 
	int length;
	int count = 0;
	int i;
	float x;

	while( scanf ("%s", seq) == 1 )
	{
	count = 0;
	length = 0;
	length = strlen(seq);

		for ( i = 0; i < length; i++ )
		{
			if ( seq[ i ] == 'G' || seq[ i ] == 'C' )
			{
				count++;
			}
		x = 100.0 * count / length ;
		}

	printf("=> The persentance of GC in the sequence is %f\n", x);

	}

}


