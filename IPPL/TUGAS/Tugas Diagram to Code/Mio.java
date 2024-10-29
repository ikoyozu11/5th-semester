public class Mio extends AutoCarRPL {
  public Mio(String bahanBakar, int kecepatan) {
      super(bahanBakar, kecepatan);
  }

  @Override
  public void start() {
      System.out.println("Mio dinyalakan.");
  }

  @Override
  public void drive() {
      System.out.println("Mio sedang berjalan.");
  }
}
