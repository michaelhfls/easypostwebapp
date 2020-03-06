from flask import Flask, render_template, request, flash
from forms import InputForm

import easypost
easypost.api_key = "EZTK711e361986de4ad3baf565bc94e598d2S7d7naG8TT7HppxWTW6u2w"

app = Flask(__name__)


@app.route("/")
@app.route("/input", methods = ['GET', 'POST'])
def input():
    if request.method == 'POST':
        name = request.form['name']
        street = request.form['street']
        street1 = request.form['street1']
        city = request.form['city']
        state = request.form['state']
        zip = request.form['zip']
        country = request.form['country']
        company = request.form['company']
        name2 = request.form['name2']
        street2 = request.form['street2']
        street3 = request.form['street3']
        city2 = request.form['city2']
        state2 = request.form['state2']
        zip2 = request.form['zip2']
        country2 = request.form['country2']
        company2 = request.form['company2']
        length = request.form['length']
        width = request.form['width']
        height = request.form['height']
        weight = request.form['weight']


        try:
            fromaddress = easypost.Address.create(
                verifications = ['delivery'],
                name = name,
                street1 = street,
                street2 = street1,
                city = city,
                state = state,
                zip = zip,
                country = country,
                company = company
            )
            toaddress = easypost.Address.create(
                verifications = ['delivery'],
                name = name2,
                street1 = street2,
                street2 = street3,
                city = city2,
                state = state2,
                zip = zip2,
                country = country2,
                company = company2
            )
            parcel = easypost.Parcel.create(
                length = length,
                width = width,
                height = height,
                weight = weight
            )
            shipment = easypost.Shipment.create(
                to_address=toaddress,
                from_address=fromaddress,
                parcel = parcel
            )
            shipment.buy(rate=shipment.lowest_rate())
        except:
            return render_template('index.html')

        fromaddress = easypost.Address.create(
            verifications = ['delivery'],
            name = name,
            street1 = street,
            street2 = street1,
            city = city,
            state = state,
            zip = zip,
            country = country,
            company = company
        )
        toaddress = easypost.Address.create(
            verifications = ['delivery'],
            name = name2,
            street1 = street2,
            street2 = street3,
            city = city2,
            state = state2,
            zip = zip2,
            country = country2,
            company = company2
        )
        parcel = easypost.Parcel.create(
            length = length,
            width = width,
            height = height,
            weight = weight
        )
        shipment = easypost.Shipment.create(
            to_address=toaddress,
            from_address=fromaddress,
            parcel = parcel
        )
        shipment.buy(rate=shipment.lowest_rate())
        return render_template('input.html', input = shipment.postage_label.label_url)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
