import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in   = new Scanner(System.in);
		
		int t = in.nextInt();
		in.nextLine();
		
		for (int i = 0; i < t; i++) {
			
			String n = in.nextLine();
			int    a = n.charAt(n.length()-1);
			if (a%2==0)
				System.out.println("even");
			else
				System.out.println("odd");
			
			
		}
			
			
			
			
	}

}
