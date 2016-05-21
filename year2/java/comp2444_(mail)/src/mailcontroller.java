/**
 * Created by Ozkh on 10/11/2015.
 */

import javax.swing.*;

// Links the GUI and email logic together (the Controller of the MVC pattern)
public class MailController implements Runnable{
    private LoginFrame loginFrame;
    private MainFrame mainFrame;
    private MailModel mailModel;

    public MailModel getMailModel() { return mailModel; }

    // Displays the MainFrame window
    public void displayMainFrame() {
        mainFrame.setUsername(mailModel.getUsername());
        mainFrame.getFrame().setVisible(true);
    }

    public void run() {
        mailModel =  new MailModel();
        loginFrame = new LoginFrame(this);
        mainFrame = new MainFrame(this);
    }

    public static void main(String args[]){
        SwingUtilities.invokeLater(new MailController());
    }
}

