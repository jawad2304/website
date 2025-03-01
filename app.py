from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# File to store user data
USER_FILE = "users.xlsx"

def save_user(data):
    try:
        df = pd.read_excel(USER_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Name", "Department", "Year", "Section", "Password"])
    
    df = df.append(data, ignore_index=True)
    df.to_excel(USER_FILE, index=False)

@app.route("/")
def home():
    return render_template("index.html")  # ✅ Make sure you have index.html in 'templates' folder

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        department = request.form["department"]
        year = request.form["year"]
        section = request.form["section"]
        password = request.form["password"]
        
        user_data = {
            "Name": name,
            "Department": department,
            "Year": year,
            "Section": section,
            "Password": password
        }
        save_user(user_data)

        return redirect(url_for("home"))

    return render_template("frontreg.html")  # ✅ Check that 'frontreg.html' exists in 'templates'

@app.route("/posters")
def posters():
    return render_template("posters.html")  # ✅ Ensure 'posters.html' is in 'templates'

if __name__ == "__main__":
    app.run(debug=True)
