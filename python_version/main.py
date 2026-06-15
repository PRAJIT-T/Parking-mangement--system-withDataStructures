import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from ui_App import Ui_Form
from ParkingSystem import ParkingSystem
from datetime import datetime

class ParkingApp(QWidget):
    def __init__(self):
        super(ParkingApp, self).__init__()
        
        # Set up the UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        # Initialize with no parking system yet
        self.parking_system = None
        
        # Set window title
        self.setWindowTitle("Parking Management System")
        
        # Default values
        self.ui.spin_noOfSpots.setValue(10)
        self.ui.progressBar_capacity.setValue(0)
        self.ui.label_exactCount.setText("0/0")
        self.ui.label_message.setText("Welcome to Parking Management System")
        
        # Connect signals and slots for Tab 1 (Configuration)
        self.ui.pushButton_saveConfig.clicked.connect(self.save_configuration)
        
        # Connect signals and slots for Tab 2 (Operations)
        self.ui.pushButton_enter.clicked.connect(self.add_car)
        self.ui.pushButton_leave.clicked.connect(self.remove_car)
        self.ui.pushButton_1.clicked.connect(self.clear_fields)  # Clear button
        self.ui.pushButton_2.clicked.connect(self.print_receipt)  # Print receipt button
        
        # Set initial tab names
        self.ui.tabWidget.setTabText(0, "Configuration")
        self.ui.tabWidget.setTabText(1, "Parking Operations")
        
        # Disable the operations tab until configuration is saved
        self.ui.tabWidget.setTabEnabled(1, False)
    
    def save_configuration(self):
        """Set up the parking system with the chosen configuration"""
        num_spots = self.ui.spin_noOfSpots.value()
        if num_spots <= 0:
            QMessageBox.warning(self, "Invalid Input", "Number of parking spots must be greater than 0")
            return
            
        tree_type = self.ui.comboBox_treeTypes.currentIndex()
        
        # Initialize the parking system with your implementation
        self.parking_system = ParkingSystem(num_spots, tree_type)
        
        # Update UI
        self.ui.label_exactCount.setText(f"0/{num_spots}")
        self.ui.progressBar_capacity.setValue(0)
        
        # Enable operations tab and switch to it
        self.ui.tabWidget.setTabEnabled(1, True)
        self.ui.tabWidget.setCurrentIndex(1)
        
        QMessageBox.information(self, "Configuration Saved", 
                               f"Parking system initialized with {num_spots} spots using " +
                               self.ui.comboBox_treeTypes.currentText())
    
    def add_car(self):
        """Add a car to the parking system"""
        if not self.parking_system:
            QMessageBox.warning(self, "Error", "Please configure the parking system first")
            return
            
        reg_no = self.ui.lineEdit_enterRegNo.text().strip()
        if not reg_no:
            QMessageBox.warning(self, "Invalid Input", "Please enter a registration number")
            return
            
        # Check if parking is full
        if self.parking_system.current_size >= self.parking_system.max_size:
            self.ui.label_message.setText("Parking is full. No spots available.")
            self.parking_system.print_tree()
            self.parking_system.print_queue()
            return
            
        # Try to add the car using your implementation
        try:
            self.parking_system.add_car(reg_no)
            self.ui.label_message.setText(f"Park your car {reg_no} in the parking spot {self.parking_system.last_spotID()}")
            self.update_occupancy_display()
            self.parking_system.print_tree()
            self.parking_system.print_queue()
        except Exception as e:
            self.ui.label_message.setText(f"Error: {str(e)}")
            self.parking_system.print_tree()
            self.parking_system.print_queue()
    
    def remove_car(self):
        """Remove a car from the parking system"""
        if not self.parking_system:
            self.parking_system.print_tree()
            self.parking_system.print_queue()
            QMessageBox.warning(self, "Error", "Please configure the parking system first")
            return
            
        reg_no = self.ui.lineEdit_enterRegNo.text().strip()
        if not reg_no:
            QMessageBox.warning(self, "Invalid Input", "Please enter a registration number")
            self.parking_system.print_tree()
            self.parking_system.print_queue()
            return
            
        # Try to remove the car using your implementation
        try:
            self.parking_system.remove_car(reg_no)
            self.ui.label_message.setText(f"Car with registration {reg_no} has left the parking")
            self.update_occupancy_display()
            self.parking_system.print_tree()
            self.parking_system.print_queue()
        except Exception as e:
            self.ui.label_message.setText(f"Error: {str(e)}")
            self.parking_system.print_tree()
            self.parking_system.print_queue()
    
    def clear_fields(self):
        """Clear the input fields and messages"""
        self.ui.lineEdit_enterRegNo.clear()
        self.ui.label_message.setText("")

    
    def print_receipt(self):
        """Print a receipt for the current operation"""
        reg_no = self.ui.lineEdit_enterRegNo.text().strip()
        if not reg_no:
            QMessageBox.warning(self, "Invalid Input", "Please enter a registration number")
            return
        
        # Generate a parking receipt with clean date and time formatting
        
        current_datetime = datetime.now()
        receipt_text = f"""
        PARKING RECEIPT
        ---------------
        Vehicle Reg. No: {reg_no}
        Date: {current_datetime.strftime("%d/%m/%Y")}
        Time: {current_datetime.strftime("%H:%M:%S")}
        ---------------
        Thank you for using our Parking System!
        """
        
        QMessageBox.information(self, "Receipt", receipt_text)
        
    def update_occupancy_display(self):
        """Update the occupancy display based on current state"""
        if not self.parking_system:
            return
            
        # Get current occupancy information from your implementation
        self.parking_system.update_status()
        current_count = self.parking_system.current_size
        max_size = self.parking_system.max_size
        occupancy_percentage = self.parking_system.get_occupancy_percentage()
        
        # Update text display
        self.ui.label_exactCount.setText(f"{current_count}/{max_size}")
        
        # Update progress bar
        self.ui.progressBar_capacity.setValue(occupancy_percentage)

def main():
    app = QApplication(sys.argv)
    window = ParkingApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()