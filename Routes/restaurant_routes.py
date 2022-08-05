"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime
from Connection import Connection


@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/locator')
@view('locator')
def locator():
    """Renders the locator page."""
    return dict(
        title='Restaurant Locator',
        message='Enter a zip code to search nearby Restaurants.',
        year=datetime.now().year
    )
