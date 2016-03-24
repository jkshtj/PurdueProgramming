import java.lang.String;
class Hex implements Comparable {

   // I don't give a way to change these values so I don't expect them to
   // change.  Making them final will have the compiler give an error if
   // I write code that makes them change, forcing me to see if my old
   // assumptions still hold.
   final int intValue;
   final double doubleValue;

   // WARNING -- this only works with positive numbers.
   // SHould really use an exception and not just negate n.
   // 
   // Demonstrates the use of the switch statement and mod operator.
   public static final String toHex(int n) {
      final int numLen = 8;
      int d = numLen-1;
      char[ ] h = new char[numLen];
      if (n < 0) n = -1;
      while (n > 0) {
         int r = n % 16;
         n = n / 16;
         switch (r) {
            case 0: h[d] = '0';
                    break;
            case 1: h[d] = '1';
                    break;
            case 2: h[d] = '2';
                    break;
            case 3: h[d] = '3';
                    break;
            case 4: h[d] = '4';
                    break;
            case 5: h[d] = '5';
                    break;
            case 6: h[d] = '6';
                    break;
            case 7: h[d] = '7';
                    break;
            case 8: h[d] = '8';
                    break;
            case 9: h[d] = '9';
                    break;
            case 10: h[d] = 'a';
                    break;
            case 11: h[d] = 'b';
                    break;
            case 12: h[d] = 'c';
                    break;
            case 13: h[d] = 'd';
                    break;
            case 14: h[d] = 'e';
                    break;
            case 15: h[d] = 'f';
                    break;
            default: System.out.println("Something bad happened in toHex case");
                     System.out.println(", r = "+r);
         }
         d--;
      }
      for (; d > -1; d--) h[d] = '0';
      return new String(h);
   }

   // Given a string n representing a hex number, it converts it to an int
   // and assigns the value to object field intValue defined above.
   // It demonstrates the use of the switch statement and various String and
   // array uses.
   public Hex(String n) {
      int val = 0;
      int powerOf16 = 1;
      char[ ] cArray = new char[n.length( )];

      n = n.toLowerCase( );
      n.getChars(0, n.length( ), cArray, 0);

      for (int i = n.length( )-1; i > -1; i--) {
         switch (cArray[i]) {
             case '0': powerOf16 = powerOf16*16;
                       break;
             case '1': val = val + 1*powerOf16;
                       powerOf16 = powerOf16*16;
                       break;
             case '2': val = val + 2*powerOf16;
                       powerOf16 = powerOf16*16;
                       break;
             case '3': val = val + 3*powerOf16;
                       powerOf16 = powerOf16*16;
                       break;
             case '4': val = val + 4*powerOf16;
                       powerOf16 = powerOf16*16;
                       break;
             case '5': val = val + 5*powerOf16;
                       powerOf16 = powerOf16*16;
                       break;
             case '6': val = val + 6*powerOf16;
                       powerOf16 = powerOf16*16;
                       break;
             case '7': val = val + 7*powerOf16;
                       powerOf16 = powerOf16*16;
                       break;
             case '8': val = val + 8*powerOf16;
                       powerOf16 = powerOf16*16;
                       break;
             case '9': val = val + 9*powerOf16;
                       powerOf16 = powerOf16*16;
                       break;
             case 'a': val = val + 10*powerOf16;
                       powerOf16 = powerOf16*16;
                       break;
             case 'b': val = val + 11*powerOf16;
                       powerOf16 = powerOf16*16;
                       break;
             case 'c': val = val + 12*powerOf16;
                       powerOf16 = powerOf16*16;
                       break;
             case 'd': val = val + 13*powerOf16;
                       powerOf16 = powerOf16*16;
                       break;
             case 'e': val = val + 14*powerOf16;
                       powerOf16 = powerOf16*16;
                       break;
             case 'f': val = val + 15*powerOf16;
                       powerOf16 = powerOf16*16;
                       break;
             default: System.out.println("Invalid Character cArray["+i+"] \""+cArray[i]+"\" found.");
                      System.out.println("cAarray = "+new String(cArray));
                      break;
         }
      }
      intValue = val;
      doubleValue = (double) val;
   }
   // Need to define the various interface functions here.
	
	@Override
	public double value() {
		// TODO Auto-generated method stub
		return doubleValue;
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
