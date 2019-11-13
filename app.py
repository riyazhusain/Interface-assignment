import os
from flask import Flask, request, jsonify, make_response, render_template
from helpers import DataProcessing
from settings import *

app = Flask(__name__)


def table_view(data):
    return render_template("list.html",data = data)


@app.route("/interface/<path:input>", methods=['GET'])
def interface_view(input):
    filepath = 'config.txt'
    data_list = DataProcessing.get_data(filepath)
    if input == 'list':
        return table_view(data_list)
    if input == 'all':
        return jsonify(data_list)
    else:
        multiple_interfaces = [data_list[i] for i, x in enumerate(data_list) if x['interface'] == input]
        if len(multiple_interfaces) < 1:
            return make_response(jsonify("No Interface named {} found".format(input)), 404)
        else:
            return jsonify(multiple_interfaces)


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG_MODE)
