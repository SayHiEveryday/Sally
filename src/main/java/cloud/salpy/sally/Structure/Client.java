package cloud.salpy.sally.Structure;

import cloud.salpy.sally.pri.Constant;
import com.jagrosh.interactions.InteractionsClient;
import com.jagrosh.interactions.requests.RestClient;

import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

public class Client {
    private InteractionsClient interactionsClient;
    private RestClient restClient;
    public Client(Integer port) {
        restClient = new RestClient(Constant.token);
        interactionsClient = new InteractionsClient.Builder()
                .setRestClient(restClient)
                .setAppId(Long.parseLong(Constant.appid))
                .setPublicKey(Constant.publickey)
                .setPort(port)
                .setPath("/")
                .build();
    }
    public void start() throws NoSuchAlgorithmException, InvalidKeyException {
        this.interactionsClient.start();
    }
    public RestClient getRestClient() {
        return this.restClient;
    }
}
