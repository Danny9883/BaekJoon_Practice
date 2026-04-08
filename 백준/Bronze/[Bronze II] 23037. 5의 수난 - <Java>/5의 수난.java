import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader   br   = new BufferedReader(new InputStreamReader(System.in));
		Scanner          in   = new Scanner(System.in);
		
		int t  = in.nextInt();
		int t1 = t/10000;
		int t2 = t%10000/1000;
		int t3 = t%1000/100;
		int t4 = t%100/10;
		int t5 = t%10;
		int ans = 0;
		ans += t1*t1*t1*t1*t1;
		ans += t2*t2*t2*t2*t2;
		ans += t3*t3*t3*t3*t3;
		ans += t4*t4*t4*t4*t4;
		ans += t5*t5*t5*t5*t5;
		System.out.println(ans);
		
		
		br.close();
			
		
			
			
	}

}
