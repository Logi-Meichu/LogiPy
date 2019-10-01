import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


# LED snippets
##############

# Set all device lighting to red
from logipy import logi_led
import time
import ctypes

print ('Setting all device lighting to red...')
logi_led.logi_led_init()
time.sleep(1) # Give the SDK a second to initialize
logi_led.logi_led_set_lighting(100, 0, 0)
raw_input('Press enter to shutdown SDK...')
logi_led.logi_led_shutdown()

# If you prefer the c/c++ style you can use the DLL directly
print ('Setting all device lighting to green...')
logi_led.led_dll.LogiLedInit()
time.sleep(1) # Give the SDK a second to initialize
logi_led.led_dll.LogiLedSetLighting(ctypes.c_int(0), ctypes.c_int(100), ctypes.c_int(0))
raw_input('Press enter to shutdown SDK...')
logi_led.led_dll.LogiLedShutdown()


# Arx snippets
##############

# Show a simple applet with the default callback
# note: will not work if a callback has already been defined by the process
from logipy import logi_arx
import time
print 'Setting up a simple applet...'
index = """
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1, target-densityDpi=device-dpi, user-scalable=no" />
        <link rel="stylesheet" type="text/css" href="style.css">
    </head>
    <body>
        <img id="splash-icon" src="https://o.aolcdn.com/images/dims?resize=2000%2C2000%2Cshrink&image_uri=https%3A%2F%2Fs.yimg.com%2Fos%2Fcreatr-uploaded-images%2F2019-08%2F20268ff0-bf39-11e9-abfe-ca68a355a645&client=a1acac3e1b3290917d92&signature=4721cae76b4dcfde3070f4429ac72bff9917b1c4" />
    </body>
    </html>
    """
css = """
    body {
        background-color: black;
    }
    img {
	    position: absolute;
	    top: 50%;
	    left: 50%;
	    width: 118px;
        height: 118px;
        margin-top: -59px;
        margin-left: -59px;
    }
    """
logi_arx.logi_arx_init('com.logitech.gaming.logipy', 'LogiPy')
time.sleep(1)
logi_arx.logi_arx_add_utf8_string_as(index, 'index.html', 'text/html')
logi_arx.logi_arx_add_utf8_string_as(css, 'style.css', 'text/css')
logi_arx.logi_arx_set_index('index.html')
raw_input('Press enter to shutdown SDK...')
logi_arx.logi_arx_shutdown()

# Show a simple applet with a custom callback
from logipy import logi_arx
import time
import ctypes

print 'Setting up a simple applet with custom callback...'
index = """
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1, target-densityDpi=device-dpi, user-scalable=no" />
        <style>
            body
            {
                background-image:url('https://o.aolcdn.com/images/dims?resize=2000%2C2000%2Cshrink&image_uri=https%3A%2F%2Fs.yimg.com%2Fos%2Fcreatr-uploaded-images%2F2019-08%2F20268ff0-bf39-11e9-abfe-ca68a355a645&client=a1acac3e1b3290917d92&signature=4721cae76b4dcfde3070f4429ac72bff9917b1c4');
                background-color: black;
                background-repeat:no-repeat;
                background-size: contain;
                background-attachment:fixed;
                background-position:center; 
            }

            h1
            {
                    color:rgb(255,255,255);
                    text-align:center;
            }
            h2
            {
                    color:rgb(255, 101, 0);
                    text-align:left;
            }
            #clickTestDiv
            {
                    color:rgb(3, 3, 3);
                    background-color:#9006a0;
                    text-align:left;
                    font-family: 'Oswald';
                    font-size: 20px;
                    width: 250px;
                    margin-left:auto;
                    margin-right:auto;
                    border:solid;
                    height:20%;
            }
            #childTest
            {
                width:70%;
                height:60%;
                margin-left: auto;
                margin-right:auto;
                text-align:center;
                background:red;
            }
            #progressbar {
              background-color: gray;
              border-radius: 13px; 
              padding: 3px;
            }

            #progressbarProgress {
               background-color: orange;
               width: 0%; 
               height: 20px;
               border-radius: 10px;
            }
            #randomImage
            {
                position:absolute;
                left:100px;
            }
            #firstButton {
                background-color: #21b55a;
                -moz-border-radius: 5px;
                -webkit-border-radius: 5px;
                border-radius:6px;
                color: #fff;
                font-family: 'Oswald';
                font-size: 40px;
                text-decoration:none;
                color:#0d0d0d;
                display:block;
                width: 300px;
                margin-left:auto;
                margin-right:auto;
                cursor: pointer;
                border:solid;
            }
            img { 
                color: red; 
                text-align: center; 
            }
            
        </style>
    </head>
    <script src="alert.js"></script>
    <body>
        <h1 id ="appletTitle"> Logitech Gamepanel App Sample</h1>
        <h2 class ="sectionTitle" id ="progressTitle">Progress Bar</h2>
        <div id="progressbar">
             <div id ="progressbarProgress"></div>
        </div>
        <br />
        <h2 class ="sectionTitle ignoreTapEvents" id ="imageTitle">Random image from bitmap</h2>
        <img src="randomImage.png" id="randomImage" alt="Load the image from bitmap from the sample"/><br /><br /><br /><br />
        <h2 class ="sectionTitle" id ="tapDemoTitle">Tap on tags demo</h2>
        <button id="firstButton">Click Me!</button> <br />
        <div id="clickTestDiv" class="ignoreTapEvents">parent Div - ignoring tap events <div id="childTest">child Div receiving tap events</div></div>
       
        <script>
            function moveRandomImage() {
                document.getElementById('randomImage').style.left = Math.floor((Math.random() * screen.width *0.6) + 1);
            }

            setInterval(function () { moveRandomImage() }, 1000);
        </script>
    </body>
</html>
    """
css = """
    body {
        background-color: black;
    }
    img {
	    position: absolute;
	    top: 50%;
	    left: 50%;
	    width: 118px;
	    height: 118px;
	    margin-top: -59px;
	    margin-left: -59px;
    }
    """
def custom_callback(event_type, event_value, event_arg, context):
    if event_arg and event_arg == 'splash-icon':
        print '\nNo wonder Logitech is called Logicool in Japan! They are so cool!'

logi_arx.logi_arx_init('com.logitech.gaming.logipy', 'LogiPy', custom_callback)
time.sleep(1)
logi_arx.logi_arx_add_utf8_string_as(index, 'index.html', 'text/html')
logi_arx.logi_arx_add_utf8_string_as(css, 'style.css', 'text/css')
logi_arx.logi_arx_set_index('index.html')
raw_input('Press enter to shutdown SDK...')
logi_arx.logi_arx_shutdown()
