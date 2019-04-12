import subprocess
import socket
from flask import request, Flask, send_from_directory

app = Flask("ReMatch-Web")


@app.route('/')
def front_page():
    with open('index.html', 'r') as f:
        return f.read()


@app.route('/bootstrap.css')
def css():
    return send_from_directory('.', "bootstrap.css")


@app.route('/darkly.min.css')
def darklycss():
    return send_from_directory('.', "darkly.min.css")


@app.route("/execute", methods=['POST'])
def execute():
    args = request.form.to_dict()
    if args['video_type_day_two'] == 'disabled':
        args['video_type_day_two'] = ''
    if args['video_type_day_three'] == 'disabled':
        args['video_type_day_three'] = ''
    command = "python3 -m ReMatch " + args['video_id_day_one'] + " " + args['video_type_day_one'] + " " + args['event_key'] + " " + args['event_type'] + " " + args['video_id_day_two'] + " " + args['video_type_day_two'] + " " + args['video_id_day_three'] + " " + args['video_type_day_three']
    subprocess.Popen(command, shell=True)
    return send_from_directory('.', 'Execute.html')


@app.route('/set_tba_key', methods=['POST'])
def set_tba_key():
    with open('tbakey.txt', 'w') as f:
        f.write(request.args.get("key"))
    return "Key set successfully!"


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


if __name__ == "__main__":
    app.run(host=get_ip())
