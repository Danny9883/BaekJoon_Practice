import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader   in   = new BufferedReader(new InputStreamReader(System.in));
		
		int t = Integer.parseInt(in.readLine());
		
		List<Integer> li = new ArrayList<>();
		
		for (int i = 0; i < t; i++) {
			String line   = in.readLine();
			String [] li2 = line.split(" ");
			li2[0] = li2[0].trim();
			if (li2[0].equals("push_back")) {
				int a = Integer.parseInt(li2[1].trim());
				li.add(a);
			} else if (li2[0].equals("push_front")) {
				int a = Integer.parseInt(li2[1].trim());
				li.add(0,a);
			} else if (li2[0].equals("pop_front")) {
				if (li.size()==0) {
					System.out.println(-1);
				} else {
					System.out.println(li.remove(0));}
			} else if (li2[0].equals("pop_back")) {
				if (li.size()==0) {
					System.out.println(-1);
				}else {
					System.out.println(li.remove(li.size()-1));}
			} else if (li2[0].equals("size")) {
				System.out.println(li.size());
			} else if (li2[0].equals("empty")) {
				if (li.isEmpty()) {
					System.out.println(1);
				}else {
					System.out.println(0);}
			} else if (li2[0].equals("front")) {
				if (li.size()==0) {
					System.out.println(-1);
				}else {
					System.out.println(li.get(0));}
			} else if (li2[0].equals("back")) {
				if (li.size()==0) {
					System.out.println(-1);
				}else {
					System.out.println(li.get(li.size()-1));}
			}
		 	
			
			
			
			
		}

		
		in.close();
			
		
			
			
	}

}
