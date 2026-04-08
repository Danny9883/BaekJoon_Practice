import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in   = new Scanner(System.in);
		
		int t = in.nextInt();
		in.nextLine();
		
		int ch = 100;
		int sd = 100;
		for (int i = 1; i <= t; i++) {
			int a = in.nextInt();
			int b = in.nextInt();
			in.nextLine();
			
			if(a>b)
				sd-=a;
			else if (a<b)
				ch-=b;
			
		}
		System.out.println(ch);
		System.out.println(sd);
			
			
			
	}

}
