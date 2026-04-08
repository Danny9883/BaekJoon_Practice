import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in   = new Scanner(System.in);
		int      a1    = in.nextInt();
		int      a2    = in.nextInt();
		int      t     = 0;
		int      max   = 0;
		if (a1>=a2)
			t = a1;
		else
			t = a2;
		int [] score1  = new int[t];
		int [] score2  = new int[t];
		for (int i = 0; i < a1; i++) {
			score1[i] = in.nextInt();
		}
		for (int i = 0; i < a2; i++) {
			score2[i] = in.nextInt();
		}
		for (int i = 0; i < t; i++) {
			if (score2[i]-score1[i]>max)
				max = score2[i]-score1[i];
		}
		System.out.println(max);

		
	
	}
}
