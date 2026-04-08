import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in = new Scanner(System.in);
		int t = in.nextInt();
		int money = in.nextInt();
		int [] p = new int[t];
		int people =0;
		for (int i = 0; i < t; i++) {
			int a = in.nextInt();
			p[i] = a;
			people += a;
		}
		int m = money / people;
		for (int i = 0; i < t; i++) {
			System.out.println(p[i]*m);
		}

	}

}
