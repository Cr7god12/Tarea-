
package Multiple;

public class Main {
    public static void  main(String[] args) {
        D d = new D(1, 2, 3);
        System.out.println("x = " + d.x + ", y = " + d.b.y + ", z = " + d.z);
        d.incrementaXZ();    
        d.incrementaZ();     
        d.b.incrementaYZ();   
        d.b.incrementaZ();     
        d.incrementaXYZ();     
 
        
        System.out.println("x = " + d.x + ", y = " + d.b.y + ", z = " + d.z);
    }
}

