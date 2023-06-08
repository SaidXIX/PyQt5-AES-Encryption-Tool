from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QTextEdit

class EncryptWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create text box to write the message
        self.message_box = QTextEdit(self)
        self.message_box.setGeometry(50, 50, 300, 200)

        # Create button to encrypt message
        self.encrypt_button = QPushButton("Encrypt", self)
        self.encrypt_button.setGeometry(150, 270, 100, 30)
        self.encrypt_button.clicked.connect(self.encrypt_message)

    def encrypt_message(self):
        # Get the message to encrypt from the text box
        message = self.message_box.toPlainText()

        # Generate a random key and IV for AES encryption
        key = get_random_bytes(32)
        iv = get_random_bytes(16)

        # Create an AES cipher object
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Pad the message to a multiple of the block size
        padded_message = pad(message.encode(), AES.block_size)

        # Encrypt the message using AES encryption
        ciphertext = cipher.encrypt(padded_message)

        # Display the encrypted message in a message box
        QMessageBox.information(self, "Encrypted Message", ciphertext.hex())


if __name__ == '__main__':
    # Create the QApplication
    app = QApplication([])

    # Create the EncryptWindow
    encrypt_window = EncryptWindow()
    encrypt_window.show()

    # Run the QApplication event loop
    app.exec_()
