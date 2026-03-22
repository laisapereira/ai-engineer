import sqlite3
import sys
from embeddings import generate_embedding
from vector_store import add_embedding_to_index

conn = sqlite3.connect('crm.db')


def init_db():
    create_users_table("user_database.db")


def create_users_table(database_file):
    """
    Creates a 'users' table in the specified SQLite database file.
    """

    try:
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS User (
            id_user INTEGER PRIMARY KEY AUTOINCREMENT,
            nm_usuario VARCHAR(255) NOT NULL,
            email_usuario VARCHAR(255) NOT NULL,
            ds_usuario VARCHAR(255),
            cd_embedding INTEGER
        )
        """

        cursor.execute(create_table_query)
        print("Table 'User' created successfully.", file=sys.stderr)

        conn.commit()
        cursor.close()

    except sqlite3.Error as e:
        print(f"An error occurred: {e}", file=sys.stderr)
    finally:

        if conn:
            conn.close()


create_users_table("user_database.db")


def insert_user(name, email, description):

    try:
        with sqlite3.connect("user_database.db") as connection:
            cursor = connection.cursor()

            check_existing_user = "SELECT id_user FROM User WHERE email_usuario = ?"
            cursor.execute(check_existing_user, (email,))
            existing_user = cursor.fetchone()

            if existing_user:
                print(
                    f"User with email '{email}' already exists.", file=sys.stderr)
                raise ValueError(f"User with email '{email}' already exists.")

            insert_query = "INSERT INTO USER (nm_usuario, email_usuario, ds_usuario) VALUES (?, ?, ?)"

            cursor.execute(insert_query, (name, email, description))
            connection.commit()

            print(f"User '{name}' inserted successfully!", file=sys.stderr)

            userId = cursor.lastrowid

            embedding = generate_embedding(description)
            faiss_index_id = add_embedding_to_index(embedding)

            print(
                f"Generated embedding for user '{name}' with ID {userId} and FAISS index ID {faiss_index_id}", file=sys.stderr)

            update_query = "UPDATE User SET cd_embedding = ? WHERE id_user = ?"
            cursor.execute(update_query, (faiss_index_id, userId))
            connection.commit()

            print(
                f"Updated user '{name}', ID {userId}, with FAISS index ID {faiss_index_id}", file=sys.stderr)

            return userId

    except sqlite3.Error as e:
        print(f"An error occurred: {e}", file=sys.stderr)
