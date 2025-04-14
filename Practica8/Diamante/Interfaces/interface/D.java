package Diamante;

public class D implements B, C {
    @Override
    public void saludar() {
        new AuxA().saludar();
        B.super.saludar();
        C.super.saludar();
        System.out.println("Hola D");
    }

    public static void main(String[] args) {
        D obj = new D();
        obj.saludar();
    }
}
