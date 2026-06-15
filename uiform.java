

import java.awt.EventQueue;

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
import java.awt.Font;
import javax.swing.DefaultComboBoxModel;
import java.awt.Color;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class uiform {

	private JFrame frame;
	private JTextField textField;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					uiform window = new uiform();
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
	public uiform() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 533, 462);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		JTabbedPane tabbedPane = new JTabbedPane(JTabbedPane.TOP);
		tabbedPane.setBounds(91, 146, 5, 5);
		frame.getContentPane().add(tabbedPane);
		
		JTabbedPane tabbedPane_1 = new JTabbedPane(JTabbedPane.TOP);
		tabbedPane_1.setBounds(0, 0, 509, 369);
		frame.getContentPane().add(tabbedPane_1);
		
		JPanel panel = new JPanel();
		tabbedPane_1.addTab("New tab", null, panel, null);
		panel.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("Enter the number of parking spots:");
		lblNewLabel.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblNewLabel.setBounds(32, 31, 303, 30);
		panel.add(lblNewLabel);
		
		JList list = new JList();
		list.setBounds(288, 60, 1, 1);
		panel.add(list);
		
		JSpinner spinner = new JSpinner();
		spinner.setFont(new Font("Tahoma", Font.PLAIN, 18));
		spinner.setBounds(345, 40, 101, 20);
		panel.add(spinner);
		
		JLabel lblNewLabel_1 = new JLabel("Choose Tree type:");
		lblNewLabel_1.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblNewLabel_1.setBounds(32, 76, 225, 30);
		panel.add(lblNewLabel_1);
		
		JComboBox comboBox = new JComboBox();
		comboBox.setToolTipText("Binary Search tree\r\nAVL tree\r\n\r\n");
		comboBox.setModel(new DefaultComboBoxModel(new String[] {"Binary Search tree", "AVL tree"}));
		comboBox.setSelectedIndex(2);
		comboBox.setBounds(345, 84, 126, 21);
		panel.add(comboBox);
		
		JButton btnNewButton = new JButton("Save        ");
		btnNewButton.setFont(new Font("Tahoma", Font.PLAIN, 18));
		btnNewButton.setBounds(54, 141, 359, 21);
		panel.add(btnNewButton);
		
		JPanel panel_1 = new JPanel();
		tabbedPane_1.addTab("New tab", null, panel_1, null);
		panel_1.setLayout(null);
		
		JLabel lblNewLabel_3 = new JLabel("Enter your vehicle Reg.no:");
		lblNewLabel_3.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblNewLabel_3.setBounds(20, 20, 245, 51);
		panel_1.add(lblNewLabel_3);
		
		textField = new JTextField();
		textField.setBounds(248, 39, 191, 19);
		panel_1.add(textField);
		textField.setColumns(10);
		
		JButton btnNewButton_1 = new JButton("I'd like to find a spot to park");
		btnNewButton_1.setFont(new Font("Tahoma", Font.PLAIN, 18));
		btnNewButton_1.setBounds(20, 91, 261, 21);
		panel_1.add(btnNewButton_1);
		
		JButton btnNewButton_2 = new JButton("I'm leaving");
		btnNewButton_2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btnNewButton_2.setFont(new Font("Tahoma", Font.PLAIN, 18));
		btnNewButton_2.setBounds(291, 91, 191, 21);
		panel_1.add(btnNewButton_2);
		
		JLabel lblNewLabel_4 = new JLabel("TextLabel");
		lblNewLabel_4.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblNewLabel_4.setBounds(31, 186, 127, 13);
		panel_1.add(lblNewLabel_4);
		
		JButton btnNewButton_3 = new JButton("Print Receipt");
		btnNewButton_3.setFont(new Font("Tahoma", Font.PLAIN, 18));
		btnNewButton_3.setBounds(50, 293, 172, 21);
		panel_1.add(btnNewButton_3);
		
		JButton btnNewButton_4 = new JButton("Clear");
		btnNewButton_4.setFont(new Font("Tahoma", Font.PLAIN, 18));
		btnNewButton_4.setBounds(280, 293, 145, 21);
		panel_1.add(btnNewButton_4);
		
		JProgressBar progressBar = new JProgressBar();
		progressBar.setIndeterminate(true);
		progressBar.setForeground(new Color(0, 0, 0));
		progressBar.setBackground(new Color(0, 0, 0));
		progressBar.setStringPainted(true);
		progressBar.setFont(new Font("Tahoma", Font.PLAIN, 16));
		progressBar.setBounds(216, 379, 255, 21);
		frame.getContentPane().add(progressBar);
		
		JLabel lblNewLabel_2 = new JLabel("Current Occupancy:");
		lblNewLabel_2.setFont(new Font("Tahoma", Font.PLAIN, 16));
		lblNewLabel_2.setBounds(20, 379, 158, 13);
		frame.getContentPane().add(lblNewLabel_2);
	}
}
