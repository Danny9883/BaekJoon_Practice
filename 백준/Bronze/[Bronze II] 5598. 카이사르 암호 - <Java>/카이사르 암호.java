import java.util.Iterator;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in   = new Scanner(System.in);
		String    t    = in.next();
		char  [] text  = t.toCharArray();
		String ans     = "";

		for (char c : text) {
			int a = c;
			if (a<=67)
				a += 23;
			else
				a -= 3;
			ans += (char)a;
		}
		
		System.out.println(ans);


			
	
	
	}
}
