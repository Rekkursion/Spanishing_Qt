import os


# the path of json-file of preferences
pref_json_file_path = './res/pref.json'

# the font-family for the interface
font_family = 'Microsoft YaHei UI'

# the attribution for using the icons from flaticon by freepik
icons_attribution_html_code = '<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>'

# the root-path of icons
__icons_root_path = './res/icons'

# the icon-path for more actions
more_actions_icon_path = os.path.join(__icons_root_path, 'more-options.png')

# the icon-path for the action of modification
modification_icon_path = os.path.join(__icons_root_path, 'pencil.png')

# the icon-path for the action of moving-up
moving_up_icon_path = os.path.join(__icons_root_path, 'up-arrow.png')

# the icon-path for the action of moving-down
moving_down_icon_path = os.path.join(__icons_root_path, 'down-arrow.png')

# the icon-path for the action of removal
removal_icon_path = os.path.join(__icons_root_path, 'trash-bin.png')
