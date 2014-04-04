from urlshort import app
from urlshort import db
from urlshort import util
import flask

@app.route('/', methods=['GET','POST'])
def urlshort_index():
    if flask.request.method == 'POST':
        form = flask.request.form
        if 'url' not in form:
            flask.flash('no url provided')
        else:
            url = form['url']
            if util.url_is_valid(url):
                with db.open() as session:
                    u = session.get_url(url)
                    if u is None:
                        u = db.URL()
                        u.url = url
                        u.name = util.random_string(8)
                        session.add(u)
                        session.commit()
                    return flask.render_template('short.html', name=u.name)
            else:
                flask.flash('url invalid')
    return flask.render_template('index.html')


@app.route('/<string:name>')
def urlshort_get_by_name(name):
    with db.open() as session:
        url = session.get_url_for_name(name)
        if url is None:
            flask.abort(404)
        else:
            return flask.redirect(url.url)
