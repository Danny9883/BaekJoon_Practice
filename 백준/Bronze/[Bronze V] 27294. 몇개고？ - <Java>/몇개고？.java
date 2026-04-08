import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader   br   = new BufferedReader(new InputStreamReader(System.in));
		Scanner          in   = new Scanner(System.in);
		
		int t = in.nextInt();
		int s = in.nextInt();
		if (s==1)
			System.out.println(280);
		else {
			if (12<=t && t<=16)
				System.out.println(320);
			else
				System.out.println(280);
		}
		
		
		br.close();
			
		
			
			
	}

}
