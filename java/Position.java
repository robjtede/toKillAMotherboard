public class Position {
	
	private int row = 0;
	private int col = 0;
	
	public Position (int row, int col) {
		this.row = row;
		this.col = col;
	}
	
	public int getRow () {
		return this.row;
	}
	
	public void setRow (int row) {
		this.row = row;
	}
	
	public int getCol () {
		return this.col;
	}
	
	public void setCol (int col) {
		this.col = col;
	}
	
	
	public boolean equals (Position pos) {
		return (this.row == pos.row) && (this.col == pos.col);
	}
	
	public String toString () {
		return "Row: " + this.row + " - Col: " + this.col;
	}
	
}
