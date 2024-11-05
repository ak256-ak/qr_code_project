FROM python:3.9-slim
WORKDIR /app
COPY generate_qr.py .
RUN pip install qrcode[pil]
CMD ["python", "generate_qr.py"]

