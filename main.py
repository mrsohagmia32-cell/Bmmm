import os
import requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

API_KEY = "00872f5f0b0c75305cc49069d7691006"
API_URL = "https://likefollowerbuy.com/api/v2"


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/api/order", methods=["POST"])
def place_order():
  data = request.form.to_dict()

  # ইউজার যে সার্ভিস বা লিংক দিয়েছে তা রিসিভ করা
  service_id = data.get("service")
  link = data.get("link")
  quantity = data.get("quantity")

  if not service_id or not link or not quantity:
    return jsonify({"status": "error", "message": "সব তথ্য সঠিকভাবে দিন!"})

  # এপিআই পেমেন্ট বা অর্ডারের পেলোড তৈরি (সিক্রেট কি এখানে যুক্ত হবে, ব্রাউজারে যাবে না)
  payload = {"key": API_KEY, "action": "add", "service": service_id, "link": link, "quantity": quantity}

  try:
    response = requests.post(API_URL, data=payload)
    result = response.json()
    return jsonify(result)
  except Exception as e:
    return jsonify({"status": "error", "message": str(e)})


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port)
