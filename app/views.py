from flask import render_template
from app import app
from .request import get_source,article_source, get_category
from flask import render_template,request,redirect,url_for
#our views
@app.route('/')
def index():
    '''
    Root function returning home page with data
    '''
    source= get_source()
    print(source)
    return render_template('index.html',sources=source)

@app.route('/article/<id>')
def article(source_id):
    '''
    view article page function that returns article details page and its data
    '''
    # title= 'Articles'
    articles = article_source(id)
    return render_template('article.html',articles= articles,id=id)


@app.route('/categories/<cat_name>')
def category(cat_name):

    '''
    function to return the category.html page and its content
    '''
    category = get_category(cat_name)
    # print (category)
    title = f'{cat_name}'
    m=cat_name
    # source = get_categories()
    return render_template('category.html',title = title,m=m, category=category)








