from Database.database import Database

class PublicacionModel:
    def __init__(self):
        self.db = Database()

    def crear_publicacion(self, usuario_email, contenido, imagen_url=None):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO publicaciones (usuario_email, contenido, imagen_url) VALUES (%s, %s, %s)",
                (usuario_email, contenido, imagen_url)
            )
            conn.commit()
            return True, cursor.lastrowid
        except Exception as e:
            print(f"Error: {e}")
            return False, None
        finally:
            conn.close()

    def obtener_publicaciones(self):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.*, u.nombre, u.foto 
            FROM publicaciones p 
            JOIN usuario u ON p.usuario_email = u.email 
            ORDER BY p.fecha_creacion DESC
        """)
        publicaciones = cursor.fetchall()
        conn.close()
        return publicaciones

    def obtener_publicacion_por_id(self, pub_id):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.*, u.nombre, u.foto 
            FROM publicaciones p 
            JOIN usuario u ON p.usuario_email = u.email 
            WHERE p.id = %s
        """, (pub_id,))
        pub = cursor.fetchone()
        conn.close()
        return pub

    def agregar_comentario(self, pub_id, usuario_email, comentario):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO comentarios (publicacion_id, usuario_email, comentario) VALUES (%s, %s, %s)",
                (pub_id, usuario_email, comentario)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    def obtener_comentarios(self, pub_id):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT c.*, u.nombre, u.foto 
            FROM comentarios c 
            JOIN usuario u ON c.usuario_email = u.email 
            WHERE c.publicacion_id = %s 
            ORDER BY c.fecha_creacion ASC
        """, (pub_id,))
        comentarios = cursor.fetchall()
        conn.close()
        return comentarios

    def obtener_publicaciones_usuario(self, usuario_email):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.*, u.nombre, u.foto 
            FROM publicaciones p 
            JOIN usuario u ON p.usuario_email = u.email 
            WHERE p.usuario_email = %s
            ORDER BY p.fecha_creacion DESC
        """, (usuario_email,))
        publicaciones = cursor.fetchall()
        conn.close()
        return publicaciones

    def actualizar_publicacion(self, pub_id, contenido, imagen_url):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE publicaciones SET contenido=%s, imagen_url=%s WHERE id=%s",
                (contenido, imagen_url, pub_id)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    def eliminar_publicacion(self, pub_id):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM publicaciones WHERE id=%s", (pub_id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
