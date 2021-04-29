Small project that aims to acquire a picture from any DSLR camera via PTP mode, and identify/label blobs in the picture.
Should work with any DSLR that matches the right model and abilities.

Requires python library for gphoto2 and opencv.

Configuration can be checked with `gphoto2 --list-config`

Supported models can be seen with `gphoto2 --list-cameras`

Please note that the camera must be set on full manual mode, and that the script sets the aperture, shutterspeed and ISO from the listed configuration. You may want to adjust these settings depending on the environment.

Tested with Canon EOS 450D 
