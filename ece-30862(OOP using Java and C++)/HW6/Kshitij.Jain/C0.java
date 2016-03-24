import java.io.*;

public class C0 {

   public Integer a;
   public Integer b;
   public int x;
   public int y;

   public C0( ) {
      this.x = 0;
      y = 0;

      a = new Integer(0);
      b = new Integer(0);
   }
      
   public C0(int x, int yy) {
      this.x = x;
      y = yy;

      a = new Integer(x);
      b = new Integer(y);
   }

   public int getA( ) {
      return -a.intValue( );
   }

   public int getB( ) {
      return -b.intValue( );
   }

   public int getX( ) {
      return -x;
   }

   public int getY( ) {
      return -y;
   }
}
