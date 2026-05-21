from rich import print

def log_step(step, data):
    print(f"[cyan]STEP:[/cyan] {step}")
    print(f"[yellow]{data}[/yellow]\n")