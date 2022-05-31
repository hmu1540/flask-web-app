1.  build the directories

2.  install packages

        pip install flask
        flask-login
        flask-sqlalchemy: wrapper for SQL, create models. delete models, add models

3.  static folder: store static files (don't change), like images, JS files, CSS files, and then load them into html by writing
    <script 
        type ="text/javascript"
        src = "{{ url_for('static', filename = 'index.js)}}"
        ></script>

        url_for: python function, load the URL for the static folder(find static on our website)
        {{}}: JINGA, means we are going to write a python expresion

4.  [virtualenv VS docker](https://stackoverflow.com/questions/50974960/whats-the-difference-between-docker-and-python-virtualenv#:~:text=A%20virtualenv%20only,with%20Docker%20installed.)

    A virtualenv only encapsulates Python dependencies. A Docker container encapsulates an entire OS.

    With a Python virtualenv, you can easily switch between Python versions and dependencies, but you're stuck with your host OS.

    With a Docker image, you can swap out the entire OS - install and run Python on Ubuntu, Debian, Alpine, even Windows Server Core.

    There are Docker images out there with every combination of OS and Python versions you can think of, ready to pull down and use on any system with Docker installed.
