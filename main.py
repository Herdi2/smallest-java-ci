from flask import Flask, request, jsonify
import git, pytest

app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook_receiver():
    data = request.json
    
    # Get ssh url
    ssh_url = data['repository']['ssh_url']
    name = data['repository']['name']
    print("data:", ssh_url)
    # Clone repo to current directory
    git.Git(None).clone(ssh_url)    
    # Run pytest and get results
    retcode = pytest.main([name + "/test.py"])
    print(retcode)
    return jsonify({'message': 'Webhook received successfully'}), 200
if __name__ == '__main__':
    app.run(debug=True)