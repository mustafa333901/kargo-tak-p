from flask import Flask, jsonify, request
app = Flask(__name__)

# Simulated shipment data
shipments = {
    "123456": {"status": "Yolda", "estimated_delivery": "2024-12-10"},
    "654321": {"status": "Teslim Edildi", "estimated_delivery": "2024-12-01"}
}

@app.route("/track/<tracking_number>", methods=["GET"])
def track_shipment(tracking_number):
    shipment = shipments.get(tracking_number)
    if shipment:
        return jsonify(shipment)
    return jsonify({"error": "Kargo bulunamadı!"}), 404

if __name__ == "__main__":
    app.run(debug=True)
