#ifndef _SANDPILES_
#define _SANDPILES_

#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>


/* ------ Prototypes -------- */

void sandpiles_sum(int grid1[3][3], int grid2[3][3]);
void grid_add(int grid1[3][3], int grid2[3][3]);
void grid_print(int grid[3][3]);
int grid_stable(int grid[3][3]);
void grid_not_stable(int grid1[3][3]);


#endif
