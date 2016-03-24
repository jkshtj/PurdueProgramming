import java.lang.Float;

class Flt implements Comparable{

   Float f; // the value returned by the value method.

   public Flt(float f) {this.f = new Float(f);}
	
	@Override
	public double value() {
		// TODO Auto-generated method stub
		return (double)f;
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
