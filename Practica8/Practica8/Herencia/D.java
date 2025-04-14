
package Multiple;


public class D extends A {
    B b;

    public D(int x, int y, int z) {
        super(x, z);
        this.b = new B(y, z) {}; 
    }

    public void incrementaXYZ() {
        x++;
        b.y++;
        z++;
        b.z = z; 
    }

}
