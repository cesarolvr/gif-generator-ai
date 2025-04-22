# GIF Generator CLI

A simple command-line tool to create and manipulate GIFs.

## Installation

1. Make sure you have Python 3.7+ installed
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Creating a GIF from multiple images

```bash
python gif_generator.py create image1.jpg image2.jpg image3.jpg --output my_gif.gif --duration 200
```

Options:
- `--output` or `-o`: Output filename (default: output.gif)
- `--duration` or `-d`: Duration of each frame in milliseconds (default: 100)

### Resizing a GIF

```bash
python gif_generator.py resize input.gif --width 500 --output resized.gif
```

Options:
- `--output` or `-o`: Output filename (default: resized.gif)
- `--width` or `-w`: New width (optional)
- `--height` or `-h`: New height (optional)

Note: If only width or height is specified, the other dimension will be calculated to maintain the aspect ratio. 