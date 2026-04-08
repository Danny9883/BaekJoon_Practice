import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader   br   = new BufferedReader(new InputStreamReader(System.in));
		
		long t = Long.parseLong(br.readLine());
		long sum = 0;
		for (long i = 1; i <= t-2; i++) {
			sum += (i*i+i)/2;
		}

		System.out.println(sum+"\n"+3);
	
		br.close();
			
		
			
			
	}

}
