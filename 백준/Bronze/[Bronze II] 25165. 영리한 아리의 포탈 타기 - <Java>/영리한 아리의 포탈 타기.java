import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader   br   = new BufferedReader(new InputStreamReader(System.in));
		Scanner          sc   = new Scanner(System.in);
		
		
		int row      = sc.nextInt();
		int col      = sc.nextInt();
		int [][] map = new int[row][col];
		
		int s        = sc.nextInt()-1;
		int g        = sc.nextInt();
		
		int mr       = sc.nextInt()-1;
		int mc       = sc.nextInt()-1;
		map[mr][mc]  = 1;
		
		ari(s,g,row,col, map);
	

		
	
		
		br.close();
			
		
			
			
	}

	private static void ari(int s, int g, int row, int col, int[][] map) {
		int y = 0 ; 
		int x = s ;
		while (true) {
			if (map[y][x]==1) {
				System.out.println("NO...");
				return;
			}
			if (y==row-1 && x==col-1) {
				System.out.println("YES!");
				return;
			}
			if (g==0) {
				x--;
				if (x<0) {
					x = 0;
					g = 1;
					y++;
				}
			} else {
				x++;
				if (x==col) {
					x = col-1;
					g = 0;
					y++;
				}
			}
				
			
		}
		
		
		
	}


}
