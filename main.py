from flask import Flask, request, jsonify
import git

app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook_receiver():
    data = request.json
    ssh_url = data['repository']['ssh_url']
    print("data:", ssh_url)
    git.Git(None).clone(ssh_url)
    print("Received webhook data:", request)
    return jsonify({'message': 'Webhook received successfully'}), 200
if __name__ == '__main__':
    app.run(debug=True)