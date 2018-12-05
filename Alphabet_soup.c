// ( Heap sorting -- timing is _always_  .LE. N*loh N  )

// Program Heap(Input,Output);

#include <stdio.h>
#include <string.h> // For strlen

#define N_MAX 100

#define \
    PRINT(iNumC,elC) \
    ({ \
	for (j=1; j< (iNumC); j++) { printf("%d ",(elC)[j]); } \
	printf("%d \n",(elC)[(iNumC)]); \
    })

#define \
    SWAP(elTemp,elB) \
    ({ \
	(elTemp)=(elB)[1]; \
	(elB)[1]=(elB)[i]; \
	(elB)[i]=(elTemp); \
    })


typedef int TElement;
int iNumA=0,iNumB=0,i,j;
TElement elTemp;
TElement elA[N_MAX]; // { Source array, tree and result }
TElement elB[N_MAX];
char words[] = "Heap Array sorting by tree building q";
char soup[] = "qwertyuiopasdfghjklzxcvbnm   AHeerray sorting by tree building q";

int FixTree(int iFrom, int iTo, TElement *elA)
{
  TElement elTop, elLeft, elRight;
  int iFromTwice;

  elTop = elA[iFrom];
  for(;;) {
    iFromTwice=iFrom*2;
    if (iFromTwice > iTo) break;
    else {
      elLeft=elA[iFromTwice];
      if (iFromTwice==iTo) { elRight=elLeft; } else { elRight=elA[iFromTwice+1]; }

      if ((elRight>elTop) && (elRight>elLeft)) { elA[iFrom]=elRight; iFrom=iFromTwice+1; }
      else if (elLeft > elTop ) { elA[iFrom]=elLeft; iFrom=iFromTwice; }
      else break;
    }
  }
  elA[iFrom] = elTop;
}

void main(int argc, int *arhv [])
{

// { Read unsorted array of words }
  for (i=0;iNumA < strlen(words);i++) elA[++iNumA] = (int)words[i];

// { Read unsorted array of soup }
  for (i=0;iNumB < strlen(soup);i++) elB[++iNumB] = (int)soup[i];


// { Build a sorting trees }
  for ( i= iNumA >> 1; i >=1; i--) FixTree(i,iNumA,elA);
  for ( i= iNumB >> 1; i >=1; i--) FixTree(i,iNumB,elB);

// { Convert tree to array }
  for (i=iNumA; i>=2; i-- )
  {
    SWAP(elTemp,elA);
    FixTree(1,i-1,elA);
  }

  for (i=iNumB; i>=2; i-- )
  {
    SWAP(elTemp,elB);
    FixTree(1,i-1,elB);
  }

// { Displey the result }
  printf("* Sorted arrays *\n");
  PRINT(iNumA, elA);
  PRINT(iNumB, elB);

  for(i=1,j=1;i<=iNumA;)
  {
    if (elA[i] > elB[j]) { j++;}
    if (elA[i] < elB[j]) { printf("\nFalse1\n");break;}
    if (j > iNumB) { printf("\nFalse3\n");break;}
    if (elA[i]==elB[j])
    {
      if ((elA[i+1] < elB[j+1]) && (i<iNumA)) { printf("\nFalse2\n");break;}
      else if (elA[i+1] >= elB[j+1]) { i++;j++; }
      else {i++;}
      if (i > iNumA) { printf("\nTrue2\n"); break; }
    }
  }
}
