import click
from PIL import Image, ImageSequence
import os

@click.group()
def cli():
    """A CLI tool to generate and manipulate GIFs."""
    pass

@cli.command()
@click.argument('input_files', nargs=-1, type=click.Path(exists=True))
@click.option('--output', '-o', default='output.gif', help='Output GIF filename')
@click.option('--duration', '-d', default=100, help='Duration of each frame in milliseconds')
def create(input_files, output, duration):
    """Create a GIF from multiple images."""
    if not input_files:
        click.echo("Error: No input files provided")
        return

    # Open all images
    images = []
    for file in input_files:
        try:
            img = Image.open(file)
            images.append(img)
        except Exception as e:
            click.echo(f"Error opening {file}: {str(e)}")
            return

    # Save as GIF
    try:
        images[0].save(
            output,
            save_all=True,
            append_images=images[1:],
            duration=duration,
            loop=0
        )
        click.echo(f"Successfully created {output}")
    except Exception as e:
        click.echo(f"Error creating GIF: {str(e)}")

@cli.command()
@click.argument('input_gif', type=click.Path(exists=True))
@click.option('--output', '-o', default='resized.gif', help='Output GIF filename')
@click.option('--width', '-w', type=int, help='New width')
@click.option('--height', '-h', type=int, help='New height')
def resize(input_gif, output, width, height):
    """Resize a GIF while maintaining aspect ratio."""
    try:
        with Image.open(input_gif) as im:
            # Calculate new dimensions while maintaining aspect ratio
            if width and height:
                new_size = (width, height)
            elif width:
                ratio = width / float(im.size[0])
                new_size = (width, int(im.size[1] * ratio))
            elif height:
                ratio = height / float(im.size[1])
                new_size = (int(im.size[0] * ratio), height)
            else:
                click.echo("Error: Please specify either width or height")
                return

            # Process each frame
            frames = []
            for frame in ImageSequence.Iterator(im):
                frame = frame.copy()
                frame = frame.resize(new_size, Image.Resampling.LANCZOS)
                frames.append(frame)

            # Save the resized GIF
            frames[0].save(
                output,
                save_all=True,
                append_images=frames[1:],
                duration=im.info.get('duration', 100),
                loop=0
            )
            click.echo(f"Successfully resized and saved as {output}")
    except Exception as e:
        click.echo(f"Error processing GIF: {str(e)}")

if __name__ == '__main__':
    cli() 