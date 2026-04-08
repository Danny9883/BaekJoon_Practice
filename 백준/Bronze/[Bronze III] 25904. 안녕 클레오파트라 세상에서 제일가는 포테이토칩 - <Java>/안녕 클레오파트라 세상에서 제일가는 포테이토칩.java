import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in   = new Scanner(System.in);
		
		int n  = in.nextInt();
		int x  = in.nextInt();
		List<Integer> li = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			int a = in.nextInt();
			li.add(a);
		}
		int i = 0;
		while (true) {
			if(li.get(i)<x) {
				System.out.println(i+1);
				break;
			}
			i++;
			x++;
			if (i == li.size())
				i=0;
		}
		

		
		

		
	}

}
