class EcuacionCuadratica {

    private double a;
    private double b;
    private double c;

    public EcuacionCuadratica(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public double getDiscriminante() {
        double dis=b * b - 4 * a * c;
        return dis ;
    }

    public double getRaiz1() {
        double discriminante = getDiscriminante();
        double raiz1=(-b + Math.sqrt(discriminante)) / (2 * a);
        return raiz1;
    }

    public double getRaiz2() {
        double discriminante = getDiscriminante();
        double raiz2=(-b - Math.sqrt(discriminante)) / (2 * a);
        return raiz2;
    }

    public void mostrarSolucion() {
        double discriminante = getDiscriminante();
        if (discriminante > 0) {
            System.out.println("La ecuación tiene dos raíces: " + getRaiz1() + " y " + getRaiz2());
        } else if (discriminante == 0) {
            System.out.println("La ecuación tiene una raíz: " + getRaiz1());
        } else {
            System.out.println("La ecuación no tiene raíces reales.");
        }
    }
}

