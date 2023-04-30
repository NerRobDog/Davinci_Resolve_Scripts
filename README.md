# Davinci Resolve Scripts

This is a small set of scripts to facilitate editing and logging. Makes it easier to work
with a large number of files.

## **Supported distributions**

- Mac OS
- Windows
- Ubuntu

## Requirements

- Davinci Resolve Studio 16 or newer
- Python 3 (3.11 or less recommended)

Does not support newer version of python for now because of usage imp module, it should be replaced with importlib in future.
    

## Installation

- Clone this repository
- Check the PYTHONPATH is set correctly for import statement to work
- (For windows) Check the PYTHONHOME is set correctly too
## Functions
At the moment there are two functions for which I created this script

- Timecode shifting

  This function was created for manual sync cameras by timecode. 
  In Davinci Resolve you can automaticly sync multiple cameras by based on timecode included in the file.
  But in situations when timecode was not synced on production it's useless.
  My script allow you to shift timecode of selected files (forward or backward) to make them synced.
  For more detailed instructions check the **Usage** box
  
- Add to Clip Name

  This function helps you to organize your Media pool.
  You can add prefix or postfix to all Clip Names in folder.
  More detailed instructions with examples in **Usage** box

## Usage
### Start
Run the main.py in the python console and follow the instructions
### Timecode shifting
In timecode shifting mode you can add or sub time from the timecode in the Davinci Resolve media pool. 
This operation does **NOT** affect the timecode of the original files, it only change label to file created by Davinci.
All files have got included Start, End and Slate timecode (TC). By default Start TC is 00:00:00:00 (Hour:Minutes:Seconds:Frames), 
End TC is Start TC + file duration.
For example, if file duration is 1 minute, End TC will be 00:01:00:00.
Slate TC exist only inside Davinci Resolve it's additional timecode created for editors to mark cinema slate clap in files, 
you can use it whatever you want, Slate TCs doesn't affect anything.

**Example of usage**

You've got 3 files named frst.mov, scnd.mov and thrd.mov. It's files from 3 cameras (angles) and it was recorded at the same time.

This files's timecodes is 00:00:00:00, 00:10:00:00 and 10:00:00:00 respectively.
In Davinci Resolve you've got 3 ways to sync this files.
- By the waveforms (based on sound of clip)
- By the markers (based on markers you manually placed in clip in Davinci)
- By the clip start (if all cameras start record at the same time)
- By the timecode (based on timecode imported from original files)

This script add the new way to sync.
If all of your cameras recorded with FreeRun TC (google it), you can manually set timecode to sync point (for example slate clap).
You watched these clips and saw that in the frst clip the slate claped on the timecode 
00:00:05:00, 
in the scnd on the 00:12:00:00, 
in the thrd on the 10:01:00:00, 
this means what in the frst clip, 5 seconds have passed, from the beginning to the slate clap, in scnd have passed 2 minutes, and 1 minute in thrd.

00:00:00:00 -> 00:00:05:00 = 5 seconds

00:10:00:00 -> 00:12:00:00 = 2 minutes

10:00:00:00 -> 10:01:00:00 = 1 minute

To make clips synced you need to set the same timecode of slate clap in all this clips. 

For example from scnd.mov -> 00:10:00:00.

To do this we should shift timecode of the slate clap in the frst.mov from 00:00:05:00 to 00:10:00:00, 
it means you need to add (shift forward) to 00:00:05:00 timecode 00:09:55:00.

00:00:05:00 + 00:09:55:00 = 00:10:00:00

Now timecode of slate clap in frst and scnd is 00:10:00:00

For the thrd.mov we should shift timecode from 10:00:00:00 to 00:10:00:00,
it means you need to substract (shift backward) from 10:00:00:00 timecode 09:50:00:00.

10:00:00:00 - 09:50:00:00 = 00:10:00:00

Now all of your clips can be synced based on new timecode 

### Add to Clip Name

If you've got multiple files with similar names (/folder1/C0001.mp4,/folder2/C0001.mp4), 
and need to merge this folders, you can add some **prefix** or **postfix** to this files (/folder1/Prefix_C0001.mp4_Postfix).
Now you can merge this foldes without issues.
