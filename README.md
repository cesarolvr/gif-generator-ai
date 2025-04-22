# GIF Generator AI

A command-line tool to create GIFs from AI-generated images.

## Installation

The recommended way to run this tool is using Docker:

```bash
# Build and start the container
docker-compose up -d --build

# Generate GIFs using the commands below (add 'docker-compose exec gif-generator' before each command)
docker-compose exec gif-generator python generate_ai_image.py --help
```

## Usage

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
python gif_generator.py frame1.png frame2.png frame3.png --output ai_generated.gif --duration 500
```

Options for AI image generation:
- `--output` or `-o`: Output image filename
- `--steps` or `-s`: Number of inference steps (default: 50)
- `--guidance` or `-g`: Guidance scale (default: 7.5)

Options for GIF creation:
- `--output` or `-o`: Output GIF filename (default: output.gif)
- `--duration` or `-d`: Duration of each frame in milliseconds (default: 100) 