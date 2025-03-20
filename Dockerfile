# Python resmi imajını kullan
FROM python:3.9

# Çalışma dizini oluştur
WORKDIR /app

# Bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Ana dosyayı çalıştır
CMD ["python", "main.py"]
