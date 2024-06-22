from flask import Flask, request, jsonify
import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

app = Flask(__name__)

# Database connection parameters
DB_NAME = os.getenv('DB_NAME', 'example_db')
DB_USER = os.getenv('DB_USER', 'example_user')
DB_PASS = os.getenv('DB_PASS', 'example_password')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')

# Establish the database connection
try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()
except Exception as e:
    print(f"Error connecting to the database: {e}")
    raise

# Create the 'words' table if it doesn't exist
try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS words (
            id SERIAL PRIMARY KEY,
            original TEXT NOT NULL,
            mirrored TEXT NOT NULL
        )
    """)
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f"Error creating 'words' table: {e}")
    raise

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})

@app.route('/api/mirror', methods=['GET'])
def mirror_word():
    try:
        word = request.args.get('word')
        if not word:
            return jsonify({"error": "No word provided"}), 400

        mirrored_word = word.swapcase()[::-1]

        # Execute INSERT query with proper exception handling
        try:
            cursor.execute("INSERT INTO words (original, mirrored) VALUES (%s, %s)", (word, mirrored_word))
            conn.commit()
        except Exception as e:
            conn.rollback()  # Rollback transaction in case of error
            print(f"Error executing SQL query: {e}")
            return jsonify({"error": "Database error"}), 500

        return jsonify({"transformed": mirrored_word})

    except Exception as e:
        print(f"Error in /api/mirror endpoint: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4004)

