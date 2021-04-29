import gphoto2 as gp
import logging
import os
import subprocess
import sys

def getCamera():
    camera = gp.Camera()
    camera.init()
    return camera

def doCapture(camera):
	print('Capturing image')
	file_path = camera.capture(gp.GP_CAPTURE_IMAGE) #triggers capture
	print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
	target = os.path.join('/tmp', file_path.name)

	print('Copying image to', target)
	camera_file = camera.file_get(
		file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
	camera_file.save(target)
	camera.exit()
	return 0;

def configureCamera(camera):
	config = camera.get_config()
	print('Applying configuration')
	try:
		#execute gphoto2 --list-all-config to retrieve the abilities of your camera
		imgformat = config.get_child_by_name('imageformat')
		shutter = config.get_child_by_name('shutterspeed')
		iso = config.get_child_by_name('iso')
		aperture = config.get_child_by_name('aperture')
		af = config.get_child_by_name('autofocusdrive')
		
		imgformat.set_value("Large Fine JPEG")
		shutter.set_value("0.5")
		iso.set_value("100")
		aperture.set_value("8")
		af.set_value("1")
		
		camera.set_config(config) #this line writes the current configuration
		sleep(0.5) #possibly not neccesary when using MF instead of AF
	except:
		print ('Warning: camera not or incorrectly configured')

if __name__ == "__main__":
		camera = getCamera()
		configureCamera(camera)
		doCapture(camera)
