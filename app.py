from flask import Flask
from donor import get_donors

app = Flask(__name__)

@app.route('/')
def home():
    donors = get_donors()
    output = "<h1>🩸 Blood Donor Finder</h1>"
    
    for d in donors:
        output += f"<p>{d['name']} - {d['blood']} - {d['location']}</p>"
    
    return output

if __name__ == "__main__":
    app.run()
