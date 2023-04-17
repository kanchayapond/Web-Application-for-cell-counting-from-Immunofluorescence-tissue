import logging
import os
from datetime import datetime, timedelta

def setup_logging():
    # Create the log directory if it does not exist
    log_dir = 'logs/' # replace with the absolute path to your log directory
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Set up the logger
    log_filename = datetime.now().strftime('%Y-%m-%d.log')
    log_path = os.path.join(log_dir, log_filename)
    print('Logging to {}'.format(log_path))
    logging.basicConfig(filename=log_path, level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # Clean up old log files (older than 3 months)
    for filename in os.listdir(log_dir):
        file_path = os.path.join(log_dir, filename)
        if os.path.isfile(file_path):
            file_creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
            if datetime.now() - file_creation_time > timedelta(days=90):
                os.remove(file_path)

    return logging

def check_pwd():
    return os.getcwd()

def tree(startpath):
    result = ''
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        result += '{}{}/\n'.format(indent, os.path.basename(root))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            result += '{}{}\n'.format(subindent, f)
    return result


if __name__ == '__main__':
    logger = setup_logging()
    logger.info('This is an example action')
    logger.info('This is another example action')

