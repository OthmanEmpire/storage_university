/**
 * created by ozkh on 10/11/2015.
 * acknowledgements to below:
 * http://www.mkyong.com/java/javamail-api-sending-email-via-gmail-smtp-example/
 * http://www.tutorialspoint.com/java/java_sending_email.htm
 * https://www.youtube.com/watch?v=glewfpkid74
 * and any other online source that i have missed out (hopefully not).
 */

import java.io.IOException;
import java.util.Properties;
import java.util.Date;
import javax.mail.*;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

// The core logic for handling emails using JavaMail API (the Model in the MVC pattern)
public class MailModel {
    private Session session;
    private Store store;
    private Folder inbox;
    private String server = "smtp.gmail.com", port = "587";
    PasswordAuthentication passwordAuthentication;

    public MailModel() {}

    public String getUsername() {
        return passwordAuthentication.getUserName();
    }

    //  Attempts to connect to gmail servers
    public void openConnection(String loginUsername, char[] loginPassword) throws MessagingException {
        passwordAuthentication = new PasswordAuthentication(loginUsername, new String(loginPassword));

        // Properties for various email protocols
        Properties props = new Properties();
        props.put("mail.smtp.host", server);
        props.put("mail.smtp.port", port);
        props.put("mail.smtp.starttls.enable", true);
        props.put("mail.smtp.auth", true);
        props.put("mail.transport.protocol", "smtp");
        props.put("mail.store.protocol", "imaps");

            // Creating a session & authenticating user credentials
            session = Session.getInstance(props,
                    new Authenticator() {
                        @Override
                        protected PasswordAuthentication getPasswordAuthentication() {
                            return passwordAuthentication;
                        }
                    });

            // Creating a store class that holds a hierarchy of folders
            store = session.getStore("imaps");
            store.connect(server, passwordAuthentication.getUserName(), passwordAuthentication.getPassword());
    }

    // Creates a message class, fills in the data to be sent, then sends the message to the server
    public void sendMail(String from, String to, String subject, String bodyText) {
        try {
            // Creates a MIME (Multipurpose Internet Mail Extension) message/email
            MimeMessage msg = new MimeMessage(session);

            //Filling the message with appropriate information
            msg.setFrom(new InternetAddress(from));
            msg.setRecipients(Message.RecipientType.TO, InternetAddress.parse(to));
            msg.setSubject(subject);
            msg.setText(bodyText);
            msg.setSentDate(new Date());

            // Actually transporting the message
            Transport.send(msg);
        } catch (MessagingException e) {
            System.out.println("Unable to send. ERROR: " + e);
        }
    }

    // Opens the inbox to be read
    public void openInbox() {
        try {
            inbox = store.getFolder("inbox");
            inbox.open(Folder.READ_ONLY);
        } catch (MessagingException e) {
            System.out.println("Unable to open Inbox. ERROR: " + e);
        }
    }

    // fetches email number Num from inbox
    public Message fetchInboxMail(int Num) {
        Message message = null;
        try {
            // Extracts email number Num
            message = inbox.getMessage(Num);
        } catch (MessagingException e) {
            System.out.println("Unable to read from Inbox. ERROR: " + e);
        }
        return message;
    }

    // Parses only a specific type of email to be read
    public static String readMail(Message message) {
        String output = "";
        try {
            Address[] from = message.getFrom();
            for (Address address : from) {
                output += "FROM: " + address.toString() + "\n";
            }
            Address[] to = message.getReplyTo();
            for (Address address : to) {
                output += "TO: " + address.toString() + "\n\n";
            }

            Multipart mp = (Multipart) message.getContent();
            BodyPart bp = mp.getBodyPart(0);

            output += "SUBJECT: " + message.getSubject() + "\n\n";
            output += bp.getContent();
            output += "SENT DATE: " + message.getSentDate();

        } catch (MessagingException e) {
            System.out.println("Unable to read from Email. ERROR: " + e);
        } catch (IOException e) {
            System.out.println("Unable to access email. ERROR: " + e);
        }
        return output;
    }

    // Closes connection to the email server
    public void closeConnections() {
        try {
            store.close();
        } catch (MessagingException e) {
            System.out.println("Unable to close connection. ERROR: " + e);
        }
    }
}
