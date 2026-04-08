import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in   = new Scanner(System.in);
		
		int t = in.nextInt();
		in.nextLine();
		
		while (true) {
			if (t==1) {
				System.out.println(1);
				break;}
			if (t%2==0)
				t/=2;
			else {
				System.out.println(0);
				break;}
				
		}
			
			
			
		
			
			
	}

}
