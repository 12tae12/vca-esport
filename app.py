from flask import Flask, render_template, request

app = Flask(__name__)

# Store room data in a dictionary
room_data = {
    'rocket_league': [],
    'mario_kart_deluxe': [],
    'splatoon_3': [],
    'super_smash_bros': []
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rocket-league', methods=['GET', 'POST'])
def rocket_league():
    if request.method == 'POST':
        room_type = request.form.get('room_type')
        room_name = request.form.get('room_name')
        room_password = request.form.get('room_password')
        if room_type and room_name and room_password:
            room_data['rocket_league'].append({
                'type': room_type,
                'name': room_name,
                'password': room_password
            })
    return render_template('rocket_league.html', rooms=room_data['rocket_league'])

@app.route('/mario-kart-deluxe', methods=['GET', 'POST'])
def mario_kart_deluxe():
    if request.method == 'POST':
        room_type = request.form.get('room_type')
        room_name = request.form.get('room_name')
        room_password = request.form.get('room_password')
        if room_type and room_name and room_password:
            room_data['mario_kart_deluxe'].append({
                'type': room_type,
                'name': room_name,
                'password': room_password
            })
    return render_template('mario_kart_deluxe.html', rooms=room_data['mario_kart_deluxe'])

@app.route('/splatoon-3', methods=['GET', 'POST'])
def splatoon_3():
    if request.method == 'POST':
        room_type = request.form.get('room_type')
        room_name = request.form.get('room_name')
        room_password = request.form.get('room_password')
        if room_type and room_name and room_password:
            room_data['splatoon_3'].append({
                'type': room_type,
                'name': room_name,
                'password': room_password
            })
    return render_template('splatoon_3.html', rooms=room_data['splatoon_3'])

@app.route('/super-smash-bros', methods=['GET', 'POST'])
def super_smash_bros():
    if request.method == 'POST':
        room_type = request.form.get('room_type')
        room_name = request.form.get('room_name')
        room_password = request.form.get('room_password')
        if room_type and room_name and room_password:
            room_data['super_smash_bros'].append({
                'type': room_type,
                'name': room_name,
                'password': room_password
            })
    return render_template('super_smash_bros.html', rooms=room_data['super_smash_bros'])
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.png', mimetype='image/png')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
