/**
 * Created by Ozkh on 29/11/2015.
 * Acknowledgements to the VLE chat code
 */

import java.net.ServerSocket;
import java.net.Socket;

import java.io.IOException;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

// Basic image server (uploads & downloads images)
public class ImageServer {

    private ServerSocket serverSocket = null;
    private ExecutorService pool;
    private int poolSize = 10;

    // Binds the instantiated server to a port and creates a fixed pool of threads
    public ImageServer(int port) {
        try {
            serverSocket = new ServerSocket(port);
            pool = Executors.newFixedThreadPool(poolSize);
        }
        catch (IOException e) {
            System.out.println("ERROR: Port: " + port + " is already in use!");
        }
    }

    // Listens for client connections and adds them to the pool
    public void runServer() {
        while (true) {
            try {
                Socket clientSocket = serverSocket.accept();
                pool.execute(new ClientHandler(clientSocket));
            } catch (IOException e) {
                System.out.println("ERROR: Could not create a Client Handler for the client!");
                pool.shutdown();
            }
            System.out.println("MESSAGE: " + pool.toString().split("\\[|]")[1]);
          }
    }

    // Runs the server
    public static void main( String[] args ) {
        ImageServer server = new ImageServer(5000);
        server.runServer();
    }
}
