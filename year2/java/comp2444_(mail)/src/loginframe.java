/**
 * Created by Ozkh on 10/11/2015.
 */

import javax.mail.MessagingException;
import javax.swing.*;
import javax.swing.border.Border;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

// The login menu (a Viewer of the MVC pattern)
public class LoginFrame extends JFrame {
    private final static String TITLEFRAME = "Login";
    private final static String LOGINBUTTON = "Enter";

    private JFrame frame;
    private JPanel userPanel, passwordPanel, loginPane;
    private JButton loginButton;
    private JTextField userField;
    private JPasswordField passwordField;
    private JLabel titleLabel, userLabel, passwordLabel;
    private Container contentPane;
    private Border emptyBorder = BorderFactory.createEmptyBorder(10, 10, 10, 10);
    MailController mailController;

    public LoginFrame(MailController mc) {
        // Allows the use of the MVC pattern
        mailController = mc;

        // Create the frame and adjust settings
        frame = new JFrame(TITLEFRAME);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(700, 700);
        frame.setMaximumSize(new Dimension(700, 700));
        frame.setVisible(true);

        // Main pane
        contentPane = frame.getContentPane();
        contentPane.setLayout(new BoxLayout(contentPane, BoxLayout.PAGE_AXIS));

        // Login pane that will be contained in the contentPane
        loginPane = new JPanel();
        loginPane.setLayout((new BoxLayout(loginPane, BoxLayout.PAGE_AXIS)));
        loginPane.setBorder(emptyBorder);

        // The username panel
        userPanel = new JPanel();
        userPanel.setLayout(new BoxLayout(userPanel, BoxLayout.LINE_AXIS));
        userPanel.setMaximumSize(new Dimension((int) frame.getMaximumSize().getHeight(), 20));    // Uses 1 row only
        userPanel.setMinimumSize(userPanel.getMaximumSize());    // Uses 1 row only

        // The password panel
        passwordPanel = new JPanel();
        passwordPanel.setLayout(new BoxLayout(passwordPanel, BoxLayout.LINE_AXIS));
        passwordPanel.setMaximumSize(new Dimension((int) frame.getMaximumSize().getHeight(), 20));  // Uses 1 row only
        passwordPanel.setMinimumSize(passwordPanel.getMaximumSize());    // Uses 1 row only

        userField = new JTextField(30);
        passwordField = new JPasswordField(30);

        titleLabel = new JLabel("Othman Empire Mail: Using Gmail");
        titleLabel.setAlignmentX(CENTER_ALIGNMENT);
        userLabel = new JLabel("Username:");
        passwordLabel = new JLabel("Password:");

        loginButton = new JButton(LOGINBUTTON);
        loginButton.setAlignmentX(CENTER_ALIGNMENT);

        userPanel.add(userLabel);
        userPanel.add(Box.createRigidArea(new Dimension(10, 0)));
        userPanel.add(userField);

        passwordPanel.add(passwordLabel);
        passwordPanel.add(Box.createRigidArea(new Dimension(11, 0)));
        passwordPanel.add(passwordField);

        loginPane.add(Box.createRigidArea(new Dimension(0, 10)));
        loginPane.add(titleLabel);
        loginPane.add(Box.createRigidArea(new Dimension(0, 10)));
        loginPane.add(userPanel);
        loginPane.add(Box.createRigidArea(new Dimension(0, 10)));
        loginPane.add(passwordPanel);
        loginPane.add(Box.createRigidArea(new Dimension(0, 10)));
        loginPane.add(loginButton);
        loginPane.add(Box.createRigidArea(new Dimension(0, 10)));

        contentPane.add(loginPane);

        frame.pack();

        // Adding listeners
        loginButton.addActionListener(new LoginButtonListener());
    }

    public JFrame getFrame() { return frame;}

    // Authenticates user credentials then moves them onto the next window (MainFrame)
    private class LoginButtonListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            try {
                mailController.getMailModel().openConnection(userField.getText(),
                        passwordField.getPassword());

                mailController.displayMainFrame();
                frame.setVisible(false);
            } catch (MessagingException e) {
                System.out.println("Invalid login credentials! ERROR: " + e);
            }
        }
    }
}
