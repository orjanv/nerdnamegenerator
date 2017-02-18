from flask import Flask, render_template, request
import sys, random

app = Flask(__name__)

boytitles = ['Mr.','Master','Lord','Sir','Earl','Baron']
girltitles = ['Miss','Mrs.','Ms.','Dame','Madam','Lady']
boynames = ['Arthur','Geordi','Jimmy','Kent','Clark','Alyx','Alistair','Sheldon', \
            'Jace','Tyr','Anakin','Ganon','Arnold','Spike','Harry','Ender','Desmond', \
            'Dax','Zack','Xander','Ronan','Oliver','Hank','Jamie','Rory','Calvin', \
            'Wesley','Willem','Mars','Hermes','Kenobi','Galileo','Buran','Kelvin', \
            'Finnick','Jorah']
girlnames = ['Ada','Echo','Fleur','Leela','Ruby','Rowena','Natasha','Nichelle', \
             'Veronica','Sabine','Trillian','Leia','Persephone','Peggy','Sonya', \
             'Teyla','Zelda','Coraline','Aurora','Carmen','Hera','Kaylee','Auri', \
             'Keiko','Thalia','Kara','Adria','Daisy','Jemma','Primrose','Sora', \
             'Ashildr','Peeta','Dione','Tauriel','Khaleesi']
geekwords = ['Bit','Byte','Dword','Nibble','Word','Emoji','Spam','Mouse','Twain', \
             'Hashtag','Like','Poke','Troll','Tweet','Blob','Bug','Crapplet','Tree', \
             'Egg','Gui','Hardcopy','Hash','Thunking','Virus','Warez','Worm','404', \
             'Cookies','Wiki','Afk','Ama','Key','Cki','Crack','Fubar','Hack','Id10t', \
             'Interwebs','Irl','Kludge','Kos','Lmao','Lmfao','Lol','Lulz','N00b', \
             'Pebkac','Podcast','Pr0n','Pwn','Rofl','Rotflmfao','Snafu','Teh','Tubez']


@app.route('/', methods=['POST', 'GET'])
def generator():

    error = ''
    gender = ''
    generatedname = ''

    if request.method == "POST":
        try:
            gender = request.form['gender']
            if gender == 'b': # if boy
                generatedname = (random.choice(boytitles) + " " + random.choice(boynames) + random.choice(geekwords))

            if gender == 'g': # if girl
                generatedname = (random.choice(girltitles) + " " + random.choice(girlnames) + random.choice(geekwords))

        except:
            return("didn't work")
    return render_template('index.html', generatedname=generatedname)


if __name__ == "__main__":
    app.run('0.0.0.0', port=3000)
