/*
 *编译生成动态链接库：gcc -shared -o libdead.so test.c
 *必须使用gcc编译 
 */
#include<stdio.h>
#include<unistd.h>

void deadLoop(){
	while(1){
		//sleep(2);
		//printf("deadLoop called \n");
	}
}
