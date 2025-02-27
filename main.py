from flask import Flask, request, jsonify

app = Flask(__name__):print("Registered Routes:", app.url_map)

@app.route('/refund', methods=['POST'])
def process_refund():
    data = request.json
    order_id = data.get('order_id')
    reason = data.get('reason')

    if not order_id or not reason:
        return jsonify({'error': 'Missing order ID or reason'}), 400

    return jsonify({
        'order_id': order_id,
        'status': 'Refund Processed',
        'message': f'Refund request for order {order_id} due to {reason} has been processed.'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
