import java.awt.EventQueue;
import java.awt.Font;
import java.awt.Color;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

import javax.swing.JFrame;
import javax.swing.JTabbedPane;
import javax.swing.JPanel;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JSpinner;
import javax.swing.JComboBox;
import javax.swing.JButton;
import javax.swing.JProgressBar;
import javax.swing.JTextField;
import javax.swing.DefaultComboBoxModel;
import javax.swing.SpinnerNumberModel;
import javax.swing.JOptionPane;

import DataStructures.*;

public class ParkingManagementUI {

    private JFrame frame;
    private JTextField regNoField;
    private JSpinner parkingSpotsSpinner;
    private JComboBox<String> treeTypeComboBox;
    private JProgressBar occupancyProgressBar;
    private JLabel resultLabel;
    private JTabbedPane tabbedPane;
    
    // Reference to the parking system
    private ParkingSystem parkingSystem;

    /**
     * Launch the application.
     */
    public static void main(String[] args) {
        EventQueue.invokeLater(new Runnable() {
            public void run() {
                try {
                    ParkingManagementUI window = new ParkingManagementUI();
                    window.frame.setVisible(true);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
    }

    /**
     * Create the application.
     */
    public ParkingManagementUI() {
        initialize();
    }

    /**
     * Initialize the contents of the frame.
     */
    private void initialize() {
        frame = new JFrame("Parking Management System");
        frame.setBounds(100, 100, 533, 462);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().setLayout(null);
        
        tabbedPane = new JTabbedPane(JTabbedPane.TOP);
        tabbedPane.setBounds(0, 0, 509, 369);
        frame.getContentPane().add(tabbedPane);
        
        // Setup panel (first tab)
        JPanel setupPanel = new JPanel();
        tabbedPane.addTab("Setup", null, setupPanel, null);
        setupPanel.setLayout(null);
        
        JLabel lblNewLabel = new JLabel("Enter the number of parking spots:");
        lblNewLabel.setFont(new Font("Tahoma", Font.PLAIN, 18));
        lblNewLabel.setBounds(32, 31, 303, 30);
        setupPanel.add(lblNewLabel);
        
        parkingSpotsSpinner = new JSpinner(new SpinnerNumberModel(10, 1, 1000, 1));
        parkingSpotsSpinner.setFont(new Font("Tahoma", Font.PLAIN, 18));
        parkingSpotsSpinner.setBounds(345, 40, 101, 20);
        setupPanel.add(parkingSpotsSpinner);
        
        JLabel lblNewLabel_1 = new JLabel("Choose Tree type:");
        lblNewLabel_1.setFont(new Font("Tahoma", Font.PLAIN, 18));
        lblNewLabel_1.setBounds(32, 76, 225, 30);
        setupPanel.add(lblNewLabel_1);
        
        treeTypeComboBox = new JComboBox<>();
        treeTypeComboBox.setToolTipText("Select tree implementation");
        treeTypeComboBox.setModel(new DefaultComboBoxModel<>(new String[] {"Binary Search Tree", "AVL Tree"}));
        treeTypeComboBox.setSelectedIndex(0);
        treeTypeComboBox.setBounds(345, 84, 126, 21);
        setupPanel.add(treeTypeComboBox);
        
        JButton saveButton = new JButton("Initialize Parking System");
        saveButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                initializeParkingSystem();
            }
        });
        saveButton.setFont(new Font("Tahoma", Font.PLAIN, 18));
        saveButton.setBounds(54, 141, 359, 21);
        setupPanel.add(saveButton);
        
        // Operations panel (second tab)
        JPanel operationsPanel = new JPanel();
        tabbedPane.addTab("Operations", null, operationsPanel, null);
        operationsPanel.setLayout(null);
        
        JLabel lblNewLabel_3 = new JLabel("Enter your vehicle Reg.no:");
        lblNewLabel_3.setFont(new Font("Tahoma", Font.PLAIN, 18));
        lblNewLabel_3.setBounds(20, 20, 245, 51);
        operationsPanel.add(lblNewLabel_3);
        
        regNoField = new JTextField();
        regNoField.setBounds(248, 39, 191, 19);
        operationsPanel.add(regNoField);
        regNoField.setColumns(10);
        
        JButton parkButton = new JButton("I'd like to find a spot to park");
        parkButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                parkCar();
            }
        });
        parkButton.setFont(new Font("Tahoma", Font.PLAIN, 18));
        parkButton.setBounds(20, 91, 261, 21);
        operationsPanel.add(parkButton);
        
        JButton leaveButton = new JButton("I'm leaving");
        leaveButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                removeCar();
            }
        });
        leaveButton.setFont(new Font("Tahoma", Font.PLAIN, 18));
        leaveButton.setBounds(291, 91, 191, 21);
        operationsPanel.add(leaveButton);
        
        resultLabel = new JLabel("System ready");
        resultLabel.setFont(new Font("Tahoma", Font.PLAIN, 18));
        resultLabel.setBounds(31, 186, 400, 60);
        operationsPanel.add(resultLabel);
        
        JButton printReceiptButton = new JButton("Print Receipt");
        printReceiptButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                printReceipt();
            }
        });
        printReceiptButton.setFont(new Font("Tahoma", Font.PLAIN, 18));
        printReceiptButton.setBounds(50, 293, 172, 21);
        operationsPanel.add(printReceiptButton);
        
        JButton clearButton = new JButton("Clear");
        clearButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                regNoField.setText("");
                resultLabel.setText("System ready");
            }
        });
        clearButton.setFont(new Font("Tahoma", Font.PLAIN, 18));
        clearButton.setBounds(280, 293, 145, 21);
        operationsPanel.add(clearButton);
        
        JLabel lblNewLabel_2 = new JLabel("Current Occupancy:");
        lblNewLabel_2.setFont(new Font("Tahoma", Font.PLAIN, 16));
        lblNewLabel_2.setBounds(20, 379, 158, 13);
        frame.getContentPane().add(lblNewLabel_2);
        
        occupancyProgressBar = new JProgressBar();
        occupancyProgressBar.setValue(0);
        occupancyProgressBar.setForeground(new Color(50, 205, 50));
        occupancyProgressBar.setBackground(new Color(220, 220, 220));
        occupancyProgressBar.setStringPainted(true);
        occupancyProgressBar.setFont(new Font("Tahoma", Font.PLAIN, 16));
        occupancyProgressBar.setBounds(216, 379, 255, 21);
        frame.getContentPane().add(occupancyProgressBar);
        
        // Initially disable the operations tab until parking system is initialized
        tabbedPane.setEnabledAt(1, false);
    }
    
    /**
     * Initialize the parking system based on user input
     */
    private void initializeParkingSystem() {
        int numSpots = (Integer) parkingSpotsSpinner.getValue();
        int treeType;
        
        // Get the selected tree type
        switch (treeTypeComboBox.getSelectedIndex()) {
            case 1:
                treeType = ParkingSystem.AVL;
                break;
            default:
                treeType = ParkingSystem.BST;
                break;
        }
        
        // Initialize the parking system
        try {
            parkingSystem = new ParkingSystem(numSpots, treeType);
            
            // Update UI
            JOptionPane.showMessageDialog(frame, 
                "Parking system initialized with " + numSpots + " spots using " + 
                treeTypeComboBox.getSelectedItem() + " implementation.",
                "System Initialized", JOptionPane.INFORMATION_MESSAGE);
            
            // Enable the operations tab and switch to it
            tabbedPane.setEnabledAt(1, true);
            tabbedPane.setSelectedIndex(1);
            
            // Reset the occupancy bar
            updateOccupancyBar();
            
        } catch (Exception e) {
            JOptionPane.showMessageDialog(frame, 
                "Error initializing parking system: " + e.getMessage(),
                "Initialization Error", JOptionPane.ERROR_MESSAGE);
        }
    }
    
    /**
     * Park a car in the system
     */
    private void parkCar() {
        if (parkingSystem == null) {
            JOptionPane.showMessageDialog(frame, 
                "Please initialize the parking system first.",
                "System Not Initialized", JOptionPane.WARNING_MESSAGE);
            return;
        }
        
        String regNo = regNoField.getText().trim();
        if (regNo.isEmpty()) {
            JOptionPane.showMessageDialog(frame, 
                "Please enter a registration number.",
                "Input Error", JOptionPane.WARNING_MESSAGE);
            return;
        }
        
        try {
            int success = parkingSystem.addCar(regNo);
            if (success != -1) {
                resultLabel.setText("Park your car " + regNo + " in the spot "+this.parkingSystem.printLastSpotID());
                updateOccupancyBar();
            } else {
                resultLabel.setText("No parking spots available. Car " + regNo + " added to waiting queue.");
            }
        } catch (Exception e) {
            resultLabel.setText("Error: " + e.getMessage());
        }
    }
    
    /**
     * Remove a car from the system
     */
    private void removeCar() {
        if (parkingSystem == null) {
            JOptionPane.showMessageDialog(frame, 
                "Please initialize the parking system first.",
                "System Not Initialized", JOptionPane.WARNING_MESSAGE);
            return;
        }
        
        String regNo = regNoField.getText().trim();
        if (regNo.isEmpty()) {
            JOptionPane.showMessageDialog(frame, 
                "Please enter a registration number.",
                "Input Error", JOptionPane.WARNING_MESSAGE);
            return;
        }
        
        try {
            boolean success = parkingSystem.removeCar(regNo);
            if (success) {
                resultLabel.setText("Car " + regNo + " removed successfully.");
                updateOccupancyBar();
            } else {
                resultLabel.setText("Car with registration " + regNo + " not found in the system.");
            }
        } catch (Exception e) {
            resultLabel.setText("Error: " + e.getMessage());
        }
    }
    
    /**
     * Print a receipt for the parking transaction
     */
    private void printReceipt() {
        if (parkingSystem == null) {
            JOptionPane.showMessageDialog(frame, 
                "Please initialize the parking system first.",
                "System Not Initialized", JOptionPane.WARNING_MESSAGE);
            return;
        }
        
        String regNo = regNoField.getText().trim();
        if (regNo.isEmpty()) {
            JOptionPane.showMessageDialog(frame, 
                "Please enter a registration number.",
                "Input Error", JOptionPane.WARNING_MESSAGE);
            return;
        }
        
        // This would be implemented based on how the ParkingSystem tracks car entry/exit times
        // For now, we'll show a simple receipt
        JOptionPane.showMessageDialog(frame,
            "===== PARKING RECEIPT =====\n" +
            "Registration No: " + regNo + "\n" +
            "Date/Time: " + java.time.LocalDateTime.now() + "\n" +
            "Thank you for using our parking system!",
            "Receipt", JOptionPane.INFORMATION_MESSAGE);
    }
    




















    
    /**
     * Update the occupancy progress bar
     */
    private void updateOccupancyBar() {
        if (parkingSystem != null) {
            int totalSpots = parkingSystem.getTotalSpots();
            int occupiedSpots = parkingSystem.getOccupiedSpots();
            int percentage = (totalSpots > 0) ? (occupiedSpots * 100 / totalSpots) : 0;
            
            occupancyProgressBar.setValue(percentage);
            occupancyProgressBar.setString(occupiedSpots + "/" + totalSpots + " (" + percentage + "%)");
            
            // Change color based on occupancy level
            if (percentage < 50) {
                occupancyProgressBar.setForeground(new Color(50, 205, 50)); // Green
            } else if (percentage < 80) {
                occupancyProgressBar.setForeground(new Color(255, 165, 0)); // Orange
            } else {
                occupancyProgressBar.setForeground(new Color(255, 0, 0)); // Red
            }
        }
    }
}
