/**
 * Created by Ozkh on 29/11/2015.
 */

import java.net.Socket;

import java.io.IOException;


// Client handler that handles client requests to access images (e.g. download, upload, etc)
public class ClientHandler implements Runnable {

    private ImageProtocol imageProtocol;

    // Creates the network protocol object for image transferring
    public ClientHandler(Socket client) throws IOException {
            imageProtocol = new ImageProtocol(client);
            imageProtocol.listenForImageRequests();
    }

    public ImageProtocol getImageProtocol(){ return imageProtocol; }

    public void run() {}
}