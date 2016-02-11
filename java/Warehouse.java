public class Warehouse extends Location {
	
	private int[] stock;
	private int[] available;
	
	public Warehouse (Position pos, int[] stock) {
		super(pos);
		this.stock = stock;
	}
	
}
