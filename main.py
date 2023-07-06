import random
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    home_teks = '''
    <a href="/random_fact">View a random fact!</a>
    <br>
    <a href="/emot">View a random emot!</a>
    <br>
    <a href="/coin_hoki">Gambar coin atau angka coin? (klik di sini untuk menguji benarnya)</a>'''
    return home_teks

@app.route("/random_fact")

def index():

    a = ["Kebanyakan orang yang menderita kecanduan teknologi mengalami stres yang kuat ketika mereka berada di luar area jangkauan jaringan atau tidak dapat menggunakan perangkat mereka", "Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50 orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.", "Studi tentang ketergantungan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan", "Menurut sebuah studi tahun 2019, lebih dari 60 orang merespons pesan pekerjaan di ponsel mereka dalam waktu 15 menit setelah pulang kerja",
         "Salah satu cara untuk memerangi ketergantungan teknologi adalah dengan mencari kegiatan yang membawa kesenangan dan meningkatkan suasana hati", "Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten", 
         "Elon Musk juga menganjurkan regulasi jejaring sosial dan perlindungan data pribadi pengguna. Dia mengklaim bahwa jejaring sosial mengumpulkan sejumlah besar informasi tentang kita, yang kemudian dapat digunakan untuk memanipulasi pikiran dan perilaku kita", "Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini"]
    return f'<p>{random.choice(a)}</p>'
    

@app.route("/emot")

def imeg():
    emoot = ['😁', '😂', '😎', '😥', '😫', '😴', '😛', '😡']
    emooot = random.choice(emoot)
    return emooot

@app.route("/coin_hoki")

def lempar():
    coinnya = ['gambar', 'angka', 'coinnya ke buang hahahahaha']
    coin_random = random.choice(coinnya)
    return coin_random



app.run(debug=True)
