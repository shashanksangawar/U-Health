from __main__ import app


# class UI:
@app.route('/test', methods=['GET'])
def test():
    return 'it works!'
