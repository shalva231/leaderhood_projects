package projects.julAndAug.java;
import javax.swing.*;

public class Main extends JFrame {
    public Main() {
        // Set up the frame
        setTitle("Word Counter");
        setSize(500, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(null);
        setResizable(false);
        setLocationRelativeTo(null); // Center the frame on the screen

        // Create the text area with placeholder
        JTextArea essay = new JTextArea("Write your essay here...");
        essay.setBounds(10, 10, 480, 200);
        essay.setLineWrap(true);
        essay.setWrapStyleWord(true);
        add(essay);

        // Create the calculate button
        JButton calculateButton = new JButton("Calculate");
        calculateButton.setBounds(200, 220, 100, 30);
        add(calculateButton);

        // Create the text field for results or additional input
        JTextField resultField = new JTextField();
        resultField.setBounds(10, 260, 480, 30);
        add(resultField);

        // Add action listener for the button (optional)
        calculateButton.addActionListener(e -> {
            // Example action: Count the words in the essay
            String text = essay.getText().trim();
            int wordCount = text.isEmpty() ? 0 : text.split("\\s+").length;
            resultField.setText("Word Count: " + wordCount);
        });
    }

    public static void main(String[] args) {
        // Create and display the frame
        Main frame = new Main();
        frame.setVisible(true);
    }
}

