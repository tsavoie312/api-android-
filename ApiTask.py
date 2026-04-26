from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for permissions  
permissions = {
    'camera': False,
    'location': False,
    'microphone': False
}

@app.route('/request_permission', methods=['POST'])
def request_permission():
    data = request.json
    permission_type = data.get('permission_type')
    action = data.get('action')
    
    if permission_type not in permissions:
        return jsonify({'status': 'error', 'message': 'Invalid permission type'}), 400
    
    if action == 'approve':
        permissions[permission_type] = True
        return jsonify({'status': 'success', 'message': f'{permission_type} permission granted.'}), 200
    elif action == 'deny':
        permissions[permission_type] = False
        return jsonify({'status': 'success', 'message': f'{permission_type} permission denied.'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Invalid action.'}), 400

@app.route('/get_permissions', methods=['GET'])
def get_permissions():
    return jsonify(permissions), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
