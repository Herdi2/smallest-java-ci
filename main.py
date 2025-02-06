from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook_receiver():
    data = request.json
    print("data:", data['ssh_url'])
    print("Received webhook data:", request)
    return jsonify({'message': 'Webhook received successfully'}), 200
if __name__ == '__main__':
    app.run(debug=True)