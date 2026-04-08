import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in   = new Scanner(System.in);
		
		String t = in.nextLine();
		if (t.equals("N") | t.equals("n"))
			System.out.println("Naver D2");
		else
			System.out.println("Naver Whale");
		
		
	}

}
