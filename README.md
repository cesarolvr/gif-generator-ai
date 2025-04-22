# GIF Generator CLI

A simple command-line tool to create and manipulate GIFs.

## Installation

1. Make sure you have Python 3.7+ installed
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage with Docker

The recommended way to run this tool is using Docker:

```bash
# Build and start the container
docker-compose up -d --build

# Generate GIFs using the commands below (add 'docker-compose exec gif-generator' before each command)
docker-compose exec gif-generator python gif_generator.py --help
```

## Usage

### Creating a GIF from multiple images

```bash
python gif_generator.py create image1.jpg image2.jpg image3.jpg --output my_gif.gif --duration 200
```

Options:
- `--output` or `-o`: Output filename (default: output.gif)
- `--duration` or `-d`: Duration of each frame in milliseconds (default: 100)

### Creating a GIF using AI-generated images

1. First, generate images using AI prompts:
```bash
# Generate first frame
python generate_ai_image.py "your prompt for first frame" -o frame1.png

# Generate second frame
python generate_ai_image.py "your prompt for second frame" -o frame2.png

# Generate third frame
python generate_ai_image.py "your prompt for third frame" -o frame3.png
```

2. Then combine them into a GIF:
```bash
python gif_generator.py create frame1.png frame2.png frame3.png --output ai_generated.gif --duration 500
```

Options for AI image generation:
- `--output` or `-o`: Output image filename
- `--steps` or `-s`: Number of inference steps (default: 50)
- `--guidance` or `-g`: Guidance scale (default: 7.5)

### Resizing a GIF

```bash
python gif_generator.py resize input.gif --width 500 --output resized.gif
```

Options:
- `--output` or `-o`: Output filename (default: resized.gif)
- `--width` or `-w`: New width (optional)
- `--height` or `-h`: New height (optional)

Note: If only width or height is specified, the other dimension will be calculated to maintain the aspect ratio. 