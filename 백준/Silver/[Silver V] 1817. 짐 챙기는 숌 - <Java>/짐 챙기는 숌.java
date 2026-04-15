import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader   br   = new BufferedReader(new InputStreamReader(System.in));
		Scanner          sc   = new Scanner(System.in);
		

		int n     = sc.nextInt();
		int m     = sc.nextInt();
		int [] li = new int[n];
		for (int i = 0; i < li.length; i++) {
			li[i] = sc.nextInt();
		}
		
		int cnt = 1;
		if (n==0)
			cnt=0;
		int w   = 0;
		for (int i : li) {
			w += i;
			if (w>m) {
				cnt++;
				w = i;
			}
		}
		
		System.out.println(cnt);
		
		
		
		
		
		br.close();
			
	}



}
