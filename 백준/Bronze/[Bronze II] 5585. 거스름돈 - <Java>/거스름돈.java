import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader   br   = new BufferedReader(new InputStreamReader(System.in));
		Scanner          in   = new Scanner(System.in);
		
		int p = in.nextInt();
		int r = 1000 - p;
		int ans = 0;
		
		ans += r/500;
		r %= 500;
		ans += r/100;
		r %= 100;
		ans += r/50;
		r %= 50;
		ans += r/10;
		r %= 10;
		ans += r/5;
		r %= 5;
		ans += r;
		
		System.out.println(ans);
		
		
		br.close();
			
		
			
			
	}

}
