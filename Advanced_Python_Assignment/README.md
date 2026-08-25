### 1. Iterator

iter(employees) obtains an iterator from the iterable employees. next(iterator) retrieves the next item from that iterator. When there are no more items, next() raises StopIteration.

### 2. Generator

yield is preferred for very large datasets because it produces values lazily, one at a time, instead of creating and storing the complete result in memory. This reduces memory usage and allows data to be processed incrementally.

### 3. Generator vs Iterator

Yes, a generator is an iterator. A generator automatically implements the iterator protocol and provides values one at a time using yield. A custom iterator requires explicitly implementing __iter__() and __next__().

### 4. Closure

check() remembers min_salary because min_salary is a variable from its enclosing scope. When the inner function is returned, Python preserves access to that variable. Therefore, even after create_salary_filter() finishes, check() can still use the original min_salary value.

### 5. Decorator
@log_execution
def generate_report():
    ...

is approximately equivalent to:

def generate_report():
    ...

generate_report = log_execution(generate_report)

The decorator receives the original function and returns a wrapped version that adds additional behavior such as logging.

### 6. Context Manager

A context manager is better than manually opening and closing a file because it automatically handles resource cleanup. With ReportFile, __enter__() opens the file and __exit__() closes it automatically when the with block finishes. This makes the code safer and easier to maintain.