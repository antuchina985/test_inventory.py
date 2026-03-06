import logging
import pathlib

audit_dir = pathlib.Path('logs')
audit_dir.mkdir(exist_ok=True)

log_file = audit_dir / 'suite.log'

logger = logging.getLogger("TalentoTech")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # ESTO DEBE ESTAR DENTRO DEL IF (4 espacios de sangría)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)