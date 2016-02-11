public class Warehouse extends Location {
	
	private int[] stock;
	private int[] available;
	
	public Warehouse (int[] stock) {
		super();
		this.stock = stock;
	}
	
	public boolean request (int[] products) {
		for (int i=0, j=available.length; i<j; i++) {
			if (available[i] - products[i] < 0) return false;
			available[i] -= products[i];
		}
		
		return true;
	}
	
	public boolean retrieve (int[] products) {
		for (int i=0, j=available.length; i<j; i++) {
			if (stock[i] - products[i] < 0) return false;
			available[i] -= products[i];
		}
		
		return true;
	}
	
}
