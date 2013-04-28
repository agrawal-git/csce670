## Search 'em all

Code repo for the CSCE 670 (Information retrieval) final project.

### Demo
The app is now **deployed** on Heroku: [http://searchem.herokuapp.com](http://searchem.herokuapp.com).

### Running [UPDATED]:

To run the flask app locally:

- Install all dependencies via "pip install -r requirements.txt"
- You need PostgreSql on your system. Refer to [Heroku docs](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup) for platform-specific installation instructions.
- Don't forget to create a database called **searchem** on your machine for the app to work properly. Refer to PostgreSql documentation on how to do that.
- Run "python searchem.py" in the terminal.
- Go to "localhost:5000" in your browser.
- Profit!


### Adding code
To add code, make sure you create a new file, add functionality in it, and import it in the index.py file. Keep your code modular and object oriented please! 

For instance, to add search functionality, you might want to add a search.py file, which contains a Search class that contains all the functionality of search. To perform a search, you do an "import Search from search" and access all the methods you want to access.

### Authors
- Wael Al-Sallami
- Ashish Agrawal
- Hong-hoe Kim
