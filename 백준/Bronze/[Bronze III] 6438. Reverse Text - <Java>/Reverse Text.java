import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in   = new Scanner(System.in);
		
		int t = in.nextInt();
		String a = in.nextLine();
		for (int i = 0; i < t; i++) {
			String line = in.nextLine();
			char [] li  = line.toCharArray();
			String text = "";
			for (int j = li.length-1; j >= 0; j--) {
				text += li[j];
			}
			System.out.println(text);
			
			
		}
		
		
	}

}
