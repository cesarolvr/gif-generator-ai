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

A command-line tool to create GIFs from AI-generated images using Apple's Metal framework for GPU acceleration.

## System Requirements

- Apple Silicon Mac (M1/M2/M3)
- macOS 12.0 or later
- Docker Desktop for Mac
- At least 8GB RAM (16GB recommended)

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

## Performance Notes

- The app uses Apple's Metal framework for GPU acceleration on Apple Silicon Macs
- NVIDIA CUDA is supported for systems with NVIDIA GPUs
- Image generation is significantly faster with GPU acceleration (Metal or CUDA)
- CPU fallback is available but much slower (approximately 10-20x slower)
- Recommended to use at least 20 steps for good quality images

### GPU Acceleration Troubleshooting

#### For Apple Silicon Macs (M1/M2/M3):
- Ensure you're using macOS 12.0 or later
- Make sure PyTorch 2.0+ is installed (included in requirements.txt)
- The app will automatically detect and use Metal for acceleration
- If you encounter issues, try setting the environment variable: `export PYTORCH_ENABLE_MPS_FALLBACK=1`

#### For NVIDIA GPU Users:
- Install PyTorch with CUDA support: `pip install torch==2.2.0 --extra-index-url https://download.pytorch.org/whl/cu118`
- Ensure NVIDIA drivers are properly installed
- For Docker users, make sure to use NVIDIA Container Toolkit and add GPU runtime to docker-compose.yml
