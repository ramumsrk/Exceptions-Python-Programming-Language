#! /usr/bin/python3.12

from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S.%s",
  filemode='+a',
  filename=F"{Path(__file__).parent.parent}/logs/ZeroDivisionError_demo.log"
)
if __name__ == '__main__':

  dividend: int = int( input( 'Enter first number: ' ) )
  divisor: int = int( input( "Enter second number: " ) )

  try:
    dividend/divisor
  except ZeroDivisionError as zeroDivisionError:
    logging.error(f'{zeroDivisionError=}')
  finally:
    logging.debug(
      f'{dividend}/{divisor} is {dividend/divisor}'
    )