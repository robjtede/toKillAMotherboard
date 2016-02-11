public class Drone {
	public static int load = 0;
	
	private int clock;
	private Position loc;
	private int[] cargo;
	//private String activity;
	private Activity activity;
	private Controller controller;
	private Environment env;

	public Drone (Position location, int typeCount, Controller c, Environment e)
	{
		loc = location;
		cargo = new int[typeCount];
		activity = "idle";
		this.controller = c;
		this.env = e;
	}

	public Activity getActivity()
	{
		return activity;
	}
	public Position getPosition()
	{
		return loc;
	}
	public void update()
	{
		clock = clock - 1;
		if (clock == 0)
		{
			switch(activity.toString())
			{
				//case "idle":
				//	this.controller.getNextActivity(this);
				//break;
				//case "waiting":
				//	this.activity = "idle";
				//break;
				case "delivering":
					this.env.deliver(this);// Environment's house under this drone should try to extract stuff from the drone
					this.loc = this.activity.pos;
					System.out.println("Drone delivering to " + loc + ".");
				break;
				case "loading":
					this.env.load(this);// Environment's warehouse under this drone should try to shove stuff into the drone
					System.out.println("Drone loading at " + loc + ".");
				break;
				default:
				break;
			}
			this.activity = this.env.getNextActivity(this);
		}
	}

	public static void main(String[] args)
	{
		Drone d = new Drone(new Position(5,6));
	}

}
