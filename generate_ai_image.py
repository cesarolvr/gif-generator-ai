import click
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

@click.command()
@click.argument('prompt')
@click.option('--output', '-o', default='output/ai_image.png', help='Output image filename')
@click.option('--steps', '-s', default=50, help='Number of inference steps')
@click.option('--guidance', '-g', default=7.5, help='Guidance scale')
def generate(prompt, output, steps, guidance):
    """Generate an image from a text prompt using Stable Diffusion."""
    try:
        # Initialize the pipeline
        pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float32,
            safety_checker=None
        )
        
        # Move to GPU if available
        if torch.cuda.is_available():
            pipe = pipe.to("cuda")
        
        # Generate the image
        image = pipe(
            prompt,
            num_inference_steps=steps,
            guidance_scale=guidance
        ).images[0]
        
        # Save the image
        image.save(output)
        click.echo(f"Successfully generated image: {output}")
        
    except Exception as e:
        click.echo(f"Error generating image: {str(e)}")

if __name__ == '__main__':
    generate() 