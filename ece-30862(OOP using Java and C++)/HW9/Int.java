import java.lang.Integer;

class Int implements Comparable{

   Integer i;

   public Int(int j) {i = new Integer(j);}

   // Implement the Comparable interface functions here.
	
	@Override
	public double value() {
		// TODO Auto-generated method stub
		return (double)i;
	}
	
	@Override
	public boolean lessThan(Comparable c) {
		// TODO Auto-generated method stub
		if(this.value() < c.value())
			return true;
		else
			return false;
	}
	
	@Override
	public boolean equal(Comparable c) {
		// TODO Auto-generated method stub
		if(this.value() == c.value())
			return true;
		else
			return false;
	}
	
	@Override
	public boolean greaterThan(Comparable c) {
		// TODO Auto-generated method stub
		if(this.value() > c.value())
			return true;
		else
			return false;
	}

}
