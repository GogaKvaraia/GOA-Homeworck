import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class SimpleGame extends JPanel implements KeyListener, ActionListener {
    private int playerX = 300, playerY = 300;
    private int playerVelocityY = 0;
    private boolean isJumping = false;
    private boolean isMovingLeft = false, isMovingRight = false;
    private Timer timer;

    public SimpleGame() {
        // Initialize the game window
        setPreferredSize(new Dimension(800, 600));
        setBackground(Color.CYAN);
        setFocusable(true);
        addKeyListener(this);

        // Set up a timer for the game loop
        timer = new Timer(10, this);
        timer.start();
    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        // Draw the player (a simple rectangle)
        g.setColor(Color.RED);
        g.fillRect(playerX, playerY, 50, 50);
    }

    @Override
    public void keyTyped(KeyEvent e) {}

    @Override
    public void keyPressed(KeyEvent e) {
        int key = e.getKeyCode();

        // Move left
        if (key == KeyEvent.VK_A) {
            isMovingLeft = true;
        }

        // Move right
        if (key == KeyEvent.VK_D) {
            isMovingRight = true;
        }

        // Jump (spacebar)
        if (key == KeyEvent.VK_SPACE && !isJumping) {
            isJumping = true;
            playerVelocityY = -15; // Set a velocity for jumping
        }
    }

    @Override
    public void keyReleased(KeyEvent e) {
        int key = e.getKeyCode();

        // Stop moving left
        if (key == KeyEvent.VK_A) {
            isMovingLeft = false;
        }

        // Stop moving right
        if (key == KeyEvent.VK_D) {
            isMovingRight = false;
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        // Update player position and jump physics
        if (isJumping) {
            playerVelocityY += 1; // Simulate gravity
        }

        playerY += playerVelocityY;

        // Prevent the player from falling below the ground level (floor)
        if (playerY >= 300) {
            playerY = 300;
            playerVelocityY = 0;
            isJumping = false;
        }

        // Handle horizontal movement (WASD)
        if (isMovingLeft) {
            playerX -= 5;
        }

        if (isMovingRight) {
            playerX += 5;
        }

        // Repaint the screen
        repaint();
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Simple Game");
        SimpleGame game = new SimpleGame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(game);
        frame.pack();
        frame.setVisible(true);
    }
}

