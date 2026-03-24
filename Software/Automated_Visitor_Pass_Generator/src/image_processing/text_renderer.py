def draw_text_auto_fit(draw, text, font_path, bbox, initial_font_size, min_font_size, color):
    """Draws text within a given bounding box, automatically adjusting font size and wrapping.

    The function attempts to fit the text by reducing font size and wrapping words if necessary.

    Args:
        draw (PIL.ImageDraw.ImageDraw): The ImageDraw object to draw on.
        text (str): The text content to draw.
        font_path (str): Path to the custom font file.
        bbox (tuple): Bounding box (x, y, width, height) for the text area.
        initial_font_size (int): The starting font size attempt.
        min_font_size (int): The minimum font size allowed.
        color (tuple): RGB color for the text.
    """
    x, y, max_width, max_height = bbox

    def get_text_size(text_content, current_font):
        """Helper to get accurate text dimensions, considering multi-line text."""
        lines = text_content.split('\n')
        line_heights = [current_font.getbbox(line)[3] - current_font.getbbox(line)[1] for line in lines] # Calculate height for each line.
        total_height = sum(line_heights)
        max_line_width = max([current_font.getbbox(line)[2] - current_font.getbbox(line)[0] for line in lines]) # Max width among lines.
        return max_line_width, total_height

    # Iterate to find the best font size that fits the text within the bounding box.
    current_font_size = initial_font_size
    wrapped_text = text

    font_cache = {} # Cache for loaded fonts to improve performance.

    while current_font_size >= min_font_size:
        if current_font_size in font_cache:
          font = font_cache[current_font_size]
        else:
          try:
            font = ImageFont.truetype(font_path, current_font_size) if os.path.exists(font_path) else ImageFont.load_default()
          except IOError:
            print(f"Warning: Could not load font from {font_path}. Using default font for size {current_font_size}.")
            font = ImageFont.load_default()
          font_cache[current_font_size] = font

        # Simple word wrap logic to break text into lines that fit the max_width.
        words = text.split(' ')
        lines = []
        current_line = []
        for word in words:
            test_line = ' '.join(current_line + [word])
            test_width, _ = get_text_size(test_line, font)
            if test_width <= max_width:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
        lines.append(' '.join(current_line)) # Add the last accumulated line.
        wrapped_text = '\n'.join(lines)

        text_width, text_height = get_text_size(wrapped_text, font)

        if text_width <= max_width and text_height <= max_height:
            break # Found a suitable font size and wrapping.
        current_font_size -= 1
    else:
        # If no size fits, use min_font_size and potentially truncate if it's still too long.
        print(f"Warning: Could not fit text '{text}' into bbox {bbox} even at min font size {min_font_size}. Text might be truncated or overflow.")
        try:
          if os.path.exists(font_path):
            font = ImageFont.truetype(font_path, min_font_size)
          else:
            font = ImageFont.load_default()
        except IOError:
          font = ImageFont.load_default()
        # Re-calculate wrapped_text with the final (min) font size for drawing.
        words = text.split(' ')
        lines = []
        current_line = []
        for word in words:
            test_line = ' '.join(current_line + [word])
            test_width, _ = get_text_size(test_line, font)
            if test_width <= max_width:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
        lines.append(' '.join(current_line))
        wrapped_text = '\n'.join(lines)

    # Center the text horizontally and vertically within the bounding box.
    text_width, text_height = get_text_size(wrapped_text, font)
    center_x = x + max_width / 2
    center_y = y + max_height / 2
    draw.text((center_x - text_width / 2, center_y - text_height / 2), wrapped_text, font=font, fill=color, align="center")

print('Helper functions defined.')
