from app import create_app

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'config')))

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)