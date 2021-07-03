from flask import Flask, request, send_from_directory
import os

app = Flask(__name__, static_url_path='')

port = int(os.environ.get('PORT', 9999))


@app.route("/")
def send_html():
    return send_from_directory('build', "index.html")

@app.route("/static/<folder>/<filename>")
def send_file(folder, filename):
    print (folder, filename)
    return send_from_directory('build/static/' + folder, filename)
    


#LAST LINE
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)