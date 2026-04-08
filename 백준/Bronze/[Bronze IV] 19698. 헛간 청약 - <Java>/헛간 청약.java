import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader   br   = new BufferedReader(new InputStreamReader(System.in));
		Scanner          in   = new Scanner(System.in);
		
		int n = in.nextInt();
		int w = in.nextInt();
		int h = in.nextInt();
		int l = in.nextInt();
		int w2 = w/l;
		int h2 = h/l;
		int ans = w2*h2;
		if (ans>=n)
			System.out.println(n);
		else
			System.out.println(ans);
		
		
		
		br.close();
			
		
			
			
	}

}
