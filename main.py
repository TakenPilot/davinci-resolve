import os
import sys

resolve_script_api = os.environ.get('RESOLVE_SCRIPT_API')
resolve_script_lib = os.environ.get('RESOLVE_SCRIPT_LIB')

if resolve_script_api:
    print("RESOLVE_SCRIPT_API:", resolve_script_api)
    if not os.path.exists(resolve_script_api):
        print("Resolve scripting api does not exist.")
        sys.exit()
else:
    print("Resolve scripting api environment is not set.")
    sys.exit()

if resolve_script_lib:
    print("RESOLVE_SCRIPT_LIB:", resolve_script_lib)
    if not os.path.exists(resolve_script_lib):
        print("Resolve scripting lib does not exist.")
        sys.exit()
else:
    print("Resolve scripting lib environment is not set.")
    sys.exit()

# Setting environment variables
sys.path.append(os.environ['RESOLVE_SCRIPT_API'] + "/Modules")

# Path to the DaVinci Resolve scripting API modules
# resolve_script_api = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules"
# sys.path.append(resolve_script_api)


# Importing the DaVinci Resolve module
try:
    import DaVinciResolveScript as dvr_script
except ImportError as e:
    print(f"Could not import the DaVinciResolveScript module: {e}")
    sys.exit()

# Print debug information about the DaVinci Resolve Scripting API
print("DaVinci Resolve Scripting API")
print("Properties:", dvr_script)
print("Methods:", dir(dvr_script))
print("")
print("Instance:", dvr_script.scriptapp("Resolve"))
print("")

# Connecting to DaVinci Resolve
resolve = dvr_script.scriptapp("Resolve")
if not resolve:
    print("Cannot find an instance of DaVinci Resolve running")
    sys.exit()

print("Connected to DaVinci Resolve:", resolve)

project_manager = resolve.GetProjectManager()
project = project_manager.GetCurrentProject()

if not project:
    print("No project is currently open")
    sys.exit()

# Loop through each timeline
for timelineIndex in range(1, project.GetTimelineCount() + 1):
    timeline = project.GetTimelineByIndex(timelineIndex)

for clip in timeline.GetItemListInTrack('Video', 1):  # Assuming text is in Video track
    # Example to get the clip name
    clip_name = clip.GetName()
    
    # Depending on how text is added, extract it here
    # This can vary greatly based on your project specifics
    # For example:
    # text = clip.GetClipProperty("Title")
    # print(f"Clip: {clip_name}, Text: {text}")