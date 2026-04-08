import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader   br   = new BufferedReader(new InputStreamReader(System.in));
		Scanner          in   = new Scanner(System.in);
		
		long a = in.nextLong();
		long b = in.nextLong();
		long big;
		long small;
		long ans = 0;
		if (a>b) {
			ans = a-b-1;
			big = a;
			small = b;
		} else if (a<b) {
			ans = b-a-1;
			big = b;
			small = a;
		} else {
			ans = 0;
			big = b;
			small = a;
		}
		System.out.println(ans);
		for (long i = small+1; i < big; i++) {
			System.out.print(i+" ");
		}
		
		br.close();
			
		
			
			
	}

}
