import click


from painter.model import Circle, Painter, Point, Rectangle, Triangle


@click.group()
@click.pass_context
def painter(ctx: click.Context) -> None:
    """A simple painter that creates and draws circles, rectangles and triangles."""
    ctx.obj = Painter()
    


@painter.command()
@click.argument('x', type=float)
@click.argument('y', type=float)
@click.argument('radius', type=float)
@click.pass_obj
def add_circle(painter, x: float, y: float, radius: float) -> None:
    """
    Add a circle given the center and radius.
    
    Example usage:
    
    $ painter add-circle 0 0 5
    
    """
    circle = Circle(Point(x, y), radius)
    painter.add_shape(circle)
    click.echo("Circle added.")


@painter.command()
@click.argument('x1', type=float)
@click.argument('y1', type=float)
@click.argument('x2', type=float)
@click.argument('y2', type=float)
@click.argument('x3', type=float)
@click.argument('y3', type=float)
@click.pass_obj
def add_triangle(painter, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> None:
    """
    Add a triangle given the coordinates of its three vertices.
    
    Example usage:
    
    $ painter add-triangle 0 0 5 0 0 5
    
    When a value is negative, it must be preceded by --, like this:
    
    $ painter add-triangle 0 0 5 0 0 -- -5
    
    """
    triangle = Triangle(Point(x1, y1), Point(x2, y2), Point(x3, y3))
    painter.add_shape(triangle)
    click.echo("Triangle added.")


@painter.command()
@click.argument('x1', type=float)
@click.argument('y1', type=float)
@click.argument('x2', type=float)
@click.argument('y2', type=float)
@click.pass_obj
def add_rectangle(painter, x1: float, y1: float, x2: float, y2: float) -> None:
    """
    Add a rectangle given the coordinates of two opposite vertices.
    
    Example usage:
    
    $ painter add-rectangle 0 0 5 5
    
    When a value is negative, it must be preceded by --, like this:
    
    $ painter add-rectangle 0 0 5 -- -5
    
    """
    rectangle = Rectangle(Point(x1, y1), Point(x2, y2))
    painter.add_shape(rectangle)
    click.echo("Rectangle added.")


@painter.command()
@click.pass_context
def list_shapes(ctx: click.Context) -> None:
    """List all shapes."""
    painter = ctx.obj
    if not painter.shapes:
        click.echo("No shapes added.")
        return
    for i, shape in enumerate(painter.shapes, start=1):
        click.echo(f"{i}. {shape}")

@painter.command()
@click.argument('shape_index', type=int)
@click.pass_obj
def draw_shape(painter, shape_index: int) -> None:
    """Draw a shape given its index when listed."""
    if shape_index < 0 or shape_index > len(painter.shapes):
        click.echo("Invalid shape index.")
        return
    shape = painter.shapes[shape_index - 1]
    click.echo("drawing shape...")
    shape.draw()


@painter.command()
@click.argument('shape_index', type=int)
@click.pass_obj
def area(painter, shape_index: int) -> None:
    """Calculate the area of a shape given its index when listed."""
    if shape_index < 0 or shape_index > len(painter.shapes):
        click.echo("Invalid shape index.")
        return
    shape = painter.shapes[shape_index - 1]
    click.echo(f"The area of the shape is {shape.area()}.")


@painter.command()
@click.pass_obj
def clear(painter) -> None:
    """Clear all shapes."""
    painter.clear()
    click.echo("Cleared all shapes.")
