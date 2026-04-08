import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in   = new Scanner(System.in);
		double before = -50;
		while (true) {
			double  t = in.nextDouble();
			if (t==999)
				break;
			if (before==-50)
				before = t;
			else {
				System.out.printf("%.2f\n",(t-before));
				before = t;
			}
		}
		

		
	}
}
