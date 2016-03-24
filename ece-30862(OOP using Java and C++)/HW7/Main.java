import java.io.*;

class Main {

   public static void main(String args[]) {
      char c = 0;
      short s = 1;
      int i = 2;
      float f = 0.0f;
      double df = 1.0;

      B b = new B( );
      D d = new D( );

      System.out.println("Direct calls");
      //d.foo(d, f);  //No such method defined
      //d.foo(c, d, df); //No method can be matched to this call after widening conversions
      d.foo(df); //B.foo(double d)
      d.foo(i); //D.foo(float f)
      //d.foo( ); //No such method defined
      //d.foo(i, d, df); //No method can be matched to this call after widening conversions
      d.foo(c, b, f); //D.foo(int i , B b, float f) //Q
      d.foo(f); //D.foo(float f)
      d.foo(c); //D.foo(float f) //Q
      d.foo(s, d, df);//B.foo(short s, D d,  double df) 
      //d.foo(i, d);//No method can be matched to this call after widening conversions

      System.out.println("b.caller");
      b.caller( ); //B.foo(short s), B.foo(double d)

   }
}
