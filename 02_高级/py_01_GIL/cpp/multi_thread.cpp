/*
 * 两个线程占满两个cpu内核资源,无GIL锁的问题
 *
 * 编译： g++ -o mul multi_thread.cpp -lpthread
 */
#include<stdio.h>
#include<pthread.h>
#include<unistd.h> //gettid() ,sleep()

void* dead_loop(void* arg){
	//printf("dead tid = %d\n",gettid());
	while(1){
	}
	return NULL;
}

int main(){
	pthread_t tidp;
	printf("before tidp = %lu\n",tidp);
	int ret = pthread_create(&tidp,NULL,dead_loop,NULL);
	printf("after tidp = %lu\n",tidp);
	printf("sizeof(tidp):%ld\n",sizeof(tidp));

	for(;;){
	}
	return 0;
}
