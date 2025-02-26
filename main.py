import qrcode
from PIL import Image, ImageDraw, ImageOps

def create_custom_qr(uri: str, qr_color: str, bg_color: str, file_name: str, icon_path: str):
    """
    Generate a QR code with rounded square modules, a specified URI, color, and background color.
    Change the icon color, add a background and margin around the icon, and place it at the center of the QR code.

    Parameters:
    uri (str): The URI to encode in the QR code.
    qr_color (str): Hex color code for the QR modules.
    bg_color (str): Hex color code for the background.
    file_name (str): Name of the file to save the QR image.
    icon_path (str): Path to the icon to be placed at the center of the QR code.
    """
    # Create a basic QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(uri)
    qr.make(fit=True)

    # Create an image with transparent background
    qr_image = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
    width, height = qr_image.size

    # Create a new image for custom QR with background color
    custom_qr = Image.new("RGBA", (width, height), bg_color)
    draw = ImageDraw.Draw(custom_qr)

    # Draw rounded square modules instead of circles or regular squares
    module_size = 10  # Size of each module (from 1 to 10)
    corner_radius = 1  # Radius for rounded corners
    for y in range(0, height, module_size):
        for x in range(0, width, module_size):
            if qr_image.getpixel((x + module_size // 2, y + module_size // 2))[0] == 0:  # Check if the module is black
                draw.rounded_rectangle(
                    [(x, y), (x + module_size, y + module_size)],
                    radius=corner_radius,
                    fill=qr_color,
                )

    # Load the icon and ensure it's RGBA
    icon = Image.open(icon_path).convert("RGBA")

    # Create a new image filled with qr_color
    colored_icon = Image.new("RGBA", icon.size, qr_color)

    # Use the alpha channel of the original icon as a mask to apply the color only to non-transparent areas
    icon = Image.composite(colored_icon, icon, icon)

    # Add background and margin around the icon
    margin_size = 20
    icon_size = width // 5  # Icon size is 1/5th of the QR code size
    icon = icon.resize((icon_size, icon_size), Image.LANCZOS)

    # Create a new image with background color and margin
    icon_bg_size = (icon_size + margin_size, icon_size + margin_size)
    icon_bg = Image.new("RGBA", icon_bg_size, bg_color)

    # Paste the icon onto the background with transparency handling
    icon_bg.paste(icon, (margin_size // 2, margin_size // 2), icon)

    # Add the icon with background to the center of the QR code
    icon_position = ((width - icon_bg.size[0]) // 2, (height - icon_bg.size[1]) // 2)
    custom_qr.paste(icon_bg, icon_position, icon_bg)

    # Save the final image
    custom_qr.save(file_name)
    print(f"Custom QR code saved as {file_name}")

if __name__ == "__main__":
    # Example usage
    uri = "folder_path"
    qr_color = "#1a73e8"  # Blue color for QR modules
    bg_color = "#f1f3f4"  # Light gray background
    file_name = "qr.png"
    icon_path = "folder-1484.png"  # Path to the icon of a folder

    create_custom_qr(uri, qr_color, bg_color, file_name, icon_path)
