package cloud.salpy.sally;


import cloud.salpy.sally.Structure.Client;

public class Main {
    public static void main(String[] args) throws Exception {
        Integer port = (System.getenv("PORT").isEmpty()) ? Integer.parseInt(System.getenv("PORT")) : 8000;
        new Client(port).start();
    }
}
