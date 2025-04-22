import click
from PIL import Image

@click.command()
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

if __name__ == '__main__':
    create() 