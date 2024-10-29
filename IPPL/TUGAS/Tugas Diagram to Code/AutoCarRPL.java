public class AutoCarRPL implements Transportasi {
  protected String bahanBakar;
  private int kecepatan;
  private Setir setir;
  private Roda[] roda;
  private Mesin mesin;

  public AutoCarRPL(String bahanBakar, int kecepatan) {
    this.bahanBakar = bahanBakar;
    this.kecepatan = kecepatan;
    this.setir = new Setir();
    this.roda = new Roda[4];
    for (int i = 0; i < 4; i++) {
        roda[i] = new Roda();
    }
    this.mesin = new Mesin();
  }

  @Override
  public void start() {
      System.out.println("Mobil dinyalakan.");
  }

  @Override
  public void drive() {
      System.out.println("Mobil sedang berjalan.");
  }

  public String getBahanBakar() {
      return bahanBakar;
  }

  public void setBahanBakar(String bahanBakar) {
      this.bahanBakar = bahanBakar;
  }

  public int getKecepatan() {
      return kecepatan;
  }

  public void setKecepatan(int kecepatan) {
      this.kecepatan = kecepatan;
  }
}
