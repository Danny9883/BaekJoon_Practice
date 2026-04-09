import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader   br   = new BufferedReader(new InputStreamReader(System.in));
		Scanner          in   = new Scanner(System.in);
		
		int t = in.nextInt();
		int a = 0;
		int b = 0;
		int c = 0;
		    
		a = t / 300;
		t %= 300;
		b = t / 60;
		t %= 60;
		c = t / 10;
		t %= 10;
		if ( t > 0 )
			System.out.println(-1);
		else
			System.out.println( a +" "+ b +" "+ c );
		
		
		br.close();
			
		
			
			
	}

}
