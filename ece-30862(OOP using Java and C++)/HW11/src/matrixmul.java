import java.util.Random;
import java.util.Scanner;

class matrix{
	int N;
	int[][] Array;
	int start;
	int stop;
	
	public matrix( int size, int str, int stp) throws InvalidN
	{
		N=size;
		if(N%2 != 0)
			throw new InvalidN("Invalid value of N");
		Array =  new int[N][N];
		start =str;
		stop =stp;
	}
	
	public void fill(int N){
		Random rand = new Random();
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<N;j++)
			{
				Array[i][j] = rand.nextInt(5);
			}
		}
	}
}


class multiply extends Thread
{
	
	matrix Z;
	matrix X;
	matrix Y;
	
	multiply(matrix A, matrix B, matrix C, int start, int stop)
	{
		A.start=start;
		A.stop=stop;
		X=A;
		Y=B;
		Z=C;
		start();
	}	
	
	public void run(){
        for (int i = X.start; i < X.stop; i++) 
        { // aRow
        	for (int j =Y.start ; j < Y.stop; j++)
        	{ // bColumn
        		for (int k = Y.start; k < Y.stop; k++) 
        		{ // aColumn
        			Z.Array[i][j] += X.Array[i][k] * Y.Array[k][j];
        		}
        	}
        }
  }
	
}

public class matrixmul
{
	public static void main(String[] args) throws InterruptedException
	{
		int mdim=0;
		long curr=0;
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter the matrix dimension:");
		mdim = scan.nextInt();
		matrix A = null;
		matrix B = null;
		matrix C = null;
		try {
			A = new matrix(mdim,0,mdim);
			B = new matrix(mdim,0,mdim);
			C = new matrix(mdim,0,mdim);
		} catch (InvalidN e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		A.fill(mdim);
		B.fill(mdim);
		curr = System.currentTimeMillis();
		
		// IN THE BELOW SECTION UNCOMMENT BASED ON THE NUMBER OF THREADS YOU WANT TO USE
				
		//////////1 thread////////////////
		//new multiply(A,B,C,0,mdim).join();
		
		//////////2 threads///////////////
		//new multiply(A,B,C,0,mdim/2).join();
		//new multiply(A,B,C,0,mdim/2).join();
		
		//////////4 threads///////////////
//		new multiply(A,B,C,0,mdim/4).join();
//		new multiply(A,B,C,mdim/4,mdim/2).join();
//		new multiply(A,B,C,mdim/2,3*mdim/4).join();;
//		new multiply(A,B,C,3*mdim/4,mdim).join();	
					
		curr = System.currentTimeMillis()-curr;
		System.out.printf("The time taken is " + curr);
		
	}
}

