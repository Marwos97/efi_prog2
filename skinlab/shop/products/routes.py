from flask import redirect, render_template, url_for, flash, request
from shop import db, app, photos
from .models import Brand, Category, Addskin
from .forms import AddSkin
import secrets


@app.route('/addbrand', methods=['GET','POST'])
def addbrand():
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name = getbrand)
        db.session.add(brand)
        flash(f'The brand {getbrand} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addbrand'))


    return render_template('products/addbrand.html', brands='brands')

@app.route('/addcat', methods=['GET','POST'])
def addcat():
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