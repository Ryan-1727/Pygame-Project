import pygame


def load_frames(sheet, frame_width, frame_height, start_x=0, start_y=0, num_frames=None, scale=1):
    """
    Extract frames from a sprite sheet.

    sheet       - the loaded sprite sheet surface
    frame_width - width of each frame
    frame_height- height of each frame
    start_x     - starting x pixel in the sheet
    start_y     - starting y pixel in the sheet
    num_frames  - how many frames to grab (if None, go until end of row)
    scale       - scaling factor (e.g., 2 = double size, 0.5 = half size)
    """
    frames = []
    sheet_width, sheet_height = sheet.get_size()

    if num_frames is None:
        num_frames = (sheet_width - start_x) // frame_width

    for i in range(num_frames):
        x = start_x + i * frame_width
        y = start_y
        frame = sheet.subsurface(pygame.Rect(x, y, frame_width, frame_height))

        # scale the frame
        if scale != 1:
            new_w = int(frame_width * scale)
            new_h = int(frame_height * scale)
            frame = pygame.transform.scale(frame, (new_w, new_h))

        frames.append(frame)

    return frames


def load_map(filename):
    grid = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:  # skip empty lines
                row = [int(char) for char in line]
                grid.append(row)
    return grid


