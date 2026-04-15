import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader   br   = new BufferedReader(new InputStreamReader(System.in));
		Scanner          sc   = new Scanner(System.in);
		
		
		String money = sc.nextLine();
		int    a     = money.length();
		int    m     = Integer.parseInt(money);
		int    cnt   = 0;
		while (true) {
			m *= 2;
			money = String.valueOf(m);
			if(a!=money.length())
				break;
			cnt++;
		}
		System.out.println(cnt);
		
			
			
	}



}
