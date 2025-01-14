import typer
import subprocess
from rarelink.cli.utils.string_utils import success_text

app = typer.Typer()

@app.command()
def restart_dockers():
    """
    CLI Command to stop, remove, and restart all relevant Docker containers.
    """
    typer.echo("Stopping all running containers...")
    subprocess.run(["docker", "stop", "$(docker ps -q)"], shell=True)
    
    typer.echo("Removing all stopped containers...")
    subprocess.run(["docker", "rm", "$(docker ps -a -q)"], shell=True)
    
    typer.echo("Restarting necessary containers...")
    # Replace with commands to start your containers
    subprocess.run(["docker-compose", "up", "-d"], check=True)
    success_text("✅ All containers restarted successfully.")