import java.io.*;

class Main {

   public static void main(String args[]) {
      C0 c01 = new C0( );
      C0 c02 = new C0(1,2);
      C1 c11 = new C1( );
      C1 c12 = new C1(3, 4, 5.0f);

      System.out.println("c01.a.intValue( ): " + c01.a.intValue( )); // c01.a printed
      System.out.println("c01.b.intValue( ): " + c01.b.intValue( )); // c01.b printed
      System.out.println("c01.x: " + c01.x); // c01.x printed
      System.out.println("c01.y: " + c01.y); // c01.y printed

      System.out.println("c02.a.intValue( ): " + c02.a.intValue( )); // c02.a printed
      System.out.println("c02.b.intValue( ): " + c02.b.intValue( )); // c02.b printed
      System.out.println("c02.x: " + c02.x); // c02.x printed
      System.out.println("c02.y: " + c02.y); // c02.y printed

      System.out.println("c11.a.intValue( ): " + c11.a.intValue( )); // c11.a printed
      System.out.println("c11.b.intValue( ): " + c11.b.intValue( )); // c11.b printed
      System.out.println("c11.c.floatValue( ): " + c11.c.floatValue( )); // c11.c printed
      System.out.println("c11.x: " + c11.x); // c11.x printed
      System.out.println("c11.y: " + c11.y); // c11.y printed
      System.out.println("c11.z: " + c11.z); // c11.z printed

      c01 = c12;
      System.out.println("c12.a.intValue( ): " + c01.a.intValue( )); //c12.a printed
      System.out.println("c12.b.intValue( ): " + c01.b.intValue( )); //c12.b printed
      System.out.println("c12.c.floatValue( ): " + ((C1) c01).c.floatValue( )); //c12.c printed
      System.out.println("c12.x: " + c01.x);//c01.x printed
      System.out.println("c12.y: " + c01.y);//c01.y printed
      //System.out.println("c12.z: " + c01.z);

      System.out.println("c02.getA( ): " + c02.getA( )); //C0.getA()
      System.out.println("c02.getB( ): " + c02.getB( )); //C0.getB()
      System.out.println("c02.getX( ): " + c02.getX( )); //C0.getX()
      System.out.println("c02.getY( ): " + c02.getY( ));

      System.out.println("c12.getA( ): " + c01.getA( )); //c12.getA()
      System.out.println("c12.getB( ): " + c01.getB( )); //c12.getB()
      System.out.println("c12.getC( ): " + ((C1) c01).getC( )); //c12.getC()
      System.out.println("c12.getX( ): " + c01.getX( ));//c01.getX
      System.out.println("c01.getY( ): " + c01.getY( ));//c12.getY()
      System.out.println("c01.getZ( ): " + c01.getY( ));
   }
}
