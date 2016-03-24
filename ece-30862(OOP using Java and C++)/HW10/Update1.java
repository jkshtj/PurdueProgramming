class DataObject {                                         
    int dataItem1;
    int dataItem2;

    DataObject() {
        dataItem1 = -1;
        dataItem2 = -1;
    }

    void set1(int d) {dataItem1 = d;}

    void set2(int d) {dataItem2 = d;}

    void test() {
        System.out.println(dataItem1 == dataItem2);
    }

    static void keepBusy( int howLong ) {
        long curr = System.currentTimeMillis();
        while ( System.currentTimeMillis() < curr + howLong );
    }
}

class RepeatedUpdates extends Thread  {
    DataObject dobj;
    int threadId;

    RepeatedUpdates( DataObject d ) {
        dobj = d;
        start();
    }
    public void run( ) {
        int i = 0;
        threadId = (int) Thread.currentThread().getId();
        
        while ( i < 20000 ) {                                  
            dobj.set1(threadId);                               
            dobj.set2(threadId);  //This statement has been swapped with the one below it
            dobj.keepBusy(10);
            if ( i % 1000 == 0 ) dobj.test();                
            try { sleep( (int) (Math.random() * 2 ) ); }    
            catch( InterruptedException e ) {}
            i++;
        }
    }
}

public class Update1 {  
    public static void main( String[] args ) {           
        DataObject d = new DataObject();  
        new RepeatedUpdates( d );  
        new RepeatedUpdates( d ); 
        new RepeatedUpdates( d );
        new RepeatedUpdates( d );
    }
}    

//Explanation for the given code behavior
/*Ans- The original behavior of the code is happening because of the dobj.keepBusy() function. When this function keeps
 *one thread busy, the other thread might come and check its dataitem1 value with the value of dataitem2, which might have
 * been set previously by one of the other four threads in the program.   */
