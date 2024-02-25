from selenium import webdriver

# Get the DevTools URL
devtools_url = "http://localhost:9222/json"

# Create a ChromeOptions instance
options = webdriver.ChromeOptions()

# Connect to an already running Chrome browser
options.debugger_address = "localhost:9222"
driver = webdriver.Chrome(options=options)

# Now you can use 'driver' to interact with the already opened Chrome browser
breakpoint()