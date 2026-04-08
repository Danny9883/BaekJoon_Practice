import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner   in   = new Scanner(System.in);
		
		String [] li = in.nextLine().split("-");
		int y        = Integer.parseInt(li[0]);
		int m        = Integer.parseInt(li[1]);
		int d        = Integer.parseInt(li[2]);
		int n        = in.nextInt();
		int day = y*360 + (m-1)*30 + d + n;
		
		int yy = day/360;
		int mm = (day%360)/30 + 1 ;
		int dd = (day%360)%30;
		if (dd==0) {
			dd=30;
			mm--;
			if (mm==0) {
				mm=12;
				yy--;
				
			}
		} 
		
		System.out.printf("%d-%02d-%02d",yy,mm,dd);
		
		
	
		

		
		

		
	}

}
