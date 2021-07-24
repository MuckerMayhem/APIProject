
### Prerequisites

TBD

### Installing

Make sure your local PostgreSQL server is running on `http://localhost:5432`. Then, create a new database called `fastapi_db`.

Now, run the `prestart.sh` script that'll create the tables and add initial data.
```shell script
./prestart.sh
```

### Running

After all the above mentioned steps, you can start the application using the following command:
```shell script
python -m app.main
```
The application will be available at https://localhost:8000.

## Development

These instructions will provide you some useful information on developing this application.

### Migrations

If there are any changes to the SQLAlchemy ORM models, you can run the following command to generate `alembic` migrations.
```shell script
alembic revision --autogenerate -m "<migration message>"
```
This command will generate a new migration file in the `migrations` directory. Remember to check the generated migration file before committing.

## Testing

The application unit tests are inside the `app/tests` module.

Run the following command in the terminal to execute the application unit tests.
```shell script
pytest app/tests
```

## Deployment

The application can be deployed in production using `gunicorn`, you don't need to make any code changes for the same.
Head over to the [Uvicorn Deployment](https://www.uvicorn.org/deployment/) documentation for complete instructions.

