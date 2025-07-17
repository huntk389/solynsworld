from flask import Flask, request, render_template, jsonify
import os, datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'data/uploads'
if not os.path.isdir(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_files = request.files.getlist("file")
        tags = request.form.get("tags")
        title = request.form.get("title")
        description = request.form.get("description")
        timestamp = datetime.datetime.now().isoformat()
        saved_files = []
        for file in uploaded_files:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            saved_files.append({
                "title": title or filename,
                "tags": tags,
                "description": description,
                "timestamp": timestamp,
                "filename": filename
            })
        return jsonify({"status": "uploaded", "files": saved_files})

    return '''
        <form method="post" enctype="multipart/form-data">
            Title: <input type="text" name="title"><br>
            Description: <textarea name="description"></textarea><br>
            Tags (comma separated): <input type="text" name="tags"><br>
            Select files: <input type="file" name="file" multiple><br>
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
