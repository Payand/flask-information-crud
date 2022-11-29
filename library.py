from flask import Flask,render_template,flash,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from forms import InformationForm


app = Flask(__name__)
 
app.config['SECRET_KEY']='66b7691d6b678ac4d6672d15a68a7397'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db = SQLAlchemy(app)

class Infos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(30), nullable=False)
    last_name=db.Column(db.String(30),nullable=False)
    email=db.Column(db.String(120),unique=True, nullable=False)
    phone_number=db.Column(db.Integer, nullable=False)
    
    
    def __repr__(self):
        return f"Infos('{self.id}','{self.first_name}','{self.last_name}','{self.email}','{self.phone_number}')"




@app.route('/')
def main():
    infos = Infos.query.all()
    return render_template('main-content.html',infos=infos)

@app.route('/add', methods=['GET','POST'])
def info_add():
    form =InformationForm()
    if form.validate_on_submit():
        infos = Infos(first_name=form.first_name.data, last_name=form.last_name.data,email=form.email.data,phone_number=form.phone_number.data)
        db.session.add(infos)
        db.session.commit()
        flash(f'{form.last_name.data} added to the list!','success')
        return redirect(url_for('main'))
    return render_template('add-update.html',title='Add-info',form=form,legend="Add You Info")



@app.route('/update/<int:id>',methods=['GET','POST'])
def update_info(id):
    info = Infos.query.get_or_404(id)
    form =InformationForm()
    if form.validate_on_submit():
        info.data = form.first_name.data
        info.last_name = form.last_name.data
        info.email = form.email.data
        info.phone_number = form.phone_number.data
        db.session.commit()
        flash('You information has been updated','success')
        return redirect(url_for('main'))
    elif request.method == "GET":
        form.first_name.data = info.first_name
        form.last_name.data=info.last_name
        form.email.data=info.email
        form.phone_number.data=info.phone_number  
    return render_template('add-update.html',title='Update',form=form,legend="Update Post")



@app.route('/delete/<int:id>',methods=['POST'])
def delete_info(id):
    info = Infos.query.get_or_404(id)
    db.session.delete(info)
    db.session.commit()
    flash('your information has been deleted','success')
    return redirect(url_for('main'))


if __name__=='__main__':
    app.run(debug=False)
