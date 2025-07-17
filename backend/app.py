from flask import Flask, request, render_template
import os, datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'data/uploads'

# ✅ Only create folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('files')
        tags = request.form.get('tags')
        title = request.form.get('title')
        description = request.form.get('description')
        timestamp = datetime.datetime.now().isoformat()

        saved_files = []

        for file in uploaded_files:
            if file.filename:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                saved_files.append({
                    'filename': filename,
                    'filepath': filepath,
                    'tags': tags,
                    'title': title,
                    'description': description,
                    'timestamp': timestamp
                })

        return f"Uploaded {len(saved_files)} files successfully."

    return render_template('upload.html')
