class FigurasGeometricas  {
    // Círculo
    public double area(double radio) {
        return Math.PI * radio * radio;
    }
    // Rectángulo
    public double area(double base, double altura) {
        return base * altura;
    }
    // Triángulo rectángulo
    public double area(int base, int altura) {
        return 0.5 * base * altura;
    }
    // Trapecio
    public double area(double baseMayor, double baseMenor, double altura1) {
        return ((baseMayor + baseMenor) * altura1) / 2;
    }
    // Pentágono regular
    public double area(int  lado, double  apotema) {
        return (5 * lado * apotema) / 2;
    }

    public static void main(String[] args) {
        FigurasGeometricas fig = new FigurasGeometricas();
        System.out.println("Área del círculo: " + fig.area(5));
        System.out.println("Área del rectángulo: " + fig.area(4, 6));
        System.out.println("Área del triángulo rectángulo: " + fig.area(3, 4));
        System.out.println("Área del trapecio: " + fig.area(6, 4, 5));
        System.out.println("Área del pentágono: " + fig.area(4, 5));
    }
}
