import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in   = new Scanner(System.in);
		
		int t = in.nextInt();
		in.nextLine();
		
		for (int i = 1; i <= t; i++) {
			int max = 0;
			int a = in.nextInt();
			if (a>max)
				max=a;
			int b = in.nextInt();
			if (b>max)
				max=b;
			int c = in.nextInt();
			if (c>max)
				max=c;
			in.nextLine();
			String text = "";
			if (a*a+b*b+c*c==max*max*2)
				text = "yes";
			else
				text = "no";
			System.out.println("Scenario #"+i+":");
			System.out.println(text);
			System.out.println();
			
		}
			
			
			
			
	}

}
