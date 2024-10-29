public class Fuel extends AutoCarRPL {
  public Fuel(String bahanBakar, int kecepatan) {
      super(bahanBakar, kecepatan);
  }

  @Override
  public void start() {
      System.out.println("Mobil berbahan bakar " + bahanBakar + " dinyalakan.");
  }

  @Override
  public void drive() {
      System.out.println("Mobil berbahan bakar " + bahanBakar + " sedang berjalan.");
  }
}
