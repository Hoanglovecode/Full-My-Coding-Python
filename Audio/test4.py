from gtts import gTTS
import os

text = "Test 4"
tts = gTTS(text=text, lang='en')

# Lấy thư mục hiện tại và tạo đường dẫn đầy đủ
current_directory = os.getcwd()
file_path = os.path.join(current_directory, "test4.mp3")

# Lưu file
tts.save(file_path)

print(f"Đã tạo file MP3 thành công!")
print(f"Bạn hãy vào thư mục này để lấy file: {file_path}")