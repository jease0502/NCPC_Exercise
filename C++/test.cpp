#include <stdio.h>

float count(float a,float b,float c){
	float up,down;
	up = a*b+a*c+b*c;
	down = a*b*c;
	return up/down;
}

int main(void)
{
	float a,b,c,need,tmp;
	scanf("%f",&need);
	float i=1,j=1,k=1;
	for(i=1;i<=2000;i++){
		for(j=i;1<=2000;j++)
		{
			for(k=j;1<=2000;k++){
				tmp = count(i,j,k);
				if(1/need == tmp){
					printf("%d,%d,%d",i,j,k);
				}
			}
		}
	}
 } 
