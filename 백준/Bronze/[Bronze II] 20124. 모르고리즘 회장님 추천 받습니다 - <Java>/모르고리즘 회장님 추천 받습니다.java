import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader   br   = new BufferedReader(new InputStreamReader(System.in));
		Scanner          in   = new Scanner(System.in);
		
		int t = in.nextInt();
		in.nextLine();
		Map<String,Integer> map = new TreeMap<>();
		int max = 0;
		
		for (int i = 0; i < t; i++) {
			String name  = in.next();
			int    score = in.nextInt(); 
			in.nextLine();
			map.put(name, score);
			if (max<score)
				max=score;
		}
		
		
		
		for (Map.Entry<String, Integer> entry : map.entrySet()) {
			String key = entry.getKey();
			Integer val = entry.getValue();
			if (val==max) {
				System.out.println(key);
				break;}
		}
	
		
		br.close();
			
		
			
			
	}

}
