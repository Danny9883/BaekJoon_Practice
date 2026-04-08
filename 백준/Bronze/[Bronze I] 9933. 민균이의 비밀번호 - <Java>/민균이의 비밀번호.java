import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in   = new Scanner(System.in);
		int       t    = in.nextInt();
		String   buf   = in.nextLine();
		int   anslen=0;
		String  ans="";
		String[]passli = new String[t];
		for (int i = 0; i < passli.length; i++) {
			passli[i] = in.nextLine();
		}
		for (int i = 0; i < passli.length; i++) {
			for (String s : passli) {
				StringBuffer sb = new StringBuffer(s);
				String r = sb.reverse().toString();
				if (passli[i].equals(r)) {
					anslen = r.length();
					ans = passli[i];
				}
			}
		}
		char[] ansli = ans.toCharArray();
		System.out.println(anslen+" "+ansli[anslen/2]);
		
		
		
	}
}
