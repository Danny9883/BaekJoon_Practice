import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader   br   = new BufferedReader(new InputStreamReader(System.in));
		
		String line = br.readLine();
		String [] li = line.split(",");
		int sum = 0;
		for (String s: li) {
			sum += Integer.parseInt(s);
		}
		System.out.println(sum);
		
		
		
		br.close();
			
		
			
			
	}

}
