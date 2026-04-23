from PIL import Image, ImageEnhance, ImageOps

def apply_studio_filter(input_path, output_path):
    try:
        # 1. เปิดไฟล์รูปภาพ
        img = Image.open(input_path)
        
        # จัดการเรื่องการหมุนภาพอัตโนมัติ (เผื่อรูปถ่ายมาจากมือถือแล้วตะแคง)
        img = ImageOps.exif_transpose(img)

        # 2. ปรับความสว่าง (Brightness) 
        # เพิ่มขึ้นประมาณ 20% เพื่อให้ดูเหมือนมีไฟสตูดิโอส่อง
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1.2)

        # 3. ปรับความคมชัดของสี (Contrast)
        # เพิ่มขึ้นเล็กน้อยเพื่อให้ภาพดูมีมิติ ไม่แบน
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.1)

        # 4. ปรับความอิ่มสี (Color/Saturation)
        # ปรับให้สีดูสดใสขึ้นอีกนิด (ประมาณ 10%)
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(1.1)

        # 5. ปรับความคม (Sharpness)
        # ช่วยให้รายละเอียดใบหน้าดูชัดขึ้น
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(1.5)

        # 6. บันทึกผลลัพธ์
        img.save(output_path, quality=95)
        print(f"แต่งรูปเสร็จแล้วครับ! บันทึกไว้ที่: {output_path}")

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

# กำหนดที่อยู่ไฟล์
input_img = "/Users/duke/Desktop/dd/IMG_6668.JPG"
output_img = "/Users/duke/Desktop/dd/kru_duke_studio.jpg"

apply_studio_filter(input_img, output_img)
