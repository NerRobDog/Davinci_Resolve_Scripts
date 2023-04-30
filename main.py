from python_get_resolve import GetResolve
import resolve_script as dvr_script
import sys
import timecoder as tcdr

resolve = dvr_script.scriptapp("Resolve")
pm = resolve.GetProjectManager()
proj = pm.GetCurrentProject()
tl = proj.GetCurrentTimeline()
mp = proj.GetMediaPool()
rootfolder = mp.GetRootFolder()
rootclips = rootfolder.GetClips()
ms = resolve.GetMediaStorage()
folder = mp.GetCurrentFolder()
clips = folder.GetClips()

mode = int(input("Choose mode\n"
                 "1. TC shifting\n"
                 "2. Add to Clip Name\n"))
input('Open folder in DVR and press Enter\n'
      'All files in this folder will accept the edit')


# TC shifting
if mode == 1:
    tc_operation = int(input("Choose operation\n"
                             "1. Add TCs\n"
                             "2. Sub TCs\n"))
    tc_shift = tcdr.remove_tc_format(input('Enter TC delta\n'
                                           'Format 00:00:00:00\n'))
    tc_type = int(input("1. Start TC\n"
                        "2. End TC\n"
                        "3. Slate TC\n"))
    print(tc_type)
    if tc_type == 1:
        tc_type = "Start TC"
    elif tc_type == 2:
        tc_type = "End TC"
    elif tc_type == 3:
        tc_type = "Slate TC"
    else:
        print("Wrong TC type")
        exit()
    fps = int(input('Enter file FPS\n'))
    for i in clips:
        in_tc = (clips[i].GetClipProperty(tc_type))
        print("File =", clips[i].GetClipProperty("Clip Name"))
        print("Input TC =", in_tc)
        tc_format = tcdr.remove_tc_format(in_tc)
        if tc_operation == 1:
            out_tc = tcdr.tc_add(tc_format, tc_shift, fps)
        elif tc_operation == 2:
            out_tc = tcdr.tc_sub(tc_format, tc_shift, fps)
        print("Out TC =", out_tc)
        clips[i].SetClipProperty(tc_type, out_tc)

# Add prefix or postfix
elif mode == 2:
    edit_type = int(input("1. Prefix\n"
                          "2. Postfix\n"))
    if edit_type == 1:
        add = input("Enter prefix\n")
    elif edit_type == 2:
        add = input("Enter postfix\n")
    else:
        print("Wrong edit type")
        exit()
    for i in clips:
        in_name = clips[i].GetClipProperty("Clip Name")
        print(in_name)
        in_name = in_name[-8::]
        print(in_name)
        in_name = add + in_name if edit_type == 1 else in_name + add
        print(in_name)
        clips[i].SetClipProperty("Clip Name", in_name)

else:
    print('Wrong mode')
    exit()
