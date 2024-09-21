from flask import Flask, request, render_template, jsonify, send_file, url_for
import os
import tempfile
from substitution_cipher import encrypt, decrypt, generate_key
from shift_cipher import shift_encrypt, shift_decrypt
from affine_cipher import affine_encrypt, affine_decrypt
from vigenere_cipher import vigenere_encrypt, vigenere_decrypt

app = Flask(__name__)

# Route cho Shift Cipher
@app.route("/", methods=["GET", "POST"])
def shift_cipher():
    result = ""
    error = ""
    download_url = ""
    text = request.form.get("text", "")
    key = request.form.get("key", "")

    if request.method == "POST":
        try:
            key = int(key)
            if key < 0 or key > 25:
                error = "Vui lòng nhập giá trị dịch chuyển từ 0 đến 25."
            else:
                action = request.form["action"]

                if 'file' in request.files and request.files['file'].filename:
                    file = request.files['file']
                    filename = file.filename
                    file_text = file.read().decode('utf-8')

                    if action == "encrypt":
                        result = shift_encrypt(file_text, key)
                        output_filename = f"encrypted_{filename}"
                    elif action == "decrypt":
                        result = shift_decrypt(file_text, key)
                        output_filename = f"decrypted_{filename}"

                    # Lưu kết quả vào file tạm thời
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt', mode='w', encoding='utf-8') as temp_file:
                        temp_file.write(f"\n{result}")
                        temp_file_path = temp_file.name

                    download_url = f"/download/{os.path.basename(temp_file_path)}"

                else:
                    if action == "encrypt":
                        result = shift_encrypt(text, key)
                    elif action == "decrypt":
                        result = shift_decrypt(text, key)

                    # Lưu kết quả vào file tạm thời
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt', mode='w', encoding='utf-8') as temp_file:
                        temp_file.write(f"\n{result}")
                        temp_file_path = temp_file.name

                    download_url = f"/download/{os.path.basename(temp_file_path)}"

        except ValueError:
            error = "Vui lòng nhập số nguyên cho giá trị dịch chuyển."

    return render_template("shift_cipher.html", result=result, error=error, text=text, key=key if key else '', download_url=download_url)

# Route cho Substitution Cipher
# app.py

@app.route("/substitution-cipher", methods=["GET", "POST"])
def substitution_cipher():
    result = ""
    error = ""
    text = request.form.get("text", "")
    generated_key = request.form.get("generated_key", "")
    input_key = request.form.get("input_key", "")
    download_url = ""

    if request.method == "POST":
        action = request.form["action"]

        if 'file' in request.files and request.files['file'].filename:
            file = request.files['file']
            filename = file.filename
            file_text = file.read().decode('utf-8')

            if action == "encrypt_sub":
                if not generated_key:
                    generated_key = generate_key()
                result = encrypt(file_text, generated_key)
                output_filename = f"encrypted_{filename}"
                with tempfile.NamedTemporaryFile(delete=False, suffix='.txt', mode='w', encoding='utf-8') as temp_file:
                    temp_file.write(f"Key: {generated_key}\nResult:\n{result}")
                    temp_file_path = temp_file.name

                download_url = f"/download/{os.path.basename(temp_file_path)}"

            elif action == "decrypt_sub":
                if not input_key:
                    error = "Vui lòng nhập khóa để giải mã."
                else:
                    try:
                        result = decrypt(file_text, input_key)
                        output_filename = f"decrypted_{filename}"
                        with tempfile.NamedTemporaryFile(delete=False, suffix='.txt', mode='w', encoding='utf-8') as temp_file:
                            temp_file.write(f"Key: {input_key}\nResult:\n{result}")
                            temp_file_path = temp_file.name

                        download_url = f"/download/{os.path.basename(temp_file_path)}"
                    except Exception as e:
                        error = f"Khóa không hợp lệ hoặc văn bản không thể giải mã: {str(e)}"

        else:
            if action == "encrypt_sub":
                if not generated_key:
                    generated_key = generate_key()
                result = encrypt(text, generated_key)
                output_filename = "encrypted_result.txt"
                with tempfile.NamedTemporaryFile(delete=False, suffix='.txt', mode='w', encoding='utf-8') as temp_file:
                    temp_file.write(f"Key: {generated_key}\nResult:\n{result}")
                    temp_file_path = temp_file.name

                download_url = f"/download/{os.path.basename(temp_file_path)}"
            elif action == "decrypt_sub":
                if not input_key:
                    error = "Vui lòng nhập khóa để giải mã."
                else:
                    try:
                        result = decrypt(text, input_key)
                        output_filename = "decrypted_result.txt"
                        with tempfile.NamedTemporaryFile(delete=False, suffix='.txt', mode='w', encoding='utf-8') as temp_file:
                            temp_file.write(f"Key: {input_key}\nResult:\n{result}")
                            temp_file_path = temp_file.name

                        download_url = f"/download/{os.path.basename(temp_file_path)}"
                    except Exception as e:
                        error = f"Khóa không hợp lệ hoặc văn bản không thể giải mã: {str(e)}"

    return render_template("substitution_cipher.html", result=result, error=error, text=text, generated_key=generated_key, download_url=download_url)

# Route cho Affine Cipher
@app.route("/affine-cipher", methods=["GET", "POST"])
def affine_cipher():
    result = ""
    error = ""
    download_url = ""
    text = request.form.get("text", "")
    a = request.form.get("a", "")
    b = request.form.get("b", "")

    if request.method == "POST":
        try:
            a = int(a)
            b = int(b)

            if a < 1 or a > 25 or b < 0 or b > 25:
                error = "Vui lòng nhập giá trị a từ 1 đến 25 và b từ 0 đến 25."
            else:
                action = request.form["action"]

                if 'file' in request.files and request.files['file'].filename:
                    file = request.files['file']
                    filename = file.filename
                    file_text = file.read().decode('utf-8')

                    if action == "encrypt":
                        result = affine_encrypt(file_text, a, b)
                        output_filename = f"encrypted_{filename}"
                    elif action == "decrypt":
                        result = affine_decrypt(file_text, a, b)
                        output_filename = f"decrypted_{filename}"

                    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt', mode='w', encoding='utf-8') as temp_file:
                        temp_file.write(f"\n{result}")
                        temp_file_path = temp_file.name

                    download_url = f"/download/{os.path.basename(temp_file_path)}"

                else:
                    if action == "encrypt":
                        result = affine_encrypt(text, a, b)
                    elif action == "decrypt":
                        result = affine_decrypt(text, a, b)

                    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt', mode='w', encoding='utf-8') as temp_file:
                        temp_file.write(f"\n{result}")
                        temp_file_path = temp_file.name

                    download_url = f"/download/{os.path.basename(temp_file_path)}"

        except ValueError:
            error = "Vui lòng nhập số nguyên hợp lệ cho a và b."

    return render_template("affine_cipher.html", result=result, error=error, text=text, a=a if a else '', b=b if b else '', download_url=download_url)

@app.route("/vigenere-cipher", methods=["GET", "POST"])
def vigenere_cipher():
    result = ""
    error = ""
    text = request.form.get("text", "")
    key = request.form.get("key", "")
    download_url = ""

    if request.method == "POST":
        if not key.isalpha():
            error = "Vui lòng nhập một key chỉ chứa chữ cái."
        else:
            action = request.form["action"]

            if 'file' in request.files and request.files['file'].filename:
                file = request.files['file']
                filename = file.filename
                file_text = file.read().decode('utf-8')

                if action == "encrypt_vigenere":
                    result = vigenere_encrypt(file_text, key)
                    output_filename = f"encrypted_{filename}"
                elif action == "decrypt_vigenere":
                    result = vigenere_decrypt(file_text, key)
                    output_filename = f"decrypted_{filename}"

                # Save result to temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix='.txt', mode='w', encoding='utf-8') as temp_file:
                    temp_file.write(f"\n{result}")
                    temp_file_path = temp_file.name

                download_url = f"/download/{os.path.basename(temp_file_path)}"

            else:
                if action == "encrypt_vigenere":
                    result = vigenere_encrypt(text, key)
                elif action == "decrypt_vigenere":
                    result = vigenere_decrypt(text, key)

                # Save result to temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix='.txt', mode='w', encoding='utf-8') as temp_file:
                    temp_file.write(f"\n{result}")
                    temp_file_path = temp_file.name

                download_url = f"/download/{os.path.basename(temp_file_path)}"

    return render_template("vigenere_cipher.html", result=result, error=error, text=text, key=key if key else '', download_url=download_url)

# Route để sinh khóa
@app.route("/generate-key")
def generate_key_route():
    key = generate_key()
    return jsonify({"key": key})

# Route để tải xuống file kết quả
@app.route("/download/<filename>")
def download_file(filename):
    return send_file(os.path.join(tempfile.gettempdir(), filename), as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
