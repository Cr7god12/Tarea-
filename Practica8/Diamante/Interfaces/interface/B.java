
package Diamante;

public interface B extends A {
    @Override
    default void saludar() {
        System.out.println("HOLA B");
    }
}