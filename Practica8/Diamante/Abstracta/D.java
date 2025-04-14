package Abstracta;

public class D extends A {
    private B b;
    private C c;

    public D() {
        // Instancias anónimas para clases abstractas
        b = new B() {};
        c = new C() {};
    }

    public void saludar() {
        super.saludar(); // Llama a A
        b.saludar();     // Llama a B
        c.saludar();     // Llama a C
        System.out.println("Hola desde D");
    }
}
