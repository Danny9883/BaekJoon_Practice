import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in   = new Scanner(System.in);
		
		int tt = in.nextInt();
		in.nextLine();
		for (int t = 0; t < tt; t++) {
			int sum = 0 ;
			int min = 101;
			for (int i = 0; i < 7; i++) {
				int a = in.nextInt();
				if (a%2==0) {
					sum += a;
					if ( a<min ) {
						min=a;
					}
				}
			}
			in.nextLine();
			System.out.println(sum+" "+min);
			
			
			
			
			
			
			
			
			
		}
		
	}

}
