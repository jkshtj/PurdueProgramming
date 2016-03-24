import java.io.*;

class MainSimple {

   public static void main(String args[]) {
      Simple s = new Simple( );
      Simple2 s2 = new Simple2( );

      System.out.println("s.x: "+s.x); //Simple.x printed
      System.out.println("s.y: "+s.y); //Simple.y printed
      System.out.println("s2.x: "+s2.x); //Simple2. x printed
      System.out.println("s2.y: "+s2.y); //Simple2.y printed

      s = s2;
      System.out.println("s = s2"); System.out.println("");
      System.out.println("s.x: "+s.x); // 0, field of Simple object  
      System.out.println("s.y: "+s.y); // 0, field of Simple object 
      System.out.println("s.getX(): "+s.getX( )); // getX( ) is in Simple2   
                                                  // object so Simple2 x 
                                                  // printed, i.e., 2
    
      System.out.println("s.getX(): "+s.getX( )); // getY( ) is in Simple2 
                                                  // object so Simple2 y 
                                                  // printed, i.e., 2
      System.out.println("s.y: "+s.y); 
      System.out.println("s2.x: "+s2.x);
      System.out.println("s2.y: "+s2.y);
   }
}
