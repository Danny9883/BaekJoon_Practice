import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader   br   = new BufferedReader(new InputStreamReader(System.in));
		Scanner          sc   = new Scanner(System.in);
		
		int t = sc.nextInt();
		int [][] map = new int[501][501];
		
		for (int i = 0; i < t; i++) {
			int x1 = sc.nextInt();
			int y1 = sc.nextInt();
			int x2 = sc.nextInt();
			int y2 = sc.nextInt();
			for (int j = y1; j < y2; j++) {
				for (int k = x1; k < x2; k++) {
					map[j][k] = 1;
				}
			}
		}
		
		int cnt = 0;
		for (int i = 0; i < 501; i++) {
			for (int j = 0; j < 501; j++) {
				if (map[i][j]==1)
					cnt++;
			}
		}
		System.out.println(cnt);
		
		
		br.close();
			
	}



}
