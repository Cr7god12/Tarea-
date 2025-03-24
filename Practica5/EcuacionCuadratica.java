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

    
}

