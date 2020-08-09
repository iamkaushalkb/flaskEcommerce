# Importing Modules
from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class, secure_filename, FileStorage
from sqlalchemy import or_
from datetime import datetime
from flask_mail import Mail
import json
import os
import math
import socket
from uuid import uuid4

# Reading JSON file
with open('config.json', 'r') as c:
    params = json.load(c)["params"]

# app_configuration
local_server = True
app = Flask(__name__)
# Upload Location
basedir = os.path.abspath(os.path.dirname(__file__))
app.secret_key = "#kaushal"
# app configuration for mail system
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password']
)
mail = Mail(app)
# Image Configuration
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/img')
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)
# For Datavase Server
# Local and Production URI which is same for now
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']


db = SQLAlchemy(app)


# Class Section
# creating class for contact db
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(80), nullable=False)
    cemail = db.Column(db.String(20), nullable=False)
    csubject = db.Column(db.String(12), nullable=False)
    cmsg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
# creating class for Post db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    tagline = db.Column(db.String(120), nullable=False)
    content = db.Column(db.String, nullable=False)
    date = db.Column(db.String(12), nullable=True)
# creating class for feedback db


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(21), nullable=False)
    feedback = db.Column(db.String(120), nullable=False)
    img = db.Column(db.String(150), nullable=False, default='img.jpg')
    date = db.Column(db.String(12), nullable=True)
# creating class for product db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(12), nullable=False)
    price = db.Column(db.Integer,  nullable=False)
    description = db.Column(db.String, nullable=False)
    img = db.Column(db.String(255), nullable=False, default='product.jpg')
    slug = db.Column(db.String(42), nullable=False)
    date = db.Column(db.String(12), nullable=True)
# creating class for bookproduct db


class Bookproduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20),  nullable=False)
    address = db.Column(db.String(20),  nullable=False)
    brand = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(12), nullable=False)
    no_of_products = db.Column(db.Integer,  nullable=False)
    date = db.Column(db.String(12), nullable=True)


class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(20), nullable=False)
    no_of_mobiles = db.Column(db.Integer,  nullable=False)
    total_sales = db.Column(db.Integer,  nullable=False)
    date = db.Column(db.String(12), nullable=True)

# Routing Page
# dashboard


@app.route("/dashboard",  methods=['GET', 'POST'])
def dashboard():
    # if user is already logged in
    if('user' in session and session['user'] == params['admin_user']):
        flash(f'Welcome to Dashboard, Here you can manage all.', 'warning')
        posts = Post.query.filter_by().all()
        product = Product.query.filter_by().all()
        feedback = Feedback.query.filter_by().all()
        bookproduct = Bookproduct.query.filter_by().all()
        sales = Sales.query.filter_by().all()
        contacts = Contact.query.filter_by().all()
        return render_template('/dashboard/dashboard.html', params=params, product=product, feedback=feedback, bookproduct=bookproduct, sales=sales, contacts=contacts, posts=posts)
    # for login
    if(request.method == 'POST'):
        username = request.form.get('uname')
        password = request.form.get('pass')
        if(username == params['admin_user'] and password == params['admin_password']):
            # Setting Session Variable
            session['user'] = username
            flash(f'Your are  successfully Logged In', 'success')
            posts = Post.query.filter_by().all()
            product = Product.query.filter_by().all()
            feedback = Feedback.query.filter_by().all()
            bookproduct = Bookproduct.query.filter_by().all()
            sales = Sales.query.filter_by().all()
            contacts = Contact.query.filter_by().all()
            return render_template('/dashboard/dashboard.html', params=params, product=product, feedback=feedback, bookproduct=bookproduct, sales=sales, contacts=contacts, posts=posts)
    return render_template('signin.html', params=params)


# product_list
@app.route("/productlist")
def productlist():
    # displaying all products
    products = Product.query.filter_by().order_by(Product.id.desc()).all()
    last = math.ceil(len(products)/int((params['no_of_d'])))
    pageprodls = request.args.get('pageprodls')
    if(not str(pageprodls).isnumeric()):
        pageprodls = 1
    pageprodls = int(pageprodls)
    products = products[(pageprodls-1)*int((params['no_of_d'])):(pageprodls-1)
                        * int((params['no_of_d']))+int((params['no_of_d']))]
    # first_page
    if (pageprodls == 1):
        prevprodls = '#'
        nextprodls = "/productlist?pageprodls="+str(pageprodls + 1)
    # last_page
    elif (pageprodls == last):
        prevprodls = "/productlist?pageprodls="+str(pageprodls - 1)
        nextprodls = "#"
    # middle_page
    else:
        prevprodls = "/productlist?pageprodls="+str(pageprodls - 1)
        nextprodls = "/productlist?pageprodls="+str(pageprodls + 1)
    return render_template('productlist.html', params=params, products=products, nextprodls=nextprodls, prevprodls=prevprodls)

# main page


@app.route("/")
def home():
    # displaying products
    products = Product.query.filter_by().order_by(Product.id.desc()).all()
    # displaying post
    # its pagination
    # For pagination "page" is used
    posts = Post.query.filter_by().order_by(Post.id.desc()).all()
    # Pagination Logic
    last = math.ceil(len(posts)/int((params['no_of_posts'])))
    page = request.args.get('page')
    if(not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page-1)*int((params['no_of_posts'])):(page-1)
                  * int((params['no_of_posts']))+int((params['no_of_posts']))]
    # first_page
    if (page == 1):
        prevp = '#'
        nextp = "/?page="+str(page + 1)
    # last_page
    elif (page == last):
        prevp = "/?page="+str(page - 1)
        nextp = "#"
    # middle_page
    else:
        prevp = "/?page="+str(page - 1)
        nextp = "/?page="+str(page + 1)

    # displaying feedbacks and
    # its pagination
    # For pagination "pagef" is used
    feedbacks = Feedback.query.filter_by().order_by(Feedback.id.desc()).all()
    # Pagination Logic
    last = math.ceil(len(feedbacks)/int((params['no_of_posts'])))
    pagef = request.args.get('pagef')
    if(not str(pagef).isnumeric()):
        pagef = 1
    pagef = int(pagef)
    feedbacks = feedbacks[(pagef-1)*int((params['no_of_posts'])):(pagef-1)
                          * int((params['no_of_posts']))+int((params['no_of_posts']))]
    # first_page
    if (pagef == 1):
        prevf = '#'
        nextf = "/?pagef="+str(pagef + 1)
    elif (pagef == last):
        prevf = "/?pagef="+str(pagef - 1)
        nextf = "#"
    else:
        prevf = "/?pagef="+str(pagef - 1)
        nextf = "/?pagef="+str(pagef + 1)
    return render_template('index.html', params=params, posts=posts, feedbacks=feedbacks, prevp=prevp, nextp=nextp, prevf=prevf, nextf=nextf, products=products)

# viewing post details


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    # giving the result of first searched slug
    post = Post.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)

# about page


@app.route("/about")
def about():
    return render_template('about.html', params=params)

# contact page


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if(request.method == 'POST'):
        # Inserting Data into DB
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        msg = request.form.get('msg')
        entry = Contact(cname=name, cemail=email,
                        csubject=subject, cmsg=msg, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        flash(f'Your message was successfully Sent', 'success')
        # Flask-mail(Sending Mail)
        mail.send_message('New message from : ' + name ,
                          sender = email,
                          recipients=[params['gmail-user']],
                          body='Email : ' + email +"\n" + 'Subject : ' + subject + "\n" + 'Message : ' + msg
                          )
    return render_template('contact.html', params=params)

# Editing and ADDING POST


@app.route("/edit/<string:id>", methods=['GET', 'POST'])
def edit(id):
    # only if user is already logged in
    if('user' in session and session['user'] == params['admin_user']):
        if(request.method == 'POST'):
            title = request.form.get('title')
            tagline = request.form.get('tagline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            date = datetime.now()
            # to add post
            if id == '0':
                post = Post(title=title, tagline=tagline,
                            slug=slug, content=content, date=date)
                db.session.add(post)
                db.session.commit()
                flash(f'Your Post was successfully Posted', 'success')
                return redirect('/edit/' + id)
            # to edit post
            else:
                post = Post.query.filter_by(id=id).first()
                post.title = title
                post.tagline = tagline
                post.slug = slug
                post.content = content
                post.date = date
                db.session.commit()
                return redirect('/edit/' + id)
        # giving result of post according to id
        post = Post.query.filter_by(id=id).first()
        return render_template('/dashboard/edit.html', params=params, post=post, id=id)

# giving feedback


@app.route("/feedback", methods=['GET', 'POST'])
def feedback():
    if(request.method == 'POST'):
        # Fetching Data For DB
        name = request.form.get('name')
        email = request.form.get('email')
        msg = request.form.get('msg')
        img = photos.save(request.files.get('img'))
        feed = Feedback(name=name, email=email, feedback=msg,
                        img=img, date=datetime.now())
        db.session.add(feed)
        db.session.commit()
        flash(f'Your Feesback was successfully Sent', 'success')
    return render_template('index.html', params=params)

# logout


@app.route("/logout")
def logout():
    # Killing The Session
    session.pop('user')
    flash(f'Your are successfully Logged Out', 'success')
    return redirect('/dashboard')

# managing post under dashbaord


@app.route("/managepost",  methods=['GET', 'POST'])
def managepost():
    # if user is already logged in
    if('user' in session and session['user'] == params['admin_user']):
        posts = Post.query.filter_by().order_by(Post.id.desc()).all()
        # Pagination Logic
        last = math.ceil(len(posts)/int((params['no_of_posts'])))
        pagemng = request.args.get('pagemng')
        if(not str(pagemng).isnumeric()):
            pagemng = 1
        pagemng = int(pagemng)
        posts = posts[(pagemng-1)*int((params['no_of_posts'])):(pagemng-1)
                      * int((params['no_of_posts']))+int((params['no_of_posts']))]
        # first_page
        if (pagemng == 1):
            prevpmg = '#'
            nextpmg = "/managepost?pagemng="+str(pagemng + 1)
        # last_page
        elif (pagemng == last):
            prevpmg = "/managepost?pagemng="+str(pagemng - 1)
            nextpmg = "#"
        # middle_page
        else:
            prevpmg = "/managepost?pagemng="+str(pagemng - 1)
            nextpmg = "/managepost?pagemng="+str(pagemng + 1)
        return render_template('/dashboard/managepost.html', params=params, posts=posts, prevpmg=prevpmg, nextpmg=nextpmg)
    # for login
    if(request.method == 'POST'):
        username = request.form.get('uname')
        password = request.form.get('pass')
        if(username == params['admin_user'] and password == params['admin_password']):
            # Setting Session Variable
            session['user'] = username
            posts = Post.query.filter_by().order_by(Post.id.desc()).all()
            return render_template('/dashboard/managepost.html', params=params, posts=posts)
    return render_template('signin.html', params=params)

# managing feedback under dashbaord


@app.route("/managefeedback",  methods=['GET', 'POST'])
def managefeedback():
    # if user is already logged in
    if('user' in session and session['user'] == params['admin_user']):
        feedbacks = Feedback.query.filter_by().order_by(Feedback.id.desc()).all()
        last = math.ceil(len(feedbacks)/int((params['no_of_d'])))
        pagefeedmng = request.args.get('pagefeedmng')
        if(not str(pagefeedmng).isnumeric()):
            pagefeedmng = 1
        pagefeedmng = int(pagefeedmng)
        feedbacks = feedbacks[(pagefeedmng-1)*int((params['no_of_d'])):(pagefeedmng-1)
                              * int((params['no_of_d']))+int((params['no_of_d']))]
        # first_page
        if (pagefeedmng == 1):
            prevfeedmg = '#'
            nextfeedmg = "/managefeedback?pagefeedmng="+str(pagefeedmng + 1)
        # last_page
        elif (pagefeedmng == last):
            prevfeedmg = "/managefeedback?pagefeedmng="+str(pagefeedmng - 1)
            nextfeedmg = "#"
        # middle_page
        else:
            prevfeedmg = "/managefeedback?pagefeedmng="+str(pagefeedmng - 1)
            nextfeedmg = "/managefeedback?pagefeedmng="+str(pagefeedmng + 1)
        return render_template('/dashboard/mngfeedback.html', params=params, feedbacks=feedbacks, prevfeedmg=prevfeedmg, nextfeedmg=nextfeedmg)
    # for login
    if(request.method == 'POST'):
        username = request.form.get('uname')
        password = request.form.get('pass')
        if(username == params['admin_user'] and password == params['admin_password']):
            # Setting Session Variable
            session['user'] = username
            feedbacks = Feedback.query.filter_by().order_by(Feedback.id.desc()).all()
            return render_template('/dashboard/mngfeedback.html', params=params, feedbacks=feedbacks)
    return render_template('signin.html', params=params)

# delete post


@app.route("/delete/<string:id>", methods=['GET', 'POST'])
def delete(id):
    # only if user is already logged in
    if('user' in session and session['user'] == params['admin_user']):
        post = Post.query.filter_by(id=id).first()
        db.session.delete(post)
        db.session.commit()
        flash(f'Your post was successfully deleted', 'info')
    return redirect('/managepost')

# delete feedback


@app.route("/deletefeedback/<string:id>", methods=['GET', 'POST'])
def deletefeedback(id):
    # only if user is already logged in
    if('user' in session and session['user'] == params['admin_user']):
        feedback = Feedback.query.filter_by(id=id).first()
        db.session.delete(feedback)
        db.session.commit()
        flash(f'Your feedback was successfully Deleted', 'info')
    return redirect('/managefeedback')

# delete sales


@app.route("/deletesales/<string:id>", methods=['GET', 'POST'])
def deletesales(id):
    # only if user is already logged in
    if('user' in session and session['user'] == params['admin_user']):
        sales = Sales.query.filter_by(id=id).first()
        db.session.delete(sales)
        db.session.commit()
        flash(f'Your Sales Entry was successfully Deleted', 'info')
    return redirect('/managesales')

# delete feedback


@app.route("/deletebookproduct/<string:id>", methods=['GET', 'POST'])
def deletebookproduct(id):
    # only if user is already logged in
    if('user' in session and session['user'] == params['admin_user']):
        bookproduct = Bookproduct.query.filter_by(id=id).first()
        db.session.delete(bookproduct)
        db.session.commit()
        flash(f' Booked Product was successfully Deleted', 'info')
    return redirect('/bookedproduct')

# delete product


@app.route("/deleteproduct/<string:id>", methods=['GET', 'POST'])
def deleteproduct(id):
    # only if user is already logged in
    if('user' in session and session['user'] == params['admin_user']):
        product = Product.query.filter_by(id=id).first()
        db.session.delete(product)
        db.session.commit()
        flash(f' Your Product was successfully Deleted', 'info')
    return redirect('/manageproducts')

# delete contactlist


@app.route("/contactdelete/<string:id>", methods=['GET', 'POST'])
def contactdelete(id):
    # only if user is already logged in
    if('user' in session and session['user'] == params['admin_user']):
        contact = Contact.query.filter_by(id=id).first()
        db.session.delete(contact)
        db.session.commit()
        flash(f' Your Contact was successfully Deleted', 'info')
    return redirect('/managecontact')

# managing products under dashbaord


@app.route("/manageproducts",  methods=['GET', 'POST'])
def manageproducts():
    # if user is already logged in
    if('user' in session and session['user'] == params['admin_user']):
        products = Product.query.filter_by().order_by(Product.id.desc()).all()
        # Pagination Logic
        last = math.ceil(len(products)/int((params['no_of_d'])))
        pageprodmng = request.args.get('pageprodmng')
        if(not str(pageprodmng).isnumeric()):
            pageprodmng = 1
        pageprodmng = int(pageprodmng)
        products = products[(pageprodmng-1)*int((params['no_of_d'])):(pageprodmng-1)
                            * int((params['no_of_d']))+int((params['no_of_d']))]
        # first_page
        if (pageprodmng == 1):
            prevprodmg = '#'
            nextprodmg = "/manageproducts?pageprodmng="+str(pageprodmng + 1)
        # last_page
        elif (pageprodmng == last):
            prevprodmg = "/manageproducts?pageprodmng="+str(pageprodmng - 1)
            nextprodmg = "#"
        # middle_page
        else:
            prevprodmg = "/manageproducts?pageprodmng="+str(pageprodmng - 1)
            nextprodmg = "/manageproducts?pageprodmng="+str(pageprodmng + 1)
        return render_template('/dashboard/manageproducts.html', params=params, products=products, nextprodmg=nextprodmg, prevprodmg=prevprodmg)
    # for login
    if(request.method == 'POST'):
        username = request.form.get('uname')
        password = request.form.get('pass')
        if(username == params['admin_user'] and password == params['admin_password']):
            # Setting Session Variable.
            session['user'] = usernam
            products = Product.query.filter_by().order_by(Product.id.desc()).all()
            return render_template('/dashboard/manageproducts.html', params=params, products=products)
    return render_template('signin.html', params=params)

# edit and add product


@app.route("/editproduct/<string:id>", methods=['GET', 'POST'])
def editproduct(id):
    # only if user is already logged in
    if('user' in session and session['user'] == params['admin_user']):
        if(request.method == 'POST'):  # Inserting Data into DB.
            brand = request.form.get('brand')
            model = request.form.get('model')
            price = request.form.get('price')
            slug = request.form.get('slug')
            description = request.form.get('description')
            date = datetime.now()
            img = photos.save(request.files.get('img'))
            # to add product
            if id == '0':
                prod = Product(brand=brand, model=model, img=img, price=price,
                               slug=slug, description=description, date=date)
                db.session.add(prod)
                db.session.commit()
                flash(f' Your Product was successfully Added', 'success')
                return redirect('/editproduct/' + id)
            # to edit product
            else:
                product = Product.query.filter_by(id=id).first()
                product.brand = brand
                product.model = model
                product.img = img
                product.description = description
                product.slug = slug
                product.date = date
                db.session.commit()
                return redirect('/editproduct/' + id)
        # giving result of product according to id
        product = Product.query.filter_by(id=id).first()
        return render_template('/dashboard/addproduct.html', params=params, product=product, id=id)

# booking product


@app.route("/bookproduct", methods=['GET', 'POST'])
def bookproduct():
    if(request.method == 'POST'):
        # Inserting Data into DB
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        brand = request.form.get('brand')
        model = request.form.get('model')
        no_of_products = request.form.get('no_of_products')
        bookproduct = Bookproduct(name=name, email=email, phone=phone,
                                  address=address, brand=brand, model=model, date=datetime.now(), no_of_products=no_of_products)
        db.session.add(bookproduct)
        db.session.commit()
        # Flask-mail(Sending Mail)
        mail.send_message('New message from : ' + name ,
                          sender = email,
                          recipients=[params['gmail-user']],
                          body='Following Product is Booked.' + "\n" + 'Email : ' + email +"\n" + 'Phone Number : ' + phone + "\n" + 'Address : ' + address + "\n" + 'Brand : ' + brand + "\n" + 'Model : ' + model + "\n" + 'No of Products : ' + no_of_products
                          )
        flash(f'Your Product was successfully Booked', 'success')
    products = Product.query.filter_by().all()
    return render_template('bookproduct.html', params=params, products=products)

# viewing product


@app.route("/product/<string:product_slug>", methods=['GET'])
def product_route(product_slug):
    # giving the result of first searched produt
    product = Product.query.filter_by(slug=product_slug).first()
    description = product.description
    print(description)
    return render_template('productview.html', params=params, product=product, description=description)


@app.route("/productconf/<string:product_slug>", methods=['GET'])
def productconf(product_slug):
    # giving the result of first searched produt
    product = Product.query.filter_by(slug=product_slug).first()
    return render_template('/dashboard/prodconf.html', params=params, product=product)

# managing list of booked products under dashbaord


@app.route("/bookedproduct",  methods=['GET', 'POST'])
def bookedproduct():
    # if user is already logged in
    if('user' in session and session['user'] == params['admin_user']):
        bookproducts = Bookproduct.query.filter_by().order_by(Bookproduct.id.desc()).all()
        # Pagination Logic
        last = math.ceil(len(bookproducts)/int((params['no_of_d'])))
        pagebookprodmng = request.args.get('pagebookprodmng')
        if(not str(pagebookprodmng).isnumeric()):
            pagebookprodmng = 1
        pagebookprodmng = int(pagebookprodmng)
        bookproducts = bookproducts[(pagebookprodmng-1)*int((params['no_of_d'])):(pagebookprodmng-1)
                                    * int((params['no_of_d']))+int((params['no_of_d']))]
        # first_page
        if (pagebookprodmng == 1):
            prevbookprodmg = '#'
            nextbookprodmg = "/bookedproduct?pagebookprodmng=" + \
                str(pagebookprodmng + 1)
        # last_page
        elif (pagebookprodmng == last):
            prevbookprodmg = "/bookedproduct?pagebookprodmng=" + \
                str(pagebookprodmng - 1)
            nextbookprodmg = "#"
        # middle_page
        else:
            prevbookprodmg = "/bookedproduct?pagebookprodmng=" + \
                str(pagebookprodmng - 1)
            nextbookprodmg = "/bookedproduct?pagebookprodmng=" + \
                str(pagebookprodmng + 1)
        return render_template('/dashboard/bookedproductlist.html', params=params, bookproducts=bookproducts, prevbookprodmg=prevbookprodmg, nextbookprodmg=nextbookprodmg)
    # for login
    if(request.method == 'POST'):
        username = request.form.get('uname')
        password = request.form.get('pass')
        if(username == params['admin_user'] and password == params['admin_password']):
            # Setting Session Variable.
            session['user'] = username
            bookproducts = Bookproduct.query.filter_by().order_by(Bookproduct.id.desc()).all()
            return render_template('/dashboard/bookedproductlist.html', params=params, bookproducts=bookproducts)
    return render_template('signin.html', params=params)

# managing contactlist under dashbaord


@app.route("/managecontact", methods=['GET', 'POST'])
def managecontact():
    # if user is already logged in
    if('user' in session and session['user'] == params['admin_user']):
        contacts = Contact.query.order_by(Contact.id.desc()).all()
        last = math.ceil(len(contacts)/int((params['no_of_d'])))
        pagecontact = request.args.get('pagecontact')
        if(not str(pagecontact).isnumeric()):
            pagecontact = 1
        pagecontact = int(pagecontact)
        contacts = contacts[(pagecontact-1)*int((params['no_of_d'])):(pagecontact-1)
                            * int((params['no_of_d']))+int((params['no_of_d']))]
        # first_page
        if (pagecontact == 1):
            prevcontact = '#'
            nextcontact = "/managecontact?pagecontact="+str(pagecontact + 1)
        # last_page
        elif (pagecontact == last):
            prevcontact = "/managecontact?pagecontact="+str(pagecontact - 1)
            nextcontact = "#"
        # middle_page
        else:
            prevcontact = "/managecontact?pagecontact="+str(pagecontact - 1)
            nextcontact = "/managecontact?pagecontact="+str(pagecontact + 1)
        return render_template('/dashboard/contactlist.html', params=params, contacts=contacts, nextcontact=nextcontact, prevcontact=prevcontact)
    # for login
    if(request.method == 'POST'):
        username = request.form.get('uname')
        password = request.form.get('pass')
        if(username == params['admin_user'] and password == params['admin_password']):
            # Setting Session Variable.
            session['user'] = username
            contacts = Contact.query.filter_by().order_by(Contact.id.desc()).all()
            return render_template('/dashboard/contactlist.html', params=params, contacts=contacts)
    return render_template('signin.html', params=params)

# searchable contacts


@app.route("/searchcontact",  methods=['GET', 'POST'])
def searchcontact():
    if(request.method == 'POST'):
        searchcontact = request.form.get('searchcontact')
        search = "%{0}%".format(searchcontact)
        contacts = Contact.query.filter(or_(Contact.id.like(search),
                                            Contact.cname.like(search),
                                            Contact.cemail.like(search),
                                            Contact.csubject.like(search),
                                            Contact.cmsg.like(search),
                                            Contact.date.like(search))).all()
        return render_template('/dashboard/contactlist.html', params=params, contacts=contacts)
    else:
        render_template('/dashboard/contactlist.html', params=params)

# searchable products


@app.route("/searchproduct",  methods=['GET', 'POST'])
def searchproduct():
    if(request.method == 'POST'):
        searchproduct = request.form.get('searchproduct')
        search = "%{0}%".format(searchproduct)
        products = Product.query.filter(or_(Product.brand.like(search),
                                            Product.id.like(search),
                                            Product.model.like(search),
                                            Product.price.like(search),
                                            Product.description.like(search),
                                            Product.date.like(search))).all()
        return render_template('/dashboard/manageproducts.html', params=params, products=products)
    else:
        render_template('/dashboard/manageproducts.html', params=params)


@app.route("/searchproductlist",  methods=['GET', 'POST'])
def searchproductlist():
    if(request.method == 'POST'):
        searchproductlist = request.form.get('searchproductlist')
        search = "%{0}%".format(searchproductlist)
        products = Product.query.filter(or_(Product.brand.like(search),
                                            Product.model.like(search),
                                            Product.price.like(search),
                                            Product.description.like(search),
                                            Product.date.like(search))).all()
        return render_template('/productlist.html', params=params, products=products)
    else:
        render_template('/productlist.html', params=params)

# searchable sales


@app.route("/searchpost",  methods=['GET', 'POST'])
def searchpost():
    if(request.method == 'POST'):
        searchpost = request.form.get('searchpost')
        search = "%{0}%".format(searchpost)
        posts = Post.query.filter(or_(Post.id.like(search),
                                      Post.title.like(search),
                                      Post.tagline.like(search),
                                      Post.content.like(search),
                                      Post.date.like(search))).all()
        return render_template('/dashboard/managepost.html', params=params, posts=posts)
    else:
        render_template('/dashboard/managepost.html', params=params)

# searchable post


@app.route("/searchbookedproduct",  methods=['GET', 'POST'])
def searchbookedproduct():
    if(request.method == 'POST'):
        searchbookedproduct = request.form.get('searchbookedproduct')
        search = "%{0}%".format(searchbookedproduct)
        bookproducts = Bookproduct.query.filter(or_(Bookproduct.id.like(search),
                                                    Bookproduct.name.like(
                                                        search),
                                                    Bookproduct.email.like(
                                                        search),
                                                    Bookproduct.phone.like(
                                                        search),
                                                    Bookproduct.address.like(
                                                        search),
                                                    Bookproduct.brand.like(
                                                        search),
                                                    Bookproduct.model.like(
                                                        search),
                                                    Bookproduct.date.like(search))).all()
        return render_template('/dashboard/bookedproductlist.html', params=params, bookproducts=bookproducts)
    else:
        render_template('/dashboard/bookedproductlist.html', params=params)

# searchable post


@app.route("/searchfeedback",  methods=['GET', 'POST'])
def searchfeedback():
    if(request.method == 'POST'):
        searchfeedback = request.form.get('searchfeedback')
        search = "%{0}%".format(searchfeedback)
        feedbacks = Feedback.query.filter(or_(Feedback.id.like(search),
                                              Feedback.name.like(search),
                                              Feedback.email.like(search),
                                              Feedback.feedback.like(search),
                                              Feedback.date.like(search))).all()
        return render_template('/dashboard/mngfeedback.html', params=params, feedbacks=feedbacks)
    else:
        render_template('/dashboard/mngfeedback.html', params=params)

# searchable post


@app.route("/searchsales",  methods=['GET', 'POST'])
def searchsales():
    if(request.method == 'POST'):
        searchsales = request.form.get('searchsales')
        search = "%{0}%".format(searchsales)
        sales = Sales.query.filter(or_(Sales.id.like(search),
                                       Sales.brand.like(search),
                                       Sales.no_of_mobiles.like(search),
                                       Sales.total_sales.like(search),
                                       Sales.date.like(search))).all()
        return render_template('/dashboard/saleslist.html', params=params, sales=sales)
    else:
        render_template('/dashboard/saleslist.html', params=params)

# edit and add product


@app.route("/editsales/<string:id>", methods=['GET', 'POST'])
def editsales(id):
    # only if user is already logged in
    if('user' in session and session['user'] == params['admin_user']):

        if(request.method == 'POST'):  # Inserting Data into DB.
            brand = request.form.get('brand')
            no_of_mobiles = request.form.get('no_of_mobiles')
            total_sales = request.form.get('total_sales')
            date = datetime.now()
            # to add sales
            if id == '0':
                sales = Sales(brand=brand, no_of_mobiles=no_of_mobiles,
                              total_sales=total_sales, date=date)
                db.session.add(sales)
                db.session.commit()
                flash(f' Your Sales Entry was successfully Added', 'success')
                return redirect('/editsales/' + id)
            # to edit product
            else:
                sales = Sales.query.filter_by(id=id).first()
                sales.brand = brand
                sales.no_of_mobiles = no_of_mobiles
                sales.total_sales = total_sales
                sales.date = date
                db.session.commit()
                flash(f' Your Sales Entry was successfully Edited', 'success')
                return redirect('/editsales/' + id)
        # giving result of product according to id
        sales = Sales.query.filter_by(id=id).first()
        products = Product.query.filter_by().all()
        return render_template('/dashboard/addsales.html', params=params, sales=sales, id=id, products=products)


@app.route("/managesales", methods=['GET', 'POST'])
def managesales():
    # if user is already logged in
    if('user' in session and session['user'] == params['admin_user']):
        sales = Sales.query.filter_by().order_by(Sales.id.desc()).all()
        last = math.ceil(len(sales)/int((params['no_of_d'])))
        pagesales = request.args.get('pagesales')
        if(not str(pagesales).isnumeric()):
            pagesales = 1
        pagesales = int(pagesales)
        sales = sales[(pagesales-1)*int((params['no_of_d'])):(pagesales-1)
                      * int((params['no_of_d']))+int((params['no_of_d']))]
        # first_page
        if (pagesales == 1):
            prevsales = '#'
            nextsales = "/managesales?pagesales="+str(pagesales + 1)
        # last_page
        elif (pagesales == last):
            prevsales = "/managesales?pagesales="+str(pagesales - 1)
            nextsales = "#"
        # middle_page
        else:
            prevsales = "/managesales?pagesales="+str(pagesales - 1)
            nextsales = "/managesales?pagesales="+str(pagesales + 1)
        return render_template('/dashboard/saleslist.html', params=params, sales=sales, nextsales=nextsales, prevsales=prevsales)
    # for login
    if(request.method == 'POST'):
        username = request.form.get('uname')
        password = request.form.get('pass')
        if(username == params['admin_user'] and password == params['admin_password']):
            # Setting Session Variable.
            session['user'] = username
            sales = Sales.query.filter_by().order_by(Sales.id.desc()).all()
            return render_template('/dashboard/saleslist.html', params=params, sales=sales)
    return render_template('signin.html', params=params)


if __name__ == '__main__':
    app.debug = False
    app.run()
