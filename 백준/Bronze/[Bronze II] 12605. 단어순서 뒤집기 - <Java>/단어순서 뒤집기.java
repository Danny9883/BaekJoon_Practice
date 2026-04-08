import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in   = new Scanner(System.in);
		int       t    = in.nextInt();
		String aaa    = in.nextLine();
		for (int i = 1; i <= t; i++) {
			String []text = in.nextLine().split(" ");
			String ans = "Case #"+i+": ";
			for (int j = (text.length)-1; j >= 0; j--) {
				ans += text[j]+" ";
			}
			System.out.println(ans);
		}
	
	}
}
