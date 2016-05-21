/**
 * created by ozkh on 10/11/2015.
 * acknowledgements to below:
 * http://www.mkyong.com/java/javamail-api-sending-email-via-gmail-smtp-example/
 * http://www.tutorialspoint.com/java/java_sending_email.htm
 * https://www.youtube.com/watch?v=glewfpkid74
 * and any other online source that i have missed out (hopefully not).
 */

import javax.mail.Message;
import javax.swing.*;
import javax.swing.border.Border;
import javax.swing.border.EtchedBorder;
import javax.swing.border.TitledBorder;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;

// The main menu (a Viewer of the MVC pattern)
public class MainFrame extends JFrame {
    private Color green = new Color(0,100,0);
    private final static String SENDPANEL = "Send Mail";
    private final static String RECEPANEL = "Receive Mail";
    private final static String TITLEFRAME = "Othman Empire Mail";
    private final static String SENDBUTTON = "Send Demonic Mail";
    private final static String NEXTBUTTON = "Next Demonic Mail";
    private final static String PREVBUTTON = "Previous Demonic Mail";
    private final static String FROMFIELD = "TheDiabolic@gmail.com";
    private final static String TOFIELD = "TheEvil@gmail.com";
    private final static String SUBJECTFIELD = "Lack of Confidence";
    private final static String BODYFIELD = "Dear Mr.Evil,\n\n" +
            "Am I a poor programmer if I can't figure out the bubble sort algorithm?\n\nRegards,\nTheDiabolic";

    private Border emptyBorder = BorderFactory.createEmptyBorder(10, 10, 10, 10);
    private Border greenBorder = BorderFactory.createLineBorder(green);
    private JFrame frame;
    private JTabbedPane tabbedPane;
    private JPanel card1, card2, sendButtonPanel, recvButtonPanel, messagePanel, subjectPanel, fromPanel, toPanel;
    private JButton sendMailButton, nextMailButton, prevMailButton;
    private JLabel subjectLabel, fromLabel, toLabel;
    private JTextField subjectField, fromField, toField;
    private JTextArea bodyText, recvText;
    private JScrollPane recvPanel, bodyPanel;
    private Container contentPane;

    private MailController mailController;
    private MailModel mailModel;    // To be accessed through mailController
    private int messageNum = 0;

    public MainFrame(MailController mc) {
        mailController = mc;
        mailModel = mailController.getMailModel();

        // Create the frame and adjust settings
        frame = new JFrame(TITLEFRAME);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(700, 700);

        // Main pane where tabs will be added
        contentPane = frame.getContentPane();

        // Tabbed pane where 'cards' will be added
        tabbedPane = new JTabbedPane();

        // Add components to the 'card' for the first tab
        card1 = new JPanel();
        card1.setLayout(new BoxLayout(card1, BoxLayout.PAGE_AXIS));

        // Add components to the 'card' for the second tab
        card2 = new JPanel();
        card2.setLayout(new BoxLayout(card2, BoxLayout.PAGE_AXIS));

        // Create the panel for the receiving buttons (previous and next buttons)
        recvButtonPanel = new JPanel();
        recvButtonPanel.setLayout((new BoxLayout(recvButtonPanel, BoxLayout.LINE_AXIS)));

        sendButtonPanel = new JPanel();
        sendButtonPanel.setLayout((new BoxLayout(sendButtonPanel, BoxLayout.LINE_AXIS)));

        // Create the panel for where the email is typed up
        messagePanel = new JPanel();
        messagePanel.setLayout((new BoxLayout(messagePanel, BoxLayout.PAGE_AXIS)));
        messagePanel.setBorder(emptyBorder);

        // Create the panel and text field where emails are typed up for card1
        bodyText = new JTextArea(BODYFIELD);
        bodyText.setBorder(BorderFactory.createCompoundBorder(greenBorder, emptyBorder));
        bodyPanel = new JScrollPane(bodyText, ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED,
                ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED);
        bodyPanel.setBorder(BorderFactory.createCompoundBorder(new EtchedBorder(), emptyBorder));

        // Create the panel and text field where received emails could be displayed for card2
        recvText = new JTextArea();
        recvText.setEditable(false);
        recvText.setBorder(BorderFactory.createCompoundBorder(greenBorder, emptyBorder));
        recvPanel = new JScrollPane(recvText, ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS,
                ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS);
        recvPanel.setBorder(new TitledBorder(
                BorderFactory.createCompoundBorder(new EtchedBorder(), emptyBorder), "Received Email: "));

        // Create the "subject" mail field panel
        subjectPanel = new JPanel();
        subjectPanel.setLayout(new BoxLayout(subjectPanel, BoxLayout.LINE_AXIS));
        subjectPanel.setMaximumSize(new Dimension((int) frame.getMaximumSize().getWidth(), 0));

        // Create the "sent from" mail field panel
        fromPanel = new JPanel();
        fromPanel.setLayout(new BoxLayout(fromPanel, BoxLayout.LINE_AXIS));
        fromPanel.setMaximumSize(new Dimension((int) frame.getMaximumSize().getWidth(), 0));

        // Create the "sent to" mail field panel
        toPanel = new JPanel();
        toPanel.setLayout(new BoxLayout(toPanel, BoxLayout.LINE_AXIS));
        toPanel.setMaximumSize(new Dimension((int) frame.getMaximumSize().getWidth(), 0));

        // Create the send and and receive (next and prev) mail buttons
        sendMailButton = new JButton(SENDBUTTON);
        nextMailButton = new JButton(NEXTBUTTON);
        nextMailButton.setMinimumSize(new Dimension(180, 25));
        nextMailButton.setMaximumSize(nextMailButton.getMinimumSize());
        prevMailButton = new JButton(PREVBUTTON);
        prevMailButton.setMinimumSize(new Dimension(180, 25));
        prevMailButton.setMaximumSize(prevMailButton.getMinimumSize());

        // Create labels corresponding to email detail fields
        subjectLabel = new JLabel("Subject");
        fromLabel = new JLabel("From");
        toLabel = new JLabel("To");

        // Create fields to enter email details for card1
        subjectField = new JTextField(SUBJECTFIELD);
        subjectField.setBorder(greenBorder);
        fromField = new JTextField(FROMFIELD);
        fromField.setBorder(greenBorder);
        fromField.setEditable(false);
        toField = new JTextField(TOFIELD);
        toField.setBorder(greenBorder);

        card1.add(Box.createRigidArea(new Dimension(10, 0)));
        card1.add(messagePanel);

        card2.add(Box.createRigidArea(new Dimension(0, 10)));
        card2.add(recvPanel);
        card2.add(Box.createRigidArea(new Dimension(0, 10)));
        card2.add(recvButtonPanel);
        card2.add(Box.createRigidArea(new Dimension(0, 10)));

        tabbedPane.addTab(SENDPANEL, card1);
        tabbedPane.addTab(RECEPANEL, card2);

        messagePanel.add(fromPanel);
        messagePanel.add(Box.createRigidArea(new Dimension(0, 10)));
        messagePanel.add(toPanel);
        messagePanel.add(Box.createRigidArea(new Dimension(0, 10)));
        messagePanel.add(subjectPanel);
        messagePanel.add(Box.createRigidArea(new Dimension(0, 10)));
        messagePanel.add(bodyPanel);
        messagePanel.add(Box.createRigidArea(new Dimension(0, 10)));
        messagePanel.add(sendButtonPanel);

        sendButtonPanel.add(sendMailButton);
        recvButtonPanel.add(prevMailButton);
        recvButtonPanel.add(Box.createRigidArea(new Dimension(30, 0)));
        recvButtonPanel.add(nextMailButton);

        subjectPanel.add(subjectLabel);
        subjectPanel.add(Box.createRigidArea(new Dimension(10, 0)));
        subjectPanel.add(subjectField);

        fromPanel.add(fromLabel);
        fromPanel.add(Box.createRigidArea(new Dimension(25, 0)));
        fromPanel.add(fromField);

        toPanel.add(toLabel);
        toPanel.add(Box.createRigidArea(new Dimension(40, 0)));
        toPanel.add(toField);

        contentPane.add(tabbedPane, BorderLayout.CENTER);

        frame.pack();

        // Adding event listeners
        sendMailButton.addActionListener(new SendButtonListener());
        RecvButtonListener recvHandler = new RecvButtonListener();
        nextMailButton.addActionListener(recvHandler);
        prevMailButton.addActionListener(recvHandler);
        addWindowListener(new ExitListener());
    }

    public JFrame getFrame() { return frame;}

    public void setUsername(String from) {
        fromField.setText(from);
    }

    // Sends an email whenever the button is pressed
    private class SendButtonListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            mailModel.sendMail(fromField.getText(), toField.getText(), subjectField.getText(), bodyText.getText());
        }
    }

    // Reads the next or previous email from inbox
    private class RecvButtonListener implements ActionListener {
        Message message = null;
        public void actionPerformed(ActionEvent event) {
            if(event.getSource() == nextMailButton) {
                messageNum += 1;
            }
            if(event.getSource() == prevMailButton) {
                messageNum -= 1;
            }
            mailModel.openInbox();
            message = mailModel.fetchInboxMail(messageNum);
            recvText.setText(mailModel.readMail(message));
        }
    }

    // Listener to ensure that all connections are closed
    // (courtesy from an online source that I no longer have access to)
    private class ExitListener implements WindowListener {
        public void windowClosing(WindowEvent arg0) {
            mailController.getMailModel().closeConnections();
            System.exit(0);
        }
        public void windowOpened(WindowEvent arg0) {}
        public void windowClosed(WindowEvent arg0) {}
        public void windowIconified(WindowEvent arg0) {}
        public void windowDeiconified(WindowEvent arg0) {}
        public void windowActivated(WindowEvent arg0) {}
        public void windowDeactivated(WindowEvent arg0) {}
    }
}