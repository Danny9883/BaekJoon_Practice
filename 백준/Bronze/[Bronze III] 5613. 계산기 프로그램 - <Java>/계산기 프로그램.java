import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in   = new Scanner(System.in);
		
		int sum = in.nextInt();
		in.nextLine();
		while (1==1) {
			String t = in.nextLine();
			if (t.equals("=")) {
				System.out.println(sum);
				break;
			}
			switch (t) {
			case "+" : sum += in.nextInt(); in.nextLine(); break;
			case "-" : sum -= in.nextInt(); in.nextLine(); break;
			case "/" : sum /= in.nextInt(); in.nextLine(); break;
			case "*" : sum *= in.nextInt(); in.nextLine(); break;
			}
		}
			
			
			
			
			
			
			
			
			
	}

}
