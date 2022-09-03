#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import Blueprint
from flask import Response
from smartmon import get_metrics

APP_PATH = "/metrics"

smartmon_exporter = Blueprint("smartmon-exporter", __name__, url_prefix=APP_PATH)


@smartmon_exporter.route("/", methods=["GET"])
def metrics():
    return Response("\n".join(get_metrics()), mimetype="text/plain")


if __name__ == "__main__":
    app = Flask(__name__)
    app.debug = True

    app.register_blueprint(smartmon_exporter)

    app.run(host="0.0.0.0", port=9110, threaded=False)
