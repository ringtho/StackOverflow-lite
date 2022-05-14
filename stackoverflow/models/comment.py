from ..init_db import get_db_connection
from psycopg2.extras import RealDictCursor

class Comment:

    def create_comment(self,answer_id,comment,author):
        conn = get_db_connection()
        cur = conn.cursor()
        query = f"""
        INSERT INTO comments (answer_id, comment, author) 
        VALUES ('{answer_id}','{comment}','{author}')
        """
        comment = cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
        return comment

    def get_comments_by_answer_id(self,answer_id):
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        query = f"""
        SELECT * FROM comments WHERE answer_id='{answer_id}'
        """
        cur.execute(query)
        comments = cur.fetchall()
        cur.close()
        conn.close()
        return comments

    def get_single_comment_by_id(self, comment_id):
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        query = f"""
        SELECT * FROM comments WHERE id='{comment_id}'
        """
        cur.execute(query)
        comment = cur.fetchall()
        cur.close()
        conn.close()
        return comment
    
    def delete_comment(self, comment_id, author):
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        query = f"""
        DELETE FROM comments WHERE id='{comment_id}'
        AND author='{author}'
        """
        cur.execute(query)
        rows = cur.rowcount
        conn.commit()
        cur.close()
        conn.close()
        return rows