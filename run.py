#!/usr/bin/env python3
from my_app import app

# without livereload (vanilla Flask)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
