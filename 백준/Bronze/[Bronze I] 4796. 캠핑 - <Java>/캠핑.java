import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in   = new Scanner(System.in);
		
		int i = 1;
		while (true) {
			int l = in.nextInt();
			int p = in.nextInt();
			int v = in.nextInt();
			if (l==0)
				break;
			int m = v/p;
			int n = v%p;
			if (n>=l)
				n=l;
			int ans = m*l+n;
			System.out.println("Case "+i+": "+ans);
			i++;
			
		}
			
		
	}

}
