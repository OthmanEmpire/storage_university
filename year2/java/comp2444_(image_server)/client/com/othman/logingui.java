/**
 * Created by Ozkh on 30/11/2015.
 */


import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;

// The GUI for the Client class
public class LoginGUI implements Runnable {

    // GUI component fields used across all class methods
    private JFrame frame;
    private JPanel loginPanel, ipPanel, portPanel, buttonPanel;
    private Container contentContainer;
    private JButton connectButton;
    private JTextField ipField, portField;
    private JLabel ipLabel, portLabel;

    private ClientController clientController;

    // Allows the use of the MVC pattern
    public LoginGUI(ClientController cc) {
        clientController = cc;
   }

    // Creates the Main frame
    private void createFrames() {
        final String TITLEFRAME = "Wonderland awaits you...";

        frame = new JFrame(TITLEFRAME);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(700, 700);
        frame.setMaximumSize(new Dimension(700, 700));
    }

    // 'Creates' (modifies) the Main frame's container
    private void createContainers() {
        contentContainer = frame.getContentPane();
        contentContainer.setLayout(new BoxLayout(contentContainer, BoxLayout.PAGE_AXIS));
    }

    // Creates four panels: login , IP address, port number, and button panel
    private void createPanels() {

        // Panel for storing all login components
        loginPanel = new JPanel();
        loginPanel.setLayout(new BoxLayout(loginPanel, BoxLayout.PAGE_AXIS));
        loginPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        loginPanel.setMaximumSize(frame.getMaximumSize());
        loginPanel.setMinimumSize(loginPanel.getMaximumSize());

        // Panel for entering server's IP address
        ipPanel = new JPanel();
        ipPanel.setLayout(new BoxLayout(ipPanel, BoxLayout.LINE_AXIS));
        ipPanel.setMaximumSize(new Dimension((int) frame.getMaximumSize().getHeight(), 20));
        ipPanel.setMinimumSize(ipPanel.getMaximumSize());

        // Panel for entering server's port
        portPanel = new JPanel();
        portPanel.setLayout(new BoxLayout(portPanel, BoxLayout.LINE_AXIS));
        portPanel.setMaximumSize(new Dimension((int) frame.getMaximumSize().getHeight(), 20));
        portPanel.setMinimumSize(portPanel.getMaximumSize());

        // Panel for the connect button
        buttonPanel = new JPanel();
        buttonPanel.setLayout(new BoxLayout(buttonPanel, BoxLayout.LINE_AXIS));
    }

    // Creates the connect button
    private void createButtons() {
        final String CONNECTBUTTON = "Connect";

        connectButton = new JButton(CONNECTBUTTON);
    }

    // Creates two fields for the IP address and port number
    private void createFields() {
        ipField = new JTextField(30);
        portField = new JTextField(30);
    }

    // Creates two labels for the IP address and port number
    private void createLabels() {
        final String IPLABEL = "IP Address: ";
        final String PORTLABEL = "Port Number: ";

        ipLabel = new JLabel(IPLABEL);
        portLabel = new JLabel(PORTLABEL);
    }

    // Sets the visibility of the GUI
    public void setVisible(boolean state) {
        frame.setVisible(state);
    }

    // Adds the ButtonListener to the connectButton
    private void addListeners() {
        connectButton.addActionListener(new ButtonListener());
    }

    // Event handler for the login button
    private class ButtonListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            String ip, port;

            ip = ipField.getText();
            port = portField.getText();
            new LoginWorker(ip, port).execute();
        }
    }

    // Constructs all GUI components in a thread safe environment
    public void run() {
        this.createFrames();
        this.createContainers();
        this.createPanels();
        this.createButtons();
        this.createFields();
        this.createLabels();

        ipPanel.add(ipLabel);
        ipPanel.add(Box.createRigidArea(new Dimension(15, 0)));
        ipPanel.add(ipField);

        portPanel.add(portLabel);
        portPanel.add(Box.createRigidArea(new Dimension(5, 0)));
        portPanel.add(portField);

        buttonPanel.add(connectButton);

        loginPanel.add(ipPanel);
        loginPanel.add(Box.createRigidArea(new Dimension(0, 10)));
        loginPanel.add(portPanel);
        loginPanel.add(Box.createRigidArea(new Dimension(0, 10)));
        loginPanel.add(buttonPanel);

        contentContainer.add(loginPanel);

        frame.pack();

        this.addListeners();
    }

    // Allows threading (SwingWorker) when connecting to server.
    // Strictly speaking, it isn't necessary but I wanted a responsive GUI
    // even when logging in for learning purposes.
    private class LoginWorker extends SwingWorker<Void, Void> {
        private String ip;
        private String port;

        // Passes in ip address and port number into the class
        public LoginWorker(String ipAddress, String portNumber) {
            ip = ipAddress;
            port = portNumber;
        }

        // Attempts to connect to the server
        protected Void doInBackground() {
            try {
                clientController.createClient(ip, Integer.parseInt(port));
                clientController.displayLoginFrame(false);
                clientController.displayMainFrame(true);
            } catch (IOException e) {
                JOptionPane.showMessageDialog(frame, "ERROR: Could not connect to: " + ip + ":" + port);
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(frame, "ERROR: Port number must be an integer.");
            } catch (IllegalArgumentException e) {
                JOptionPane.showMessageDialog(frame, "ERROR: Port out of range.");
            }
            return null;    // A tragic requirement
        }
    }

    // Allows independent run of the LoginGUI
    public static void main(String args[]) {
        ClientController cc = new ClientController();
        LoginGUI loginMenu;

        try {
            SwingUtilities.invokeAndWait((loginMenu = new LoginGUI(cc)));
            loginMenu.setVisible(true);
        } catch (InterruptedException e) {
            System.out.println("ERROR: GUI creation thread was interrupted.");
        } catch (InvocationTargetException e) {
            System.out.println("ERROR: Could not create the GUI.");
        }
    }
}

