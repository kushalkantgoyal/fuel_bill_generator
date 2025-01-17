import os
from PIL import Image, ImageDraw, ImageFont


def generate_fuel_bill_with_logo_png(output_path, logo_path, date, time, fuel_rate, volume, vehicle_no, mode, product,receipt_no):
    # Calculate total amount
    amount = fuel_rate * volume

    # Create an image canvas
    img_width, img_height = 280, 470  # Increased height for the logo
    img = Image.new("RGB", (img_width, img_height), "white")
    draw = ImageDraw.Draw(img)

    # Define fonts
    font_path = "resources/DejaVuSans.ttf"  # Path to a font that supports Unicode
    font_title = ImageFont.truetype(font_path, 17)
    font_text = ImageFont.truetype(font_path, 14)

    # Add logo
    try:
        logo = Image.open(logo_path)
        logo_width, logo_height = 150, 100  # Resize logo to fit nicely
        logo = logo.resize((logo_width, logo_height))
        img.paste(logo, (img_width // 2 - logo_width // 2, 10))
    except Exception as e:
        print(f"Error loading logo: {e}")

    # Add header
    y_position = 120  # Adjust below the logo

    text = "Welcome To BPCL"
    text_bbox = draw.textbbox((0, 0), text, font=font_title)  # Get the bounding box of the text
    text_width = text_bbox[2] - text_bbox[0]
    draw.text(((img_width - text_width) / 2, y_position), text, font=font_title, fill="black")

    y_position += 25
    text = "SHARMA BROTHERS"
    text_bbox = draw.textbbox((0, 0), text, font=font_title)  # Get the bounding box of the text
    text_width = text_bbox[2] - text_bbox[0]
    draw.text(((img_width - text_width) / 2, y_position), text, font=font_title, fill="black")

    y_position += 25
    text = "TONK ROAD JAIPUR"
    text_bbox = draw.textbbox((0, 0), text, font=font_title)  # Get the bounding box of the text
    text_width = text_bbox[2] - text_bbox[0]
    draw.text(((img_width - text_width) / 2, y_position), text, font=font_title, fill="black")

    # Add receipt details
    y_position += 40
    line_spacing = 25

    details = [
        ["RECEIPT NO.", f": {receipt_no}"],
        [f"DATE", f": {date}"],
        [f"TIME", f": {time}"],
        [f"VEH. NO.", f": {vehicle_no}"],
        [f"PRODUCT:", f": {product}"],
        [f"RATE/LTR", f": ₹{fuel_rate}"],
        [f"VOLUME", f": {volume:.2f} lt"],
        [f"AMOUNT", f": ₹{amount:.2f}"],
        [f"MODE", f": {mode}"],
    ]

    for detail in details:
        draw.text((20, y_position), detail[0], font=font_text, fill="black")
        draw.text((150, y_position), detail[1], font=font_text, fill="black")
        y_position += line_spacing

    # Footer message
    footer = [
        "THANK YOU! VISIT AGAIN",
    ]

    for line in footer:
        draw.text((30, y_position), line, font=font_text, fill="black")
        y_position += line_spacing

    # Save the PNG
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    img.save(output_path+f"/bill_{date}.png")

    print(f"{date}, {time}, {fuel_rate}, {amount:.2f}, {volume}, {vehicle_no}, {mode}, {product}, {receipt_no}")
