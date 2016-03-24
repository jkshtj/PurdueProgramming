// A simple demonstration of the existence of the Object class 
// and the hashCode method defined by the Object class.
class Any extends Object implements Comparable{

   final double value;

   public Any( ) {
      value = hashCode( );
   }

	@Override
	public double value() {
		// TODO Auto-generated method stub
		return value;
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



