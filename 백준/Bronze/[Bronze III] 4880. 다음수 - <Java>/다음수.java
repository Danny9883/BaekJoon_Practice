import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in   = new Scanner(System.in);
		
		while (1==1) {
			
			int a = in.nextInt();
			int b = in.nextInt();
			int c = in.nextInt();
			in.nextLine();
			
			if (a==0 && b==0)
				break;
			
			if ( b*2 == a+c ) {
				int ans = c*2-b;
				System.out.println("AP "+ ans);
			} else {
				int ans = c*c/b;
				System.out.println("GP "+ ans);
			}
			
			
		} 
			
			
			
			
			
			
			
			
			
	}

}
