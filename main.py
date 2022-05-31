# import website package, grab teh funciton and run
from website import create_app

app = create_app()


if __name__ == '__main__':
    # only if we run this file, not if we import this file, are we going to execute teh line
    # if you were to import main.py from another file and you didn't have line 7, it will run the web server. 
    # but you only want to run the web server if you only run this file directly.
   
    # start a web server
    app.run(debug=True) 
    # debug is true means every time we make a change to our python code, it will automatically rerun the web server
    # you will want to turn it off when you run in production
# import sys
# print(sys.path)