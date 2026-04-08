import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in = new Scanner(System.in);
		String[] a = in.next().split("");
		int count = 0;
		for (int i = 0; i < a.length; i++) {
			int b = Integer.parseInt(a[i]);
			if (b==0)
				count += 9;
			count += b;
		}
		System.out.println(count);

			
	
	
	}
}
