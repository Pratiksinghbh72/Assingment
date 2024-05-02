Sure, here's how you can create a README file to document your GraphQL API project:

```markdown
# GraphQL API using Python and Flask

This project demonstrates how to set up a GraphQL API using Python and Flask. It includes instructions for setting up the environment, installing dependencies, creating a schema, setting up the Flask app, running the server locally, and deploying the API to Heroku.

## Table of Contents

- [Set Up Environment](#set-up-environment)
- [Install Dependencies](#install-dependencies)
- [Create a Schema](#create-a-schema)
- [Create the Flask App](#create-the-flask-app)
- [Run the Server](#run-the-server)
- [Deploy to Heroku](#deploy-to-heroku)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Set Up Environment

1. Make sure you have Python installed on your system.
2. Create a new directory for your project.
3. Inside that directory, create a virtual environment:
    ```
    python3 -m venv venv
    ```
4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

## Install Dependencies

Install Flask and Graphene using pip:

```bash
pip install flask graphene
```

## Create a Schema

Create a file named `schema.py` and define your GraphQL schema there. Example schema is provided in the project.

## Create the Flask App

Create a file named `app.py` and define your Flask application there. Example Flask app setup is provided in the project.

## Run the Server

Run your Flask app:

```bash
python app.py
```

Your GraphQL API server should be running locally at `http://localhost:5000/gql`. You can visit this URL in your browser to access the GraphiQL interface and execute queries.

## Deploy to Heroku

To deploy your GraphQL API to Heroku, follow these steps:

1. Make sure you have the Heroku CLI installed and logged in.
2. Create a `requirements.txt` file containing the dependencies (`flask`, `graphene`).
3. Create a `Procfile` with the following content:
    ```
    web: python app.py
    ```
4. Initialize a git repository, commit your files, and push to Heroku:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    heroku create
    git push heroku master
    ```
5. Your app should be deployed to Heroku now.

## Testing

You can add unit tests using libraries like `pytest`. Ensure you have separate tests for your resolver functions in `schema.py`. You can also write integration tests to test the GraphQL endpoint using libraries like `requests`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

You can copy this markdown content into a file named `README.md` in your project directory. Make sure to replace placeholders with actual content and modify it according to your project structure and requirements.
