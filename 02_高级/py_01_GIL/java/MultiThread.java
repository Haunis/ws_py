//无GIL锁的存在，两个线程占满两个核

public class MultiThread{
	public static void main(String[] args){
		Thread t = new Thread(){
			public void run(){
				while(true){
				}
			}
		};
		t.start();

		while(true){
		
		}	
	}

}
