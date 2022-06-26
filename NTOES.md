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

5.  [The application will use a SQLite database to store users and posts.](https://flask.palletsprojects.com/en/2.1.x/tutorial/database/)

    SQLite is convenient because it doesn’t require setting up a separate database server and is built-in to Python.

    However, if concurrent requests try to write to the database at the same time, they will slow down as each write happens sequentially.

        Small applications won’t notice this. Once you become big, you may want to switch to a different database.

6.  [venv](https://python.land/virtual-environments/virtualenv)有新的 dependencies 以及对本地 denpendency 的路径（OS 依赖）。

    [cloud storage ](https://stackoverflow.com/questions/45082883/python-virtualenv-cant-work-through-onedrive) of venv can't be shared due to invalid link in the venv.

    need to rebuild venv.

7.  The url_for() function generates the URL to a view based on a name and arguments. The name associated with a view is also called the endpoint, and by default it’s the same as the name of the view function.

8.  [How to implent a flask app.](https://flask.palletsprojects.com/en/2.1.x/quickstart/#a-minimal-application)

    run an app using a development server.

        $env:FLASK_APP = appname
        $env:FLASK_ENV = "development"
        flask run

9.  Jinga

    The Flask web application framework, also maintained by Pallets, uses Jinja templates by default. Flask sets up a Jinja environment and template loader for you, and provides functions to easily render templates from view functions.

10. globals

    Bootstrap employs a handful of important global styles and settings that you’ll need to be aware of when using it, all of which are almost exclusively geared towards the normalization of cross browser styles.

- Bootstrap requires the use of the HTML5 doctype. Without it, you’ll see some funky incomplete styling, but including it shouldn’t cause any considerable hiccups.

        <!doctype html>
        <html lang="en">
        ...
        </html>

- Bootstrap is developed mobile first, a strategy in which we optimize code for mobile devices first and then scale up components as necessary using CSS media queries. To ensure proper rendering and touch zooming for all devices, add the responsive viewport meta tag to your <head>.

        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

- For more straightforward sizing in CSS, we switch the global box-sizing value from content-box to border-box. This ensures padding does not affect the final computed width of an element, but it can cause problems with some third party software like Google Maps and Google Custom Search Engine.

  On the rare occasion you need to override it, use something like the following:

        .selector-for-some-widget {
        box-sizing: content-box;
        }

- For improved cross-browser rendering, we use **Reboot** to correct inconsistencies across browsers and devices while providing slightly more opinionated resets to common HTML elements.

11. [The Rules of the Grid:](http://bootstrap.themes.guide/how-to-use-bootstrap-grid.html)

    1. Columns must be the immediate child of a Row.

    2. Rows are only used to contain Columns, nothing else. The sole purpose of the "row" is to contain 1 or more "columns".

    3. Rows should be placed inside a Container.

    The Container can be used to hold any elements and content. It’s not only used for the Grid Rows & Columns.

    At first, the Container may seem trivial or unnecessary, but it’s very important to control width of the layout. The Container is also used to evenly align the left and right edges of the layout within the browser’s viewport.

    Rows have a negative left/right margin of -15px. The Container padding of 15px is used to counteract the negative margins of the Row. This is to keep content evenly aligned on the edges of the layout. If you don’t put a Row in a Container, the Row will overflow it’s container, causing an undesirable horizontal scroll.

    Bootstrap 4 has 2 types of Containers. In my examples I used .container, but there is also the full-width .container-fluid.

        Fixed-width container to center your layout in the middle:

        Full-width container for a layout the spans the entire width:

12. bootstrap class: a specific set of syles

13. [frameword](https://getbootstrap.com/docs/5.1/getting-started/introduction/)

14. [Jinja if else](https://www.codegrepper.com/code-examples/whatever/jinja+if+else)

15. conditionally display elements in html

    x <div class="form-floating" data-show-if="frequency='2'">

16. Set a <div> element to not be displayed:

    document.getElementById("myDIV").style.display = "none";
    The display property sets or returns the element's display type.

    Elements in HTML are mostly "inline" or "block" elements: An inline element has floating content on its left and right side. A block element fills the entire line, and nothing can be displayed on its left or right side.

    The display property also allows the author to show or hide an element. It is similar to the visibility property. However, if you set display:none, it hides the entire element, while visibility:hidden means that the contents of the element will be invisible, but the element stays in its original position and size.

    Tip: If an element is a block element, its display type can also be changed with the float property.

17. 填充提交
    
    element.sendKeys("your text");
    element.submit();

     textField.sendKeys("text you type into field" + "\n").

    elem.send_keys(Keys.ARROW_DOWN)
    elem.send_keys(Keys.RETURN)

18. [Heroku 部署](https://evancalz.medium.com/deploying-your-flask-app-to-heroku-43660a761f1c)
    
19. [Heroku deploy](https://medium.com/daily-programming-tips/deploy-a-flask-app-with-a-sqlite-database-on-heroku-22b5402c5c6)

    pip freeze > requirements. txt