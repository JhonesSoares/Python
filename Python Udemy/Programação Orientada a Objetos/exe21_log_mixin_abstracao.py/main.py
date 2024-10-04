from log import Log
from log import LogFileMixin, LogPrintMixin

log_print = LogPrintMixin()
log_print.log_error('Qualquer coisa.')
log_print.log_success('Que Legal')