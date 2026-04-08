import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader   br   = new BufferedReader(new InputStreamReader(System.in));
		Scanner          in   = new Scanner(System.in);
		
		double d1 = in.nextDouble();
		double d2 = in.nextDouble();
		double d3 = in.nextDouble();
		double a = (d1+d2-d3)/2;
		double b = (d1+d3-d2)/2;
		double c = (d2+d3-d1)/2;
		if (a<=0 || b<=0 || c<=0) {
			System.out.println(-1);
		} else {
			System.out.printf("1\n%.1f %.1f %.1f",a,b,c);			
		}
	
		
		br.close();
			
		
			
			
	}

}
