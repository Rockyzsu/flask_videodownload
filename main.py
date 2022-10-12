from task import video_downloader
from flask import  Flask
from flask import request,jsonify,render_template
app = Flask(__name__)

@app.route('/vd',methods=['GET',"POST"])
def download():
    if request.method =='GET':
        return render_template('base.html')
    else:
        link = request.form.get('link')
        name = request.form.get('name')
        data={'status':True}
        ret = video_downloader.download(link,name)
        data['status'] = ret
        return jsonify(data)


if __name__=='__main__':
    app.run(host='0.0.0.0',port=18080,debug=True)