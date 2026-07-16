import mysql.connector

# =====================================
# DATABASE CONNECTION
# =====================================

def connect_db():

    try:

        connection = mysql.connector.connect(

            host="localhost",

            user="root",

            password=".#RamJi.",

            database="skillswap",

            port=5918

        )

        return connection

    except mysql.connector.Error as err:

        print("Database Connection Error:", err)

        return None


# =====================================
# INSERT USER
# =====================================

def insert_user(
    full_name,
    username,
    email,
    password,
    location,
    skills_offer,
    skills_learn
):

    conn = connect_db()

    if conn is None:
        return False, "Database connection failed."

    try:

        cursor = conn.cursor()

        query = """
        INSERT INTO users
        (full_name, username, email, password,
        location, skills_offer, skills_learn)

        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            full_name,
            username,
            email,
            password,
            location,
            skills_offer,
            skills_learn
        )

        cursor.execute(query, values)

        conn.commit()

        return True, "Registration Successful!"

    except mysql.connector.IntegrityError as err:

        if "username" in str(err).lower():
            return False, "Username already exists."

        elif "email" in str(err).lower():
            return False, "Email already exists."

        else:
            return False, str(err)

    except Exception as err:

        return False, str(err)

    finally:

        if conn and conn.is_connected():
            cursor.close()
            conn.close()
# =====================================
# LOGIN USER
# =====================================

def login_user(email, password):

    conn = connect_db()

    if conn is None:
        return False, None

    try:

        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT *
        FROM users
        WHERE email=%s
        AND password=%s
        """

        cursor.execute(query, (email, password))

        user = cursor.fetchone()

        if user:

            return True, user

        else:

            return False, None

    except Exception as err:

        print(err)

        return False, None

    finally:

        if conn.is_connected():

            cursor.close()

            conn.close()