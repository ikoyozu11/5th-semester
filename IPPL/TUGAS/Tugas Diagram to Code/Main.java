public class Main {
  public static void main(String[] args) {
      AutoCarRPL mobil = new AutoCarRPL("Bensin", 100);
      mobil.start();
      mobil.drive();

      Mio mio = new Mio("Bensin", 60);
      mio.start();
      mio.drive();

      Fuel fuelCar = new Fuel("Solar", 80);
      fuelCar.start();
      fuelCar.drive();
  }
}
