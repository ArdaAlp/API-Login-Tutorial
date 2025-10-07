[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.105-green)](https://fastapi.tiangolo.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-orange)](https://www.sqlite.org/index.html)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

# FastAPI Kullanıcı Yönetim Sistemi

Bu proje, **FastAPI**, **SQLite** ve **Jinja2** kullanarak basit bir kullanıcı yönetim sistemi oluşturur. Kullanıcılar sisteme kayıt olabilir, giriş yapabilir ve şifrelerini unutmaları durumunda görüntüleyebilirler.

---

## Özellikler 🌟

- Kullanıcı kayıt (Register)  
- Kullanıcı girişi (Login)  
- Dashboard görüntüleme
- Şifre unutma (Forgotten Password)  
- SQLite veritabanı ile kullanıcı verilerini saklama  
- Jinja2 ile HTML templating  

---

## Kurulum 💻

### 1. Projeyi klonlayın:
```bash
git clone https://github.com/ArdaAlp/API-Login-Tutorial.git
cd "API-Login-Tutorial"
```

<br>

### 2. Sanal ortam oluşturun ve aktif edin:
```python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

<br>

### 3. Gerekli paketleri yükleyin:
```
pip install fastapi uvicorn jinja2 pydantic
```

---

## Kullanım 📌
- #### Kayıt Ol: ```/register``` sayfasından kullanıcı adı ve şifre ile kayıt olun.

- #### Giriş Yap: ```/login``` sayfasından kullanıcı adı ve şifre ile giriş yapın.

- #### Şifreyi Unuttum: ```/forgotten``` sayfasından kullanıcı adınızı girerek şifrenizi görebilirsiniz.

- #### Dashboard: Başarılı giriş sonrası tüm kullanıcı verilerini görebileceğiniz dashboard açılır.

---

## Çalıştırma ▶️
*Konsoldan:* ```uvicorn main:app --reload``` **ya da** ```fastapi dev app.py```

*Tarayıcıdan:* ```http://127.0.0.1:8000```

*Swagger:* ```http://127.0.0.1:8000/docs```

---

## Veritabanı 🗂
*SQLite kullanılır ve proje dizininde* ```users.db``` *olarak saklanır.*

```user``` tablosu aşağıdaki alanlara sahiptir:

| Alan     | Tür     | Açıklama               |
| -------- | ------- | ---------------------- |
| id       | INTEGER | Otomatik artan ID      |
| username | TEXT    | Kullanıcı adı (unique) |
| password | TEXT    | Şifre                  |

---

## Notlar 🔧
- *Bu proje prototip amaçlıdır, şifreler plain text olarak saklanır. Üretim ortamında hashleme kullanılmalıdır.*

- ***Projeyi geliştirmek için** kullanıcı rolleri, token tabanlı authentication veya frontend framework entegrasyonu eklenebilir.*
