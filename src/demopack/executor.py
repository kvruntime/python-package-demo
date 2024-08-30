import typer

app = typer.Typer()


@app.command()
def greet():
    print("greeting")
    return None


@app.command(name="hello")
def hello(name: str):
    print(f"hello {name}")
    return None
