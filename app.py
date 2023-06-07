from flask import Flask, render_template, request
from tkinter import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    print("Switch 1:", data['switch1'])
    print("Switch 2:", data['switch2'])
    print("Switch 3:", data['switch3'])
    print("Entries:", data['entries'])
    root = Tk()
    label = Label(root, text=data)
    label.pack()

    root.mainloop()
    return 'Data received'
    
    

if __name__ == '__main__':
    app.run(debug=True)
