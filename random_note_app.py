import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import QTimer

class RandomNoteApp(QWidget):
    """
    A PyQt5 application that displays random musical notes at a user-specified interval.
    
    Features:
    - Choose between all musical notes or only natural notes.
    - Adjustable time interval between note displays (default: 10 seconds).
    - Simple UI with buttons to start and exit the application.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Music Notes")
        self.setGeometry(100, 100, 400, 300)
        
        self.natural_notes = ["A", "B", "C", "D", "E", "F", "G"]
        self.all_notes = ["A", "A#", "Bb", "B", "C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab"]
        self.current_notes = []
        self.interval = 10  # default interval in seconds
        
        self.layout = QVBoxLayout()
        
        self.label = QLabel("Select An Option to Start", self)
        self.label.setStyleSheet("font-size: 40px; text-align: center;")
        self.layout.addWidget(self.label)

        # create a horizontal layout for the interval input
        interval_layout = QHBoxLayout()
        self.interval_label = QLabel("Time Interval (Seconds):", self)
        self.interval_input = QLineEdit(self)
        self.interval_input.setPlaceholderText("Enter interval (Seconds)")
        self.interval_input.setText(str(self.interval))

        interval_layout.addWidget(self.interval_label)
        interval_layout.addWidget(self.interval_input)
        self.layout.addLayout(interval_layout)  # add the horizontal layout to the main vertical layout

        self.all_notes_button = QPushButton("All Notes", self)
        self.all_notes_button.clicked.connect(lambda: self.start_game(self.all_notes))
        self.layout.addWidget(self.all_notes_button)
        
        self.natural_notes_button = QPushButton("Natural Notes", self)
        self.natural_notes_button.clicked.connect(lambda: self.start_game(self.natural_notes))
        self.layout.addWidget(self.natural_notes_button)
        
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.clicked.connect(self.close)
        self.layout.addWidget(self.exit_button)
        
        self.setLayout(self.layout)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_next_note)
    
    def start_game(self, notes):
        """
        Starts the note display cycle, shuffling the notes and setting the timer interval.
        
        Parameters:
        notes (list): List of musical notes to display.
        """
        try:
            self.interval = int(self.interval_input.text()) * 1000  # convert to milliseconds
            if self.interval <= 0:
                self.interval = 10000  # reset to default if invalid
        except ValueError:
            self.interval = 10000  # reset to default if input is not a number
        
        self.current_notes = notes[:]
        random.shuffle(self.current_notes)
        self.show_next_note()
        self.timer.start(self.interval)
    
    def show_next_note(self):
        """
        Displays the next note in the shuffled list. Stops when all notes have been displayed.
        """
        if self.current_notes:
            note = self.current_notes.pop(0)
            self.label.setText(note)
        else:
            self.label.setText("All Notes Displayed!")
            self.timer.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RandomNoteApp()
    window.show()
    sys.exit(app.exec_())