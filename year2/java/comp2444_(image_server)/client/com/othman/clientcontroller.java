/**
 * Created by Ozkh on 30/11/2015.
 */

import javax.swing.*;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;

// Controller of the MVC pattern for the Client application
public class ClientController {

    private LoginGUI loginMenu;
    private MainGUI mainMenu;
    private Client client;

    // Creates a client for the given ip address and port
    public void createClient(String ip, int port) throws IOException {
        client = new Client(ip, port);
    }

    // Sets visibility of the main GUI
    public void displayMainFrame(boolean isVisible) {
        mainMenu.setVisible(isVisible);
    }

    // Sets visibility of the login GUI
    public void displayLoginFrame(boolean isVisible) {
        loginMenu.setVisible(isVisible);
    }

    // Invokes the creation of all the GUI components
    public void initialize() {
        try {
            SwingUtilities.invokeAndWait((loginMenu = new LoginGUI(this)));
            SwingUtilities.invokeAndWait(mainMenu = new MainGUI(this));
        } catch (InterruptedException e) {
            System.out.println("ERROR: GUI creation threads were interrupted.");
        } catch (InvocationTargetException e) {
            System.out.println("ERROR: Could not create the GUI.");
        }
        loginMenu.setVisible(true);
    }

    public Client getClient() {
        return client;
    }

    // Starting point of the client application
    public static void main(String args[]) {
        ClientController cc = new ClientController();
        cc.initialize();
    }
}
