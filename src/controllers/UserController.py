import re
import random
import smtplib
import os
import base64
import bcrypt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from dotenv import load_dotenv
from models.UserModel import UsuarioModel

_search_dirs = [
    os.path.dirname(__file__),
    os.path.join(os.path.dirname(__file__), ".."),
    os.path.join(os.path.dirname(__file__), "..", ".."),
    os.path.join(os.path.dirname(__file__), "..", "..", "base"),
]
for _d in _search_dirs:
    _env = os.path.join(os.path.abspath(_d), ".env")
    if os.path.exists(_env):
        load_dotenv(_env)
        break

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()
        self._codigos = {}

    def login(self, email, password):
        if not email or not password:
            return None, "Completa todos los campos."
        user = self.model.buscar_por_email(email)
        if user and bcrypt.checkpw(password.encode(), user["password"].encode()):
            return user, "OK"
        return None, "Correo o contraseña incorrectos."

    def registrar(self, nombre, email, password):
        if not nombre or not email or not password:
            return False, "Completa todos los campos."
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$', email):
            return False, "Correo inválido."
        class UserData:
            pass
        data = UserData()
        data.nombre = nombre
        data.email = email
        data.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        ok = self.model.registrar(data)
        if ok:
            return True, "Cuenta creada exitosamente."
        return False, "Error al crear la cuenta. El correo ya existe."

    def enviar_codigo(self, email):
        if not self.model.buscar_por_email(email):
            return False, "No existe una cuenta con ese correo."
        codigo = str(random.randint(100000, 999999))
        self._codigos[email] = codigo
        try:
            img_path = os.path.join(os.path.dirname(__file__), "..", "..", "base", "assest", "BoreasWindLogo.jpeg")
            img_path = os.path.abspath(img_path)

            msg = MIMEMultipart("related")
            msg["Subject"] = "Recuperación de contraseña - BoreasWind"
            msg["From"] = os.getenv("MAIL_USER")
            msg["To"] = email

            html = f"""
            <html><body style="text-align:center; font-family:Arial">
                <h2>Recuperación de contraseña</h2>
                <p>Hola, tu código de recuperación es:</p>
                <h1 style="letter-spacing:8px">{codigo}</h1>
                <img src="cid:logo" width="150" style="margin-top:20px">
            </body></html>
            """
            msg.attach(MIMEText(html, "html"))

            if os.path.exists(img_path):
                with open(img_path, "rb") as f:
                    img = MIMEImage(f.read())
                    img.add_header("Content-ID", "<logo>")
                    msg.attach(img)

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(os.getenv("MAIL_USER"), os.getenv("MAIL_PASSWORD"))
                server.sendmail(os.getenv("MAIL_USER"), email, msg.as_string())
            return True, "Código enviado a tu correo."
        except Exception as e:
            return False, f"Error al enviar correo: {e}"

    def verificar_codigo(self, email, codigo):
        if self._codigos.get(email) == codigo:
            return True, "Código correcto."
        return False, "Código incorrecto."

    def cambiar_password(self, email, nueva_password):
        if not nueva_password or len(nueva_password) < 8:
            return False, "La contraseña debe tener al menos 8 caracteres."
        hashed = bcrypt.hashpw(nueva_password.encode(), bcrypt.gensalt()).decode()
        self.model.actualizar_password(email, hashed)
        self._codigos.pop(email, None)
        return True, "Contraseña actualizada correctamente."
