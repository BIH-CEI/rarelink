from .config_utils import ONTOP_DIRECTORY, ONTOP_SH, ONTOBRIGE_PROPERTIES_SAVING, INDEX
import logging
import subprocess

def create_properties_file(jdbc_name, jdbc_url, jdbc_user, jdbc_password):

    properties_content = f"""
jdbc.name={jdbc_name}
jdbc.url={jdbc_url}
jdbc.user={jdbc_user}
jdbc.password={jdbc_password}
    """
    with open(ONTOBRIGE_PROPERTIES_SAVING, 'w') as file:
        file.write(properties_content)
        
def execute_ontop_materialize():
    try:
        logging.debug('Setting read/write permissions for the ONTOP directory.')
        subprocess.run(['chmod', '-R', '777', ONTOP_DIRECTORY], check=True)
        logging.debug('Permissions set successfully.')

        logging.debug('Listing the contents of the data/ directory.')
        subprocess.run(['ls', 'data/'], check=True)
        logging.debug('Contents listed successfully.')

        logging.debug(f'Executing ONTOP script: {ONTOP_SH}')
        subprocess.run(['sh', ONTOP_DIRECTORY + ONTOP_SH], check=True)
        logging.debug('Script executed successfully.')

    except subprocess.CalledProcessError as e:
        logging.error(f'Error executing a command: {e}')
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
