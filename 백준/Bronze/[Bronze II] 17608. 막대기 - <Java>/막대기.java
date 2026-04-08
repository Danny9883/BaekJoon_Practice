import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in   = new Scanner(System.in);
		int       t    = in.nextInt();
		int   [] stick = new int[t];
		for (int i = 0; i < stick.length; i++) {
			stick[i] = in.nextInt();
		}
		int max = 0;
		int count = 0;
		for (int i = (stick.length)-1; i >= 0; i--) {
			if (stick[i]>max) {
				count += 1;
				max = stick[i]; } 			
		}
		System.out.println(count);
		
		
	}
}
