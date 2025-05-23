import click
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import time
from tqdm import tqdm

@click.command()
@click.argument('prompt')
@click.option('--output', '-o', default='output/ai_image.gif', help='Output GIF filename')
@click.option('--steps', '-s', default=50, help='Number of inference steps')
@click.option('--guidance', '-g', default=8.5, help='Guidance scale - higher values make the image more closely match the prompt')
@click.option('--frames', '-f', default=3, help='Number of frames to generate')
@click.option('--duration', '-d', default=500, help='Duration between frames in milliseconds')
def generate(prompt, output, steps, guidance, frames, duration):
    """Generate a GIF from a text prompt using Stable Diffusion."""
    try:
        click.echo("Loading model... (this may take a few seconds)")
        start_time = time.time()

        # Initialize the pipeline with a more recent model
        pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float32,
            safety_checker=None,
            requires_safety_checker=False
        )

        # Move to GPU if available
        if torch.cuda.is_available():
            pipe = pipe.to("cuda")
            click.echo("Using GPU for faster generation")
        else:
            click.echo("Using CPU - generation will be slower")
            click.echo(f"Estimated time per frame: {steps * 1.5:.1f} seconds")

        # Generate frames
        frames_list = []
        click.echo(f"\nGenerating {frames} frames...")

        # Use a base seed for consistency across frames
        base_seed = int(time.time())
        click.echo(f"Using base seed: {base_seed} for consistent animation")

        for frame in range(frames):
            click.echo(f"\nGenerating frame {frame + 1}/{frames}")
            with tqdm(total=steps, desc="Progress") as pbar:
                def callback_on_step_end(pipe, i, t, callback_kwargs):
                    pbar.update(1)
                    return callback_kwargs

                # Use small increments to the base seed for subtle variations between frames
                current_seed = base_seed + (frame * 10)

                image = pipe(
                    prompt,
                    num_inference_steps=steps,
                    guidance_scale=guidance,
                    callback_on_step_end=callback_on_step_end,
                    width=512,
                    height=512,
                    seed=current_seed  # Use consistent seed pattern for coherent animation
                ).images[0]

                frames_list.append(image)

        # Save as GIF
        if frames_list:
            frames_list[0].save(
                output,
                save_all=True,
                append_images=frames_list[1:],
                duration=duration,  # Duration between frames in milliseconds
                loop=0
            )

            total_time = time.time() - start_time
            click.echo(f"\nSuccessfully generated GIF: {output}")
            click.echo(f"Total time: {total_time:.1f} seconds")

    except Exception as e:
        click.echo(f"Error generating GIF: {str(e)}")

if __name__ == '__main__':
    generate() 
