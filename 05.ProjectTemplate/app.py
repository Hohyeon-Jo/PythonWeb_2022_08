from flask import Flask, render_template, request, current_app
import os
app = Flask(__name__)
@app.route('/')
def home():
    menu = {'home' :1, 'menu':0}
    return render_template('index.html', menu=menu)
@app.route('/menu', methods=['GET', 'POST'])
def menu():
    menu = {'home' :0, 'menu':1}
    if request.method == 'GET':
        languages = [
            {'disp':'영어', 'val':'en'},
            {'disp':'일어', 'val':'jp'},
            {'disp':'중국어', 'val':'cn'},
            {'disp':'프랑스어', 'val':'fr'},
            {'disp':'스페인어', 'val':'es'},
        ]
        return render_template('Menu.html', options=languages, menu=menu)
    else:
        # 사용자가 입력한 정보를 서버가 읽음
        index = request.form['index']
        lang = request.form['lang']
        lyrics = request.form['lyrics']
        print(lang, '\n', index, '\n', lyrics)
        f_image = request.files['image']
        print(f_image.filename)
        filename = os.path.join(current_app.root_path, 'static/upload/') + f_image.filename
        print(filename)
        f_image.save(filename)
        result = f_image.filename
        fname = f_image.filename
        return render_template('Menu_res.html',result=result, fname=fname, menu=menu)   
        
if  __name__ == '__main__':
    app.run(debug=True)