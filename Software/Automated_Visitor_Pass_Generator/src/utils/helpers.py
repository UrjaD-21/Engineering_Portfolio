def sanitize_name_for_filename(name):
    """Sanitizes a string to be used as a valid part of a filename.

    Replaces non-alphanumeric characters (except underscore) with underscores.
    """
    return re.sub(r'[^a-zA-Z0-9_]', '_', name)



def find_photo_path(participant_name):
    """Looks up the local file path for a participant's photo using the pre-built photo_map.

    Args:
        participant_name (str): The name of the participant.

    Returns:
        str: The full path to the participant's photo, or None if not found.
    """
    key = re.sub(r'[^a-zA-Z0-9_]', '_', participant_name.lower()) # Create a sanitized key.
    return photo_map.get(key)



def apply_rounded_corners(im, rad):
    """Applies rounded corners to a PIL Image using an alpha mask.

    Args:
        im (PIL.Image.Image): The input image.
        rad (int): The radius for the rounded corners.

    Returns:
        PIL.Image.Image: The image with rounded corners applied.
    """
    circle = Image.new('L', (rad * 2, rad * 2), 0) # Create a black circle for the mask.
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255) # Draw a white ellipse in the circle.
    alpha = Image.new('L', im.size, 255) # Create an alpha layer for the image.
    w, h = im.size
    # Paste parts of the circle mask to create rounded corners on the alpha layer.
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha) # Apply the constructed alpha layer to the image.
    return im

