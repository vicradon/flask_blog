# Flask Blog App

This is a demo blog built using Flask for demo purposes only.

## Setting up the app

You need to provision a PostgreSQL database to get the app running. Create a postgresql database called `flask_blog_db` and then set the username, password, hostname in the connection string below:

```
DATABASE_URL="postgresql://username:password@hostname/flask_blog_db"
```

With the correct connection string constructed, create a `.env` file from the `.env.example` file and set the value of `DATABASE_URL` to the connection string.

### Installing dependencies

You can install all the required dependencies after you create your virtual environment. Use the command below to create the virtual environment and activate it.

```sh
python3 -m venv .venv && source .venv/bin/activate
```

> N/B: The command above assumes you are using a UNIX shell. If you're using a windows shell, source the virtual environment using `.venv/Scripts/activate`.

### Seeding the database

You can seed the database you created using the `misc/seed.py` script. Simply run the script using the command below:

```sh
python misc/seed.py
```

Ensure you are in a terminal with the virtual environment active before you run the script.

## Running the app

You can run the app using the command `python app.py`. This command will start the flask local development server on port 5000.
