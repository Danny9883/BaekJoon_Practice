import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in   = new Scanner(System.in);
		int a = 0;
		int b = 0;
		for (int i = 3; i > 0; i--) {
			int k = in.nextInt();
			a += k*i;
		}
		for (int i = 3; i > 0; i--) {
			int k = in.nextInt();
			b += k*i;
		}
		if (a>b)
			System.out.println("A");
		else if (a<b)
			System.out.println("B");
		else
			System.out.println("T");
	
	}
}
