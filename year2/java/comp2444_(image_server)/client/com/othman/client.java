/**
 * Created by Ozkh on 29/11/2015.
 */

import java.net.Socket;
import java.io.IOException;

// Client that connects to the image server (through
// ImageProtocol, it can download, upload and list all images from the server)
public class Client {

    private Socket socket;
    private ImageProtocol imageProtocol;

    // Creates a socket and assigns the imageProtocol for network functionality
    public Client(String host, int port) throws IOException {
        socket = new Socket(host, port);
        imageProtocol = new ImageProtocol(socket);
    }

    public ImageProtocol getImageProtocol() { return imageProtocol; }

    // Allows for Client class testing
    public static void main( String[] args ) {
        try {
            Client client = new Client("127.0.0.1", 5000);
        } catch (IOException e) {
            System.out.println("COULD NOT CONNECT");
        }
    }
}
