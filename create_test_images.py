from PIL import Image, ImageDraw

# Create three test images with different colors
for i in range(3):
    # Create a new image with a different color for each frame
    img = Image.new('RGB', (200, 200), color=(
        255 if i == 0 else 0,  # Red for first image
        255 if i == 1 else 0,  # Green for second image
        255 if i == 2 else 0   # Blue for third image
    ))
    
    # Add some text to identify each frame
    draw = ImageDraw.Draw(img)
    draw.text((50, 80), f"Frame {i+1}", fill='white')
    
    # Save the image
    img.save(f'test_image_{i+1}.png') 