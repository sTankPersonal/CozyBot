from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

from Config.Settings import DB_CONNECTION_STRING

# Import Base and your models so metadata is populated
from Domain.Entities.AbstractBase import Base
import Domain.Entities  # important: registers Message, EmbedField, Server, etc.

# Alembic Config object
config = context.config

# Override sqlalchemy.url in alembic.ini with .env setting
if DB_CONNECTION_STRING:
    config.set_main_option("sqlalchemy.url", DB_CONNECTION_STRING)

# Logging setup
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Tell Alembic which metadata to compare
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
