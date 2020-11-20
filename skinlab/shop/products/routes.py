from flask import redirect, render_template, url_for, flash, request, session
from shop import db, app, photos
from .models import Brand, Category, Addskin
from .forms import AddSkin
import secrets


@app.route('/addcollection', methods=['GET','POST'])
def addcollection():
    if 'email' not in session:
        print("esta el email")
        flash(f'Iniciar Sesion antes', 'danger')
        return redirect(url_for('login'))
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name= getbrand)
        db.session.add(brand)
        flash(f'The brand {getbrand} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addcollection'))
    return render_template('products/addcollection.html', brands='brands')

@app.route('/updatecollection/<int:id>', methods=['GET','POST'])
def updatecollection(id):
    if 'email' not in session:
        print("esta el email")
        flash(f'Iniciar Sesion antes', 'danger')
        return redirect(url_for('login'))
    updatecollection = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method == 'POST':
        updatecollection.name = brand
        flash(f'La coleccion fue actualizada', 'success')
        db.session.commit()
        return redirect(url_for('collections'))
    return render_template('products/updatecollection.html', title='Update collection', updatecollection=updatecollection)


@app.route('/updatecategory/<int:id>', methods=['GET','POST'])
def updatecategory(id):
    if 'email' not in session:
        print("esta el email")
        flash(f'Iniciar Sesion antes', 'danger')
        return redirect(url_for('login'))
    updatecategory = Category.query.get_or_404(id)
    category = request.form.get('category')
    if request.method == 'POST':
        updatecategory.name = category
        flash(f'La categoria de armas fue actualizada', 'success')
        db.session.commit()
        return redirect(url_for('categories'))
    return render_template('products/updatecollection.html', title='Update category', updatecategory=updatecategory)


@app.route('/addcat', methods=['GET','POST'])
def addcat():
    if 'email' not in session:
        print("esta el email")
        flash(f'Iniciar Sesion antes', 'danger')
        return redirect(url_for('login'))
    if request.method == "POST":
        getcat = request.form.get('category')
        cat = Category (name = getcat)
        db.session.add(cat)
        flash(f'The category {getcat} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addcat'))


    return render_template('products/addbrand.html')


@app.route('/addskin', methods=['POST', 'GET'])
def addskin():
    if 'email' not in session:
        print("esta el email")
        flash(f'Iniciar Sesion antes', 'danger')
        return redirect(url_for('login'))
    brands = Brand.query.all()
    categories = Category.query.all()
    form = AddSkin(request.form)
    if request.method == "POST":
        name = form.name.data
        price = form.price.data
        float = form.float.data
        stock = form.stock.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        image = photos.save(request.files.get('image'), name=secrets.token_hex(10) + ".")
        addskin = Addskin(name=name, price=price, float=float, stock=stock, brand_id=brand, category_id=category, image=image)
        db.session.add(addskin)
        flash(f'La skin fue cargada con exito')
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('products/addskin.html', title='Agregar Skin a la venta', form=form, brands=brands, categories=categories)


@app.route('/updateskin/<int:id>', methods=["GET","POST"])
def updateskin(id):

    collection = Brand.query.all()
    categories = Category.query.all()
    skin = Addskin.query.get_or_404(id)
    collection = request.form.get('collection')
    category = request.form.get('category')
    form = AddSkin(request.form)
    if request.method == 'POST':     
        skin.name = form.name.data
        skin.price = form.price.data
        skin.float = form.float.data
        skin.stock = form.stock.data
        db.session.commit()
        flash(f'Skin actualizada')
        return redirect(url_for('admin'))

    form.name.data = skin.name
    form.price.data = skin.price
    form.float.data = skin.float
    form.stock.data = skin.stock

    return render_template('products/updateskin.html', form=form, collection=collection, categories=categories, skin=skin)