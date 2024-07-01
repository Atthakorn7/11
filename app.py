from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/control')
def control():
    return render_template('control.html')

@socketio.on('control')
def handle_control(command):
    print(f"Received command: {command}")
    # เพิ่มโค้ดเพื่อส่งคำสั่งไปยังรถโมเดล เช่น ใช้ serial
    # ser.write(command.encode())

if __name__ == '__main__':
    socketio.run(app, debug=True)
