from CTFd.utils.plugins import override_template
import os

def load(app):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(dir_path, 'new-challenge.html')
    override_template('challenge.html', open(template_path).read())