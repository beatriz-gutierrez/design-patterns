from logger import Logger

logger1 = Logger()
logger2 = Logger()

logger1.write_log("Log message 1")
print(logger2.read_log())

print(logger1 is logger2)