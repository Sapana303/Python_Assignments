### 1. What is exception handling?

Exception handling is a way of handling errors that occur while a Python program is running. Instead of allowing the program to crash, we can use try, except, else, and finally to handle errors properly and continue or safely stop the program.

For example, if a user enters "abc" when the program expects a number, Python raises a ValueError. Exception handling allows us to catch this error and display a meaningful message.

### 2. Why should we use exception handling?

We should use exception handling to prevent unexpected errors from crashing the application.

If exceptions are not handled:

The program may terminate unexpectedly.
The user may see a confusing error message.
Important operations may not be completed.
The application may become unreliable.
Debugging problems can become more difficult.

Exception handling makes programs more reliable and user-friendly.

### 3. What is the difference between try and except?

The try block contains code that may cause an exception.

The except block handles the exception if one occurs in the try block.

Example:

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number.")

Here:

try → attempts to convert the input to an integer.
except → handles the ValueError if the conversion fails.

### 4. When is the else block executed?

The else block is executed only when no exception occurs in the try block.

Example:

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number.")
else:
    print("Number entered successfully.")

If the user enters 25, the else block executes.

If the user enters abc, the except block executes and the else block is skipped.

### 5. When is the finally block executed?

The finally block is executed whether an exception occurs or not.

It is commonly used for cleanup operations or actions that must happen at the end of processing.

Example:

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number.")
finally:
    print("Processing completed.")

The message "Processing completed." is printed whether the conversion succeeds or fails.

### 6. What is logging?

Logging is the process of recording important information about what happens inside a program.

Python provides the built-in logging module for this purpose.

Logging is useful because it can record:

Normal application events
Warnings
Errors
Exceptions
Detailed debugging information

Logs can be stored in a file such as student_app.log, allowing developers to investigate problems after the application has run.

### 7. What is the difference between print() and logging?

print() is mainly used to display information directly to the user on the console.

Logging is designed to record application events and errors for monitoring, debugging, and troubleshooting
| `print()` | Logging |
|---|---|
| Displays information on the console | Can write information to a log file |
| Mainly for user output | Mainly for application monitoring |
| No built-in severity levels | Has levels such as DEBUG, INFO, WARNING, ERROR, CRITICAL |
| Harder to control in large applications | Can filter messages by logging level |
| Usually temporary/debug output | Useful for maintaining a history of application events |

For example:

print("Invalid input.")

displays a message to the user.

Whereas:

logging.error("Invalid input received.")

records an error in the configured logging destination.

### 8. What happens when the logging level is set to ERROR? Which log levels will be recorded?

When the logging level is set to:

logging.basicConfig(
    filename="student_app.log",
    level=logging.ERROR
)

only messages with level ERROR or higher are recorded.

Therefore:

### Log Level	Recorded?
    DEBUG	      No
    INFO	      No
    WARNING	      No
    ERROR	      Yes
    CRITICAL	  Yes

This happens because logging levels have an order of severity. Setting the level to ERROR filters out messages that are less severe than ERROR.

### 9. What happens if we do not handle ValueError when converting user input using int()?

If invalid input is passed to int(), Python raises a ValueError.

For example:

number = int("abc")

causes:

ValueError

If the exception is not handled, the program can terminate and display a traceback.

Using:

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number.")

allows the program to handle the invalid input without crashing.

### 10. Why should we avoid using a broad exception handler such as except: pass?

We should avoid:

except:
    pass

because it catches almost every exception and then silently ignores it.

This can hide serious programming errors and make debugging very difficult.

For example:

try:
    number = int(input("Enter number: "))
except:
    pass

If something goes wrong, the program gives no indication that an error occurred.

It is better to catch specific exceptions:

except ValueError:
    print("Please enter a valid number.")

This makes the program safer, clearer, and easier to debug.

### 11. Why is logging useful in a production application?

Logging is useful in production because developers usually cannot watch the application directly while users are using it.

Logs provide a record of what happened in the application.

They can help developers:

Identify errors and exceptions
Understand application behavior
Investigate failures
Monitor important events
Troubleshoot problems
Find the cause of unexpected behavior

For example, if a production application fails, an error such as:

ERROR: Database connection failed.

in the log can help developers identify the problem.

### 12. What is the purpose of the finally block?

The purpose of the finally block is to execute code that should run regardless of whether an exception occurs.

It is commonly used for cleanup or final processing tasks.

Example:

try:
    # code that may cause an exception
except ValueError:
    # handle exception
finally:
    print("Processing completed.")

In our Student Result Processing System, the finally block is used to display:

Processing completed.

This message is displayed whether the student processing succeeds or an exception occurs.

Therefore, finally is useful when an action must happen at the end of processing regardless of the result.
