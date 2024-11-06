import qrcode
import os

def generate_qr_code():
    url = os.getenv('QR_DATA_URL', 'https://github.com/ak256-ak')  # Default to your GitHub URL
    qr_code_dir = os.getenv('QR_CODE_DIR', 'qr_codes')
    qr_code_filename = os.getenv('QR_CODE_FILENAME', 'github_qr.png')
    
    print(f"URL to encode: {url}")
    print(f"QR code directory: {qr_code_dir}")
    print(f"QR code filename: {qr_code_filename}")

    if not os.path.exists(qr_code_dir):
        os.makedirs(qr_code_dir)
        print(f"Created directory: {qr_code_dir}")

    img = qrcode.make(url)
    img_path = os.path.join(qr_code_dir, qr_code_filename)
    img.save(img_path)
    print(f"QR code generated and saved as {img_path}")

if __name__ == "__main__":
    generate_qr_code()
