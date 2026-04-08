import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader   br   = new BufferedReader(new InputStreamReader(System.in));
		Scanner          in   = new Scanner(System.in);
		
		int a = in.nextInt();
		if (a % 2 == 0)
			System.out.println("Duck");
		else
			System.out.println("Goose");
	
		
		br.close();
			
		
			
			
	}

}
