public class Main {

   public static void main(String[] args) {

      B b = new B( );
      D1 d1 = new D1( );
      D2 d2 = new D2( );

//      System.out.println("Base and b calls");
//      B.f1( ); 
//     // B.f2( ); 
//      b.f1( ); 
//     // b.f2( ); 
//      b.f3( ); 
//      //b.f4( ); 
//      //b.f5( ); 
//      b.bCaller( ); //functions called- f1,f2,f3,f4
//      System.out.println(" ");
//
//      System.out.println("D1 and d1 calls");
//      D1.f1( ); 
//      //D1.f2( ); 
//      d1.f1( ); 
//      //d1.f2( ); 
//      d1.f3( ); 
//      //d1.f4( ); 
//      d1.f5( ); 
//      //d1.f6( ); 
//      //d1.f7( ); 
//      d1.d1Caller( ); //functions called - f1,f3,f4,f5,f6
//      System.out.println(" ");
//     
//      System.out.println("d1.bCaller");
//      d1.bCaller( );//functions called-B.f1,B.f2,D.f3,B.f4
//      System.out.println(" ");
//
//      System.out.println("D2 and d2 calls");
//      D2.f1( ); 
//      //D2.f2( ); 
//      d2.f1( ); 
//      //d2.f2( ); 
//      d2.f3( ); 
//      //d2.f4( ); 
//      d2.f5( ); 
//      //d2.f6( ); 
//      d2.f7( ); 
//      d2.d2Caller( );//functions called-f1,f3,f4,f5,f7
//      System.out.println(" ");
      
      b=d1;
      b.func();
    }
}

