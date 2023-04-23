from flask import render_template, redirect, Blueprint

blueprint = Blueprint('simple_pages', __name__)


@blueprint.route('/')
@blueprint.route('/index')
def index():
    return render_template('index.html')
