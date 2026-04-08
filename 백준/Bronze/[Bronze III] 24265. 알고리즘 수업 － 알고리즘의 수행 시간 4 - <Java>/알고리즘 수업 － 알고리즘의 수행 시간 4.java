import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader   br   = new BufferedReader(new InputStreamReader(System.in));
		
		long t = Long.parseLong(br.readLine());
		t--;
		long sum = (t*t+t)/2;
		System.out.println(sum+"\n"+2);
	
		br.close();
			
		
			
			
	}

}
