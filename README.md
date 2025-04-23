# GIF Generator AI

```
 ╔═══════════════════════════════════════╗
 ║   ██████╗ ██╗███████╗  ██████╗ ███████╗███╗   ██╗   ║
 ║  ██╔════╝ ██║██╔════╝ ██╔════╝ ██╔════╝████╗  ██║   ║
 ║  ██║  ███╗██║█████╗   ██║  ███╗█████╗  ██╔██╗ ██║   ║
 ║  ██║   ██║██║██╔══╝   ██║   ██║██╔══╝  ██║╚██╗██║   ║
 ║  ╚██████╔╝██║██║      ╚██████╔╝███████╗██║ ╚████║   ║
 ║   ╚═════╝ ╚═╝╚═╝       ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ║
 ╚═══════════════════════════════════════╝
```

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

Generate a GIF directly from a prompt:
```bash
python generate_ai_image.py "your prompt" -o output.gif -f 3 -s 20
```

Options:
- `--output` or `-o`: Output GIF filename (default: output/ai_image.gif)
- `--steps` or `-s`: Number of inference steps per frame (default: 50)
- `--guidance` or `-g`: Guidance scale (default: 7.5)
- `--frames` or `-f`: Number of frames to generate (default: 3) 