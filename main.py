from api.routes import create_app
from gui.main_window import MainWindow
from PyQt5.QtWidgets import QApplication
import sys
import threading

def run_flask():
    app = create_app()
    app.run(debug=False)

if __name__ == '__main__':
    # Start Flask server in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Start PyQt5 application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())