import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader   br   = new BufferedReader(new InputStreamReader(System.in));
		Scanner          in   = new Scanner(System.in);
		
		List<Integer> li = new ArrayList<>();
		for (int i = 0; i < 3; i++) {
			int a = in.nextInt();
			li.add(a);
		}
		Collections.sort(li);
		for (Integer i : li) {
			System.out.print(i+" ");
		}
		
		br.close();
			
		
			
			
	}

}
