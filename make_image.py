from PIL import Image, ImageDraw

# สร้างรูปภาพใหม่ พื้นหลังสีน้ำเงินเข้ม (RGB: 10, 40, 80) ขนาด 600x400
img = Image.new('RGB', (600, 400), color=(10, 40, 80))

# เตรียมตัววาด
draw = ImageDraw.Draw(img)

# วาดรูปสี่เหลี่ยมสีเหลืองไว้ตรงกลาง
draw.rectangle([50, 50, 550, 350], outline="gold", width=5)

# วาดวงกลมมุมบนขวา
draw.ellipse([450, 20, 550, 120], fill="orange")

# บันทึกไฟล์เป็นรูป .png
img.save('/Users/duke/my-first-web/kru_duke_art.png')

print("สร้างรูปภาพสำเร็จแล้วที่: /Users/duke/my-first-web/kru_duke_art.png")
