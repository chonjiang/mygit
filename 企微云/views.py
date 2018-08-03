from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)
app.config['DEBUG'] = True
manager = Manager(app)

#
# @app.route('/')
# def get_base():
#     return render_template('base.html')


@app.route('/test/')
def get_test():
    return render_template('test.html')


@app.route('/test2/')
def get_test2():
    return render_template('test2.html')


@app.route('/publish/')
def get_publish():
    return render_template('publish.html')


@manager.command
def dev():
    """开发者用于实时监控代码，在网页端同步更新，提高开发效率"""
    from livereload import Server  # 导入监控包
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')  # 可用正则表达式，此处用于监测整个项目文件，
    live_server.serve(open_url=True)  # True表示自己打开浏览器


if __name__ == '__main__':
    manager.run()
