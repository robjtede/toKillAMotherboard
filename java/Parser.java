import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.lang.Integer;

public class Parser {
	
	//Environment env = new Environment();
	
	public Parser(File file) throws FileNotFoundException, IOException {
		BufferedReader bufferedReader = new BufferedReader(new FileReader(file));
		int num = 0;
		
		while((bufferedReader.readLine()) != null) {
			num++;
		}
		
		bufferedReader = new BufferedReader(new FileReader(file));
		
		String data[] = new String[num];
		String line = "";
		
		for(int i = 0; i < num; i++) {
			data[i] = bufferedReader.readLine();
		}
		
		String[] temp;
	
		int rows = Integer.parseInt(data[0].split(" ")[0]);
		int cols = Integer.parseInt(data[0].split(" ")[1]);
		int numDrone = Integer.parseInt(data[0].split(" ")[2]);
		int deadline = Integer.parseInt(data[0].split(" ")[3]);
		int maxLoad = Integer.parseInt(data[0].split(" ")[4]);
		
		int numProdType = Integer.parseInt(data[1]);
		
		temp = data[2].split(" ");
		int[] prodWeights = new int[temp.length];
		for(int i = 0; i < temp.length; i++)
			prodWeights[i] = Integer.parseInt(temp[i]);
		
		int numWarehouse = Integer.parseInt(data[3]);
		
		Warehouse[] stores = new Warehouse[numWarehouse];
		
		Location[][] grid = new Location[rows][cols];
		for(int i = 0; i < rows; i++) {
			for(int j = 0; j < cols; j++) {
				grid[i][j] = null;
			}
		}
		
		for(int i = 4; i < 4 + (2 * numWarehouse); i += 2) {
			temp = data[i + 1].split(" ");
			int[] stock = new int[temp.length];
			for(int j = 0; j < temp.length; j++) {
				stock[j] = Integer.parseInt(temp[j]);
			}
			
			temp = data[i].split(" ");
			
			grid[Integer.parseInt(temp[0])][Integer.parseInt(temp[1])] = new Warehouse(stock);
		}
		
		int numOrders = Integer.parseInt(data[4 + (2 * numWarehouse)]);
		
		
		System.out.println(numOrders);
		for(int i = 4 + (2 * numWarehouse); i < 4 + (2 * numWarehouse) + (3 * numOrders); i += 2) {
			temp = data[i + 1].split(" ");
			int[] stock = new int[temp.length];
			for(int j = 0; j < temp.length; j++) {
				stock[j] = Integer.parseInt(temp[j]);
			}
			
			temp = data[i].split(" ");
		}
		
		/*
							
							ln = ln + (numWarehouses * 2)
						
							numOrders = int(data[ln])
							sim['numOrders'] = numOrders
							ln += 1
						
							# orders
							orders = []
							for x in xrange(ln, ln + (3 * numOrders), 3):
								orders.append({
									'pos': {
										'row': int(data[x].split(" ")[0]),
										'col': int(data[x].split(" ")[1])
									},
									'num': int(data[x + 1]),
									'products': list(map(int, data[x + 2].split(" ")))
								})
							
							sim['orders'] = orders
		*/
		System.out.println(prodWeights[0]);
	}
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		Parser parser = new Parser(new File("../busy_day.in"));
	}
	
	//new Environment(rows, cols, numDr, deadline, maxLoad, numProdType, 
	//public Environment getEnvironment() {
		//return env;
	//}
	
}