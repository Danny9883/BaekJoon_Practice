import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader   br   = new BufferedReader(new InputStreamReader(System.in));
		Scanner          sc   = new Scanner(System.in);
		
		
		int t = sc.nextInt();
		
		int a = t / 5;
		if(t%5==0)
			System.out.println(a);
		else
			System.out.println(a+1);

		
	
		
		br.close();
			
		
			
			
	}


}
