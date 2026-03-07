import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.awt.Color;
import java.awt.GridLayout;

import javax.swing.JButton;
import javax.swing.JFrame;

public class App {

    private static int[] getBounds() throws IOException {
        Scanner scanner = new Scanner(new File("bounds.txt"));
        String text = scanner.nextLine();
        scanner.close();

        int x, y, size;
        String[] pair = text.split(" ");
        x = Integer.parseInt(pair[0]);
        y = Integer.parseInt(pair[1]);
        size = Integer.parseInt(pair[2]);
        return new int[] {x, y, size};
    }

    public static void main(String[] args) throws Exception {
        int[] bounds = getBounds();
        int size = bounds[2];

        JFrame frame = new JFrame("Tracker");
        frame.setSize(600, 600);
        frame.setLayout(new GridLayout(bounds[0], bounds[1]));
        
        for (int i = 1; i < size + 1; i++) {
            JButton button = new JButton(String.valueOf(i));
            button.setBackground(Color.red);
            button.addActionListener(e -> {
                button.setBackground((button.getBackground() == Color.red) ? Color.green : Color.red);
            });
            frame.add(button);
        }

        frame.setVisible(true);
    }
}
