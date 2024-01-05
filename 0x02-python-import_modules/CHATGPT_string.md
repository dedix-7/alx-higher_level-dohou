What you're experiencing is related to how Python searches for modules and how module caching works. Let's break down the behavior step by step:

1. **Original file (`test.py`):**
   ```python
   #!/usr/bin/python3
   import string
   print(dir(string))
   ```

   When you run this script, it imports the `string` module and prints the list of attributes (names) in the `string` module.

2. **Renamed file (`string.py`):**
   ```python
   #!/usr/bin/python3
   import string
   print(dir(string))
   ```

   When you rename the file to `string.py` and run it, Python will first look in the current directory for a file named `string.py` before looking in the standard library. So, it imports the local `string.py` file instead of the standard `string` module. This is why you see a reduced list of attributes; it only reflects what is defined in your local file.

   Additionally, after you execute the script, Python caches the imported modules in memory to avoid reloading them unnecessarily. This cache is based on the module name. Since the name `string` is now associated with your local file, subsequent imports of `string` will refer to your file rather than the standard library module.

3. **Subsequent executions:**
   ```python
   #!/usr/bin/python3
   import string
   print(dir(string))
   ```

   Even after you rename the file back to `test.py`, when you run it again, Python still uses the cached version of the `string` module (your local file). The cache is persistent across executions.

To avoid this issue, you should choose a different name for your script that doesn't conflict with standard library modules. Using names that are already used by Python standard libraries can lead to unexpected behavior, as you've observed.
