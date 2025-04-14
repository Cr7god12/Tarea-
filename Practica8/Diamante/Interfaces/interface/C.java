
package Diamante;

public interface C extends A {
    @Override
    default void saludar() {
        System.out.println("HOLA C");
    }
}
