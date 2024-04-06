from flask import Flask, request
app = Flask(__name__)

"""  esimerkki pyynnöstä    http://127.0.0.1:3000/alkuluku?Number=31      """

@app.route('/alkuluku')
def primenumber():
    # Get arguments from the request

    args = request.args
    Number = args.get("Number")

    if Number is None:     # Check if Number is defined

        return "Number not defined"
    try:
        Number = int(Number)       # number must be int

    except ValueError:
        return "Error: Number must be an integer."

    if Number < 0:
        return "kielteinen luku ei voi olla alkulukuna."

    if Number == 1 or Number == 0:
        return {"Number": Number, "isPrime": False}

    is_Prime = True
    for i in range(2, int(Number ** 0.5) + 1):
        if Number % i == 0:
            is_Prime = False
            break

    return {"Number": Number, "isPrime": is_Prime}

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

