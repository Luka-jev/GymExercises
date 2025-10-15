from flask import render_template, Flask
from app import app

class IndexController:

    @app.route('/', methods=['GET'])
    def index():
        triceps = [
            {"exo": "Barre au front", "img": "https://www.docteur-fitness.com/wp-content/uploads/2000/09/barre-front.gif"},
            {"exo": "Dips", "img": "https://louismove.com/wp-content/uploads/2022/12/02511101-Chest-Dip_Chest_medium.png.webp"},
            {"exo": "Extension corde à la poulie", "img": "https://www.docteur-fitness.com/wp-content/uploads/2021/10/extension-triceps-poulie-haute-corde.gif"},
            {"exo": "Développé couché prise serrée", "img": "https://www.docteur-fitness.com/wp-content/uploads/2022/11/developpe-couche-prise-serree-smith-machine.gif"},
            {"exo": "Kickback haltère", "img": "https://www.docteur-fitness.com/wp-content/uploads/2022/12/kickback-debout-avec-halteres.gif"},
            {"exo": "Extension poulie barre droite", "img": "https://www.fitadium.com/conseils/wp-content/uploads/2020/07/02011301-Cable-Pushdown_Upper-Arms_720.gif"}
        ]

        jambes = [
            {"exo": "Squat barre", "img": "https://www.docteur-fitness.com/wp-content/uploads/2021/11/homme-faisant-un-squat-avec-barre.gif"},
            {"exo": "Presse à cuisses", "img": "https://www.docteur-fitness.com/wp-content/uploads/2000/06/presse-a-cuisse-exercice-musculation.gif"},
            {"exo": "Fentes marchées", "img": "https://www.docteur-fitness.com/wp-content/uploads/2021/12/fentes-avant-kettlebell.gif"},
            {"exo": "Extension de jambes", "img": "https://www.docteur-fitness.com/wp-content/uploads/2000/06/leg-extension-exercice-musculation.gif"},
            {"exo": "Flexion jambes allongé", "img": "https://www.docteur-fitness.com/wp-content/uploads/2021/10/leg-curl-allonge.gif"},
            {"exo": "Mollets debout machine", "img": "https://www.docteur-fitness.com/wp-content/uploads/2021/10/extension-mollets-debout-machine.gif"}
        ]

        biceps = [
            {"exo": "Curl barre EZ", "img": "https://muscu-street-et-crossfit.fr/wp-content/uploads/2021/10/Muscles-Biceps-curl.001-980x551.jpeg"},
            {"exo": "Curl haltères alterné", "img": "https://www.docteur-fitness.com/wp-content/uploads/2022/08/curl-biceps-avec-halteres-alterne.gif"},
            {"exo": "Curl incliné haltères", "img": "https://www.docteur-fitness.com/wp-content/uploads/2021/10/curl-haltere-incline.gif"},
            {"exo": "Curl marteau", "img": "https://www.fitadium.com/conseils/wp-content/uploads/2020/11/03131301-Dumbbell-Hammer-Curl_Forearm_720.gif"},
            {"exo": "Curl pupitre", "img": "https://www.docteur-fitness.com/wp-content/uploads/2022/01/curl-au-pupitre-barre-ez-larry-scott.gif"},
            {"exo": "Curl à la poulie basse", "img": "https://www.docteur-fitness.com/wp-content/uploads/2021/10/curl-biceps-poulie-basse.gif"}
        ]

        pecs = [
            {"exo": "Développé couché barre", "img": "https://muscu-street-et-crossfit.fr/wp-content/uploads/2021/09/Muscles-DC.001-980x551.jpeg"},
            {"exo": "Développé incliné haltères", "img": "https://louismove.com/wp-content/uploads/2022/12/03141101-Dumbbell-Incline-Bench-Press_Chest-FIX_medium-1.png.webp"},
            {"exo": "Pec fly machine", "img": "https://training.fit/wp-content/uploads/2020/02/butterflys-800x448.png"},
            {"exo": "Développé décliné barre", "img": "https://purshape.com/wp-content/uploads/2021/03/Exercice-developpe-couche-incline-avec-barre.jpg"},
            {"exo": "Câble vis-à-vis", "img": "https://louismove.com/wp-content/uploads/2023/01/02271101-Cable-Standing-Fly_Chest-FIX_medium.png"},
            {"exo": "Pompes lestées", "img": "https://cdn.shopify.com/s/files/1/0680/7843/6626/files/pompes_incline_480x480.png?v=1692505131"}
        ]

        epaules = [
            {"exo": "Développé haltères assis", "img": "https://i.pinimg.com/originals/0d/e1/98/0de1986e80eba3c85cf3853c8fc0b8d7.gif"},
            {"exo": "Développé militaire barre", "img": "https://muscu-street-et-crossfit.fr/wp-content/uploads/2022/03/Muscles-DM-Halteres.001-980x551.jpeg"},
            {"exo": "Élévations latérales", "img": "https://www.fitadium.com/conseils/wp-content/uploads/2020/08/03341301-Dumbbell-Lateral-Raise_shoulder_720.gif"},
            {"exo": "Élévations frontales", "img": "https://www.fitadium.com/conseils/wp-content/uploads/2020/08/03101301-Dumbbell-Front-Raise_Shoulders_720.gif"},
            {"exo": "Oiseau (reverse fly)", "img": "https://www.docteur-fitness.com/wp-content/uploads/2021/12/pec-deck-inverse.gif"},
            {"exo": "Face pull", "img": "https://louismove.com/wp-content/uploads/2023/02/56561101-Cable-Standing-Face-Pull-with-rope_Shoulders_medium.png.webp"}
        ]

        dos = [
            {"exo": "Tractions pronation", "img": "https://225fitnessstudio.fr/illustration/prise-en-pronation-vs-supination-au-traction-400-208.jpg"},
            {"exo": "Rowing machine", "img": "https://louismove.com/wp-content/uploads/2022/12/54471101-Lever-Pronated-Grip-Seated-Row-plate-loaded_Back_medium-1.png.webp"},
            {"exo": "Rowing haltère unilatéral", "img": "https://louismove.com/wp-content/uploads/2022/12/02921101-Dumbbell-Bent-over-Row_back_Back-AFIX_medium.png.webp"},
            {"exo": "Tirage vertical poulie haute", "img": "https://louismove.com/wp-content/uploads/2022/12/01971101-Cable-Wide-Pulldown_Back-FIX_medium.png.webp"},
            {"exo": "Tirage horizontal poulie basse", "img": "https://louismove.com/wp-content/uploads/2022/12/26611101-Cable-Seated-Row-with-V-bar_Back_medium.png.webp"},
            {"exo": "Pull-over à la poulie", "img": "https://louismove.com/wp-content/uploads/2022/12/60361101-Cable-Straight-Arm-Pulldown-VERSION-2_Back_medium.png"}
        ]

        abdos = [
            {"exo": "Crunch machine", "img": "https://www.docteur-fitness.com/wp-content/uploads/2022/04/crunch-machine-abdos.gif"},
            {"exo": "Relevé de jambes suspendu", "img": "https://www.docteur-fitness.com/wp-content/uploads/2000/07/releve-de-genoux-suspendu-exercice-musculation.gif"},
            {"exo": "Crunch à la poulie haute", "img": "https://www.docteur-fitness.com/wp-content/uploads/2000/06/crunch-poulie-haute-exercice-musculation.gif"},
            {"exo": "Rotation du buste machine", "img": "https://www.docteur-fitness.com/wp-content/uploads/2022/02/rotation-buste-debout-poulie.gif"},
            {"exo": "Gainage lesté", "img": "https://www.docteur-fitness.com/wp-content/uploads/2022/05/planche-abdos.gif"},
            {"exo": "Planche latérale", "img": "https://www.docteur-fitness.com/wp-content/uploads/2022/08/planche-laterale-avec-rotation.gif"}
        ]

        return render_template('index.html', triceps=triceps, jambes=jambes, biceps=biceps, pecs=pecs, epaules=epaules, dos=dos, abdos=abdos)


    @app.route('/seance', methods=['GET'])
    def seance():
        return render_template('seance.html')
