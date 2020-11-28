#Antonio Manilla Maldonado
#Evaluación
#Modules
from flask import Flask, jsonify
import csv

#Instance of flask
app = Flask(__name__)

#Functions -----------------------------------------------------------------
#Decorator
@app.route("/", methods=["GET"])
def read_csv():
    #reads the csv at the given path in the open sentence, then, with the list
    #appends the values of each row as a single element of the list. Later, it
    #jsonify the list so it can be displayed
    list_1 = []
    with open("data/employees.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        for data in reader:
            list_1.append(data)
    return jsonify(list_1)

#Main --------------------------------------------------------------
if __name__ == "__main__":
    #app.run(debug=True)
    #app.run(debug=True, port=5050)

    #runs the instance with the given ip and port
    app.run(debug=True, host="0.0.0.0", port=5050)