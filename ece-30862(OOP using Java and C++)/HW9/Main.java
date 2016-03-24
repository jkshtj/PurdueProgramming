import java.util.Random;

class Main {

   // One of the worst sorts known, written in one of the world's finest 
   // languages.  This optimized version is taken from Wikipedia.
   static void bubbleSort(Comparable[ ] a) {
      int n = a.length;
      boolean swapped = true;
      while (swapped) {
         swapped = false;
         for (int i = 1; i <= n-1; i++) { 
             // Compare i-1 and i element, swap if i-1 element > i element.
             // set swapped appropriately.
        	 if(a[i-1].value() > a[i].value())
        	 {
        		 swapped = true;
        	 }
         }
         n = n - 1;
      }
   }

   // This demonstrates how you can find the type of an object.
   static String type(Object o) {
      if (o instanceof Any) return "an Any";
      if (o instanceof Hex) return "an Hex";
      if (o instanceof Int) return "an Int";
      if (o instanceof Flt) return "a Flt";
      return "Err";
   }

   public static void main(String args[]) {

      int sortSize = 50;
      Random rand = new Random(0);
      Comparable[ ] compArray = new Comparable[sortSize];

      // Initialize the array to be sorted.
      // shows how to generate random integers in Java.  The Random class
      // can be used to generate many kinds of random sequences.
      for (int i = 0; i < sortSize; i++) {
         int r =  rand.nextInt(4);
         switch (r) {
            case 0: compArray[i] = new Int((r+1)*rand.nextInt( ));
                    break;
            case 1: compArray[i] = new Flt((r+1)*rand.nextInt( ));
                    break;
            case 2: compArray[i] = new Hex(Hex.toHex((r+1)*rand.nextInt( )));
                    break;
            case 3: compArray[i] = new Any( );
                    break;
            default: System.out.print("Something bad happend in Main case");
                     System.out.print("value of r is "+r);
         }
      }

      bubbleSort(compArray);

      // Print out the sorted array and the type of object in each 
      // position of the array.
      for (int i = 0; i < sortSize; i++) {
         System.out.print("compArray["+i+"] is "+type(compArray[i])+" ");
         System.out.println("with a value of "+compArray[i].value( ));
      }
   }
}
