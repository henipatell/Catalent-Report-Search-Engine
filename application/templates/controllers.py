import sqlite3
from app import app


# def insert_pdf_to_db(pdf_name):
#     # insert a pdf into the database and return its id
#     path = app.config['PDF_DIR_LOC'] + app.config['PDF_DIR'] + pdf_name
#     conn = conn_to_db('report_pdf.db')
#     cursor = conn.execute("INSERT INTO PDF (NAME, HASH, DATE) VALUES ('{}', '{}', {})".format(
#                                             pdf_name, hash_file(path), int(time())))
#     conn.commit()
#     pdf_id = cursor.lastrowid
#     conn.close()
#     return pdf_id

# def insert_word_to_db(pdf_id, word, freq):
#     conn = conn_to_db('pdf.db')
#     conn.execute("INSERT INTO FREQ (PDF_ID, WORD, W_FREQ) VALUES ({}, '{}', {})".format(
#                                     pdf_id, word, str(freq)))
#     conn.commit()
#     conn.close()

# def get_results(words, page=0, nb_max_by_pages=8, nb_min_pdfs=8):
#     return True


