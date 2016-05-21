/**
 * Created by Ozkh on 30/11/2015.
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;

public class MainGUI implements Runnable {

    private JFrame frame;
    private Container contentContainer;
    private JPanel mainPanel, uploadAndListPanel, downloadPanel, listTextPanel;
    private JButton downloadButton, uploadButton, listAllButton;
    private TextField downloadTextField;
    private TextArea listTextArea;

    private ClientController clientController;
    private JFileChooser uploadFileChooser;

    // Allows the use of the MVC pattern
    public MainGUI(ClientController cc) {
        clientController = cc;
   }

    // Creates the Main frame
    private void createFrames() {
        final String TITLEFRAME = "Welcome to Wonderland...";

        frame = new JFrame(TITLEFRAME);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(1000, 1000);
        frame.setMaximumSize(new Dimension(1000, 1000));
    }

    // 'Creates' (modifies) the Main frame's container
    private void createContainers() {
        //
        contentContainer = frame.getContentPane();
        contentContainer.setLayout(new BoxLayout(contentContainer, BoxLayout.PAGE_AXIS));
    }

    // Creates two panels: main, and the buttons panel
    private void createPanels() {

        // Panel for storing all login components
        mainPanel = new JPanel();
        mainPanel.setLayout(new BoxLayout(mainPanel, BoxLayout.PAGE_AXIS));
        mainPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        mainPanel.setMaximumSize(frame.getMaximumSize());
        mainPanel.setMinimumSize(mainPanel.getMaximumSize());

        // Panel for the upload and list all buttons
        uploadAndListPanel = new JPanel();
        uploadAndListPanel.setLayout(new BoxLayout(uploadAndListPanel, BoxLayout.LINE_AXIS));

        // Panel for the download button
        downloadPanel = new JPanel();
        downloadPanel.setLayout(new BoxLayout(downloadPanel, BoxLayout.LINE_AXIS));

        // Panel for where the listed image file names from the server are appearing
        listTextPanel = new JPanel();
        listTextPanel.setLayout(new BoxLayout(listTextPanel, BoxLayout.LINE_AXIS));
    }

    // Creates the download, upload and list all buttons
    private void createButtons() {
        final String DOWNLOADBUTTON = "Download";
        final String UPLOADBUTTON = "Upload";
        final String LISTALLBUTTON = "List All";

        downloadButton = new JButton(DOWNLOADBUTTON);
        uploadButton = new JButton(UPLOADBUTTON);
        listAllButton = new JButton(LISTALLBUTTON);
    }

    // Creates the text field for the download panel
    private void createTextFields() {
        downloadTextField = new TextField("ReplaceMe.jpg");
        downloadTextField.setMaximumSize(new Dimension(400, 25));
    }

    // Creates the text area for the listText panel
    private void createTextArea() {
        listTextArea = new TextArea("And now I am become death, the destroyer of worlds.");
        listTextArea.setEditable(false);
    }

    // Sets the visibility of the GUI
    public void setVisible(boolean state) {
        frame.setVisible(state);
        frame.pack();
    }

    // Adds the button listeners
    private void addListeners() {
        uploadButton.addActionListener(new UploadButtonListener());
        downloadButton.addActionListener(new DownloadButtonListener());
        listAllButton.addActionListener(new ListAllButtonListener());
    }

    // Event handler for the upload button
    private class UploadButtonListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            uploadFileChooser.showOpenDialog(uploadButton);
            File imageFile = uploadFileChooser.getSelectedFile();
            new UploadWorker(imageFile).execute();
        }
    }

    // Event handler for the download button
    private class DownloadButtonListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            String fileName = downloadTextField.getText();
            File imageFile = new File(fileName);
            new DownloadWorker(imageFile).execute();
        }
    }

    // Event handler for the listing server files button
    private class ListAllButtonListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            new ListAllWorker().execute();
       }
    }

    // Constructs all GUI components and dependencies in a thread safe environment
    public void run() {
        uploadFileChooser = new JFileChooser();

        this.createFrames();
        this.createContainers();
        this.createPanels();
        this.createButtons();
        this.createTextFields();
        this.createTextArea();

        uploadAndListPanel.add(uploadButton);
        uploadAndListPanel.add(Box.createRigidArea(new Dimension(15, 0)));
        uploadAndListPanel.add(listAllButton);

        downloadPanel.add(downloadButton);
        downloadPanel.add(Box.createRigidArea(new Dimension(15, 0)));
        downloadPanel.add(downloadTextField);

        listTextPanel.add(listTextArea);

        mainPanel.add(uploadAndListPanel);
        mainPanel.add(Box.createRigidArea(new Dimension(0, 10)));
        mainPanel.add(downloadPanel);
        mainPanel.add(Box.createRigidArea(new Dimension(0, 10)));
        mainPanel.add(listTextPanel);

        contentContainer.add(mainPanel);

        frame.pack();

        this.addListeners();
    }

    // To allow a responsive GUI even if the download is not complete
    private class DownloadWorker extends SwingWorker<Void, Void> {
        private File imageFile;

        // Specifies the file to be downloaded
        public DownloadWorker(File file) {
            imageFile = file;
        }

        // Attempts to download from the server
        protected Void doInBackground() {
            clientController.getClient().getImageProtocol().download(imageFile);
            return null;    // A tragic requirement
        }
    }

    // To allow a responsive GUI even if the download is not complete
    private class UploadWorker extends SwingWorker<Void, Void> {
        private File imageFile;

        // Specifies the file to be uploaded
        public UploadWorker(File file) {
            imageFile = file;
        }

        // Attempts to upload to the server
        protected Void doInBackground() {
            clientController.getClient().getImageProtocol().upload(imageFile);
            return null;    // A tragic requirement
        }
    }

    // To allow a responsive GUI even if the download is not complete
    private class ListAllWorker extends SwingWorker<Void, Void> {

        // Attempts to retrieve the list of all image file names from the server
        protected Void doInBackground() {
            String[] serverImageFiles;
            String stringOfImageFiles = "";

            serverImageFiles = clientController.getClient().getImageProtocol().listAllImages();

            // Constructs a single string to support the .setText(str) method
            for (String imageFile : serverImageFiles) {
                stringOfImageFiles += imageFile;
                stringOfImageFiles += System.lineSeparator();
            }
            listTextArea.setText(stringOfImageFiles);
            return null;    // A tragic requirement
        }
    }

    // Allows independent run of the MainGUI
    public static void main(String args[]) {
        ClientController cc;
        MainGUI mainGUI;

        try {
            cc = new ClientController();
            SwingUtilities.invokeAndWait((mainGUI = new MainGUI(cc)));
            mainGUI.setVisible(true);
            cc.createClient("127.0.0.1", 5000);
       } catch (InterruptedException e) {
            System.out.println("ERROR: GUI creation thread was interrupted.");
        } catch (InvocationTargetException e) {
            System.out.println("ERROR: Could not create the GUI.");
        } catch (IOException e) {
        System.out.println("Could not connect to '127.0.0.1:5000'");
        }
    }
}
