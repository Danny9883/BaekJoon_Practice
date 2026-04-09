import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader   br   = new BufferedReader(new InputStreamReader(System.in));
		Scanner          in   = new Scanner(System.in);
		
		int n = in.nextInt();
		int h = in.nextInt();
		int [] c = new int[n];
		boolean isNotKill = true;
		for (int i = 0; i < n; i++) {
			c[i] = in.nextInt();
			h -= c[i];
			if (h<=0) {
				System.out.println(i+1);
				isNotKill = false;
				break;
			}
		}
		if (isNotKill)
			System.out.println(-1);
			

		
		
		br.close();
			
		
			
			
	}

}
