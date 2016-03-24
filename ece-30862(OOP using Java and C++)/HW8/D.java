public class D extends B implements I {

   public D( ) { };

   public void foo(int j) {}//i = 1;}  // B - i cannot be changed because it is a variable of public static final type. It is not an instance variable.

   public void foo(short s, D d,  double df) {System.out.println("D foo(short, D, double)");}

   public void bar(short s, D d,  double df) {System.out.println("D bar(short, D, double)");}

   public void dPrint( ) {
      System.out.println("i: "+i+", s: "+s);
   }
}

//Q4) Not defining "void foo(short)" does not give us an error because if we pass a short type argument to foo, it will be converted to an int due to widening conversions and thus, there is no need to define the function separately.