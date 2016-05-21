/**
 * Created by Ozkh on 02/12/2015.
 */

import java.io.*;
import java.net.Socket;
import java.net.SocketException;
import java.text.SimpleDateFormat;
import java.util.Date;

// A network protocol to upload, download and list files
public class ImageProtocol {

    private Socket socket = null;
    private DataInputStream inputStream = null;
    private DataOutputStream outputStream = null;


    // Creates variables for input and output of the socket
    public ImageProtocol(Socket networkSocket) throws IOException {
        socket = networkSocket;
        inputStream = new DataInputStream(socket.getInputStream());
        outputStream = new DataOutputStream(socket.getOutputStream());
    }

    /************************************
     * CLIENT FEATURES
     ************************************/

    // Sends a request to either download, upload or list all files
    public void sendRequest(String request, String fileName) {
        try {
            outputStream.writeChars(encodeRequest(request, fileName));
            System.out.println("MESSAGE: Request " + request + " sent.");
        } catch (IOException e) {
            System.out.println("ERROR: Could not send a " + request + " request out.");
        }
    }

    // Attempts to download a specified fileName from a server
    public void download(File imageFile) {
        System.out.println("MESSAGE: Attempting to download " + imageFile.getName());
        this.sendRequest("DOWNLOAD", imageFile.getName());
        this.receiveFile(imageFile, "clientImages");
        System.out.println();
   }

    // Uploads a file by the name of "fileName" to the server's image directory
    public void upload(File imageFile) {
        System.out.println("MESSAGE: Attempting to upload " + imageFile.getName());
        this.sendRequest("UPLOAD", imageFile.getName());
        this.sendFile(imageFile);
        System.out.println();
    }

    // Lists all the files in the server's image directory
    public String[] listAllImages() {
        System.out.println("MESSAGE: Attempting to list all images from server");
        this.sendRequest("LIST", null);
        System.out.println();
        return this.receiveListOfAllImages();
    }

    /************************************
     * SERVER FEATURES
     ************************************/

    // Listens for incoming image requests
    public void listenForImageRequests() {
        (new Thread(new RequestHandler())).start();
    }

    // Handles the different type of requests sent by ImageProtocol
    private class RequestHandler implements Runnable {
        public void run() {
            String request, fileName, encodedData = "";
            String[] decodedData;

            while (true) {
                try {
                    // Waits for a valid request from the client
                    while (!encodedData.endsWith("?")) {
                        encodedData += inputStream.readChar();
                    }

                    // Decodes the received valid request
                    decodedData = ImageProtocol.this.decodeRequest(encodedData);
                    request = decodedData[0];
                    fileName = decodedData[1];
                    System.out.println("MESSAGE: received a request to " + request);
                    ImageProtocol.this.logRequests(request);

                    if (request.equals("DOWNLOAD")) {
                        // Need to generate absolute path since when a download request is received,
                        // only the image name and not path is specified
                        final String relativeDirectory = "serverImages";
                        final String absolutePath =  System.getProperty("user.dir") + File.separatorChar +
                                relativeDirectory + File.separatorChar + fileName;

                        ImageProtocol.this.sendFile(new File(absolutePath));
                    }
                    if (request.equals("UPLOAD")) {
                        ImageProtocol.this.receiveFile(new File(fileName), "serverImages");
                    }
                    if (request.equals("LIST")) {
                        ImageProtocol.this.sendListOfAllFiles("serverImages");
                    }

                } catch(SocketException e) {
                    // Extracts ip address
                    String socketToString = socket.getRemoteSocketAddress().toString();
                    String networkAddress = socketToString.substring(1, socketToString.length());
                    String ip = networkAddress.split(":")[0];
                    try {
                        System.out.println("ERROR: Client " + ip + " has left the building");
                        ImageProtocol.this.socket.close();
                    } catch (IOException err) {
                        System.out.println("ERROR: Could not close the network socket");
                    }
                    finally { break; }

                } catch (IOException e) {
                    System.out.println("ERROR: Unable to read incoming requests.");
                } finally {
                    encodedData = "";   // Allows for inputting new requests
                    System.out.println();
                }
            }
        }
    }

    /*************************************
     * HELPER FEATURES
     * ************************************/

    // Transfers a file by first sending the size of the file then it's contents
    private void sendFile(File imageFile) {
        try {
            FileInputStream imageFileInputStream = new FileInputStream(imageFile);
            long fileSize = imageFile.length();

            // Sends the file size
            outputStream.writeLong(fileSize);
            System.out.println("MESSAGE: File size sent of " + fileSize);

            // Sends the contents of the image
            this.copyStream(imageFileInputStream, outputStream, fileSize);

            System.out.println("MESSAGE: File has been sent successfully");
        }
        catch(IOException e) {
            if(imageFile.exists()) {
                System.out.println("ERROR: Could not find an image to send in: " + imageFile.getPath());
            }
            else {
                System.out.println("ERROR: Could not send the image, " + imageFile.getName());
                try {
                    outputStream.writeLong(-1);
                } catch (IOException err) {
                    System.out.println("ERROR: Unable to notify requester that the request must be rejected");
                }
            }
        }
    }

    // Downloads a file from the network socket
    private void receiveFile(File imageFile, String relativeDirectory) {
        long fileSize = 0;
        final String absolutePath =  System.getProperty("user.dir") + File.separatorChar +  relativeDirectory +
                File.separatorChar + imageFile.getName();

        try {
            // Output file
            File newFile = new File(absolutePath);
            FileOutputStream fileOutputStream = new FileOutputStream(newFile);

            // Waits to receive the file size then begins downloading the file data
            while (true) {
                if((fileSize = inputStream.readLong()) == -1) {
                    System.out.println("ERROR: The request was declined");
                    break;
                }
                else if (fileSize  >= 0) {
                    System.out.println("MESSAGE: A file size of " + fileSize + " received.");
                    this.copyStream(inputStream, fileOutputStream, fileSize);
                    System.out.println("MESSAGE: Download has been successfully completed");
                    System.out.println("MESSAGE: Name of the file generated is '" + imageFile.getName() + "'");
                    break;
                }
            }
        } catch (IOException e) {
            if (!imageFile.exists()) {
                System.out.println("ERROR: Could not generate an image in the following path: "
                        + absolutePath);
            } else {
                System.out.println("ERROR: Could not download the image, " + imageFile.getName() +
                        ", from the server.");
            }
        }
    }

    // Sends the list of image names on the server
    private void sendListOfAllFiles(String relativeDirectory) {
        File[] files = this.listAllFiles(relativeDirectory);
        char separatingSymbol = '!';
        char endSymbol = '?';

        try {
            // Encodes the name of all the images so it is easier
            // to deal with when receiving
            for (File imageFile : files) {
                outputStream.writeChars(imageFile.getName());
                outputStream.writeChar(separatingSymbol);
            }
            outputStream.writeChar(endSymbol);
            System.out.println("MESSAGE: Sent a list of all files");
        } catch (IOException e) {
            System.out.println("ERROR: Could not send the list of images");
        }
    }

    // Receives the list of image names on the server
    private String[] receiveListOfAllImages() {
        String[] listOfImages = null;
        String stringOfImages = "";
        String terminatingSymbolRemoved;
        String separatingSymbol = "!";

        try {
            // Waits and reads incoming data
            while(!stringOfImages.endsWith("?")) {
                stringOfImages += inputStream.readChar();
            }

            // Decodes the string that contains the name of all the images
            terminatingSymbolRemoved = stringOfImages.substring(0, stringOfImages.length() - 1);
            listOfImages = terminatingSymbolRemoved.split(separatingSymbol);

        } catch (IOException e) {
            System.out.println("ERROR: Unable to receive the list of images");
        }
        return listOfImages;
    }

    // Encodes a request protocol data as a single string with a dash separator
    private String encodeRequest(String request, String fileName) {
        String encodedRequest;

        encodedRequest = request + "-" + fileName + "?";    // Terminating symbol "?" helps validate requests
        return encodedRequest;
    }

    // Decodes a request protocol data
    private String[] decodeRequest(String encodedRequest) {
        String terminatingSymbolRemoved;
        String[] decodedRequest;

        terminatingSymbolRemoved = encodedRequest.substring(0, encodedRequest.length() - 1);
        decodedRequest = terminatingSymbolRemoved.split("-");

        return decodedRequest;
    }

    // Essentially connects an input stream to an output stream for data transfer
    private void copyStream(InputStream input, OutputStream output, long dataAmount) throws IOException
    {
        byte[] buffer = new byte[1024];
        int bytesRead = 0;
        int totalRead = 0;
        while(totalRead != dataAmount) {

            if((bytesRead = input.read(buffer)) > 0) {
                totalRead += bytesRead;
                output.write(buffer, 0, bytesRead);
                System.out.println("Data Transfer Progress: " + totalRead + " / " + dataAmount);
            }
        }
        output.flush();
    }

    // Returns all the image files on the server
    private File[] listAllFiles(String relativeDirectory) {
        final String absolutePath =  System.getProperty("user.dir") + File.separatorChar +  relativeDirectory +
                File.separatorChar;

        File[] files = new File(absolutePath).listFiles();

        return files;
    }

    // Logs all requests to a text file
    private void logRequests(String request) {
        final String relativeDirectory = "logs";
        String fileName;
        String absolutePath;

        Date date = new Date();
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy.MM.dd-hh:mm:ss");

        try {
            // Extracts the ip address (and port number) as string form
            String socketToString = socket.getRemoteSocketAddress().toString();
            String networkAddress = socketToString.substring(1, socketToString.length());
            String ip = networkAddress.split(":")[0];

            // Creates the log file and it's writer
            fileName = ip + ".txt";
            absolutePath =  System.getProperty("user.dir") + File.separatorChar +  relativeDirectory +
                    File.separatorChar + fileName;
            File logFile = new File(absolutePath);
            PrintWriter writer = new PrintWriter(new FileOutputStream(logFile, true));

            // Writes the log entry
            String logText = dateFormat.format(date) + "-" + networkAddress + "-" + request + System.lineSeparator();
            writer.write(logText);
            writer.flush();
        } catch (IOException e) {
           System.out.println("ERROR: Request could not be logged");
        }
    }
}
