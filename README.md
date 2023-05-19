<img src='res/logo.png' width='500'></img>

# Table of Contents

[Introduction](https://github.com/zuckung/test3/blob/main/README.md#introduction) 
 
[Download Information](https://github.com/zuckung/test3/blob/main/README.md#download-information)  
- [Downloading Alternative](https://github.com/zuckung/test3/blob/main/README.md#downloading-alternative)  
- [Notes](https://github.com/zuckung/test3/blob/main/README.md#notes)  
- [Known Plugin Issues](https://github.com/zuckung/test3/blob/main/README.md#known-plugin-issues)  

[Contribution](https://github.com/zuckung/test3/blob/main/README.md#contribution)  
- [Regarding Plugin Informations](https://github.com/zuckung/test3/blob/main/README.md#regarding-plugin-informations)  
- [Add your Plugin](https://github.com/zuckung/test3/blob/main/README.md#add-your-plugin)  

[Plugin Download](https://github.com/zuckung/test3/blob/main/README.md#plugin-download)  
- [Cheats](https://github.com/zuckung/test3/blob/main/README.md#cheats)  
- [Gameplay](https://github.com/zuckung/test3/blob/main/README.md#gameplay)  
- [Graphics](https://github.com/zuckung/test3/blob/main/README.md#graphics)  
- [Outfits](https://github.com/zuckung/test3/blob/main/README.md#outfits)  
- [Overhauls](https://github.com/zuckung/test3/blob/main/README.md#overhauls)  
- [Overwrites](https://github.com/zuckung/test3/blob/main/README.md#overwrites)  
- [Patches](https://github.com/zuckung/test3/blob/main/README.md#patches)  
- [Races](https://github.com/zuckung/test3/blob/main/README.md#races)  
- [Ships](https://github.com/zuckung/test3/blob/main/README.md#ships)  
- [Story](https://github.com/zuckung/test3/blob/main/README.md#story)   
- [Weapons](https://github.com/zuckung/test3/blob/main/README.md#weapons)  
- [Uncategorized](https://github.com/zuckung/test3/blob/main/README.md#uncategorized)  

---

# Introduction

A comprehensive library of 468 ancient and new plugins for the open-source game Endless Sky.

---

# Download Information

All plugins can get downloaded directly as zip-files from this page.

## Downloading Alternative

Third party tool such as [https://download-directory.github.io](https://download-directory.github.io/) can download a single folder/plugin. Paste the url to the folder url into that tool and you will be given a .zip for that folder.

For example, for the "50 cal" plugin, enter: [https://github.com/Hecter94/EndlessSky-PluginArchive/tree/main/Working/All%20Plugins/50%20cal](https://github.com/Hecter94/EndlessSky-PluginArchive/tree/main/Working/All%20Plugins/50%20cal)

Github by default only allows the entire library to be downloaded as a single .zip. Github may have issues with downloading very large file sizes, a possible workaround is using Github Desktop or Git Bash to clone the repository.

## Notes

- "Working" directory – plugins updated to work with the continous build of Endless Sky
- "Originals" directory – archived copies of original plugins
- "Nonfunctional" directory – plugins that will not function without updates

## Known Plugin Issues

<details>

### A Galaxy Far Far Away, Businessman Mod, Endless Depth, Normandy

Title screen missing/corrupted. override the title screen, using one or more of these can cause issues with it looking corrupted or "missing". Recommend to use one of these at a time, OR delete title.png from \images to restore the vanilla title screen

### Civil War, Edge of Endless, Jump to Lightspeed and Star Wars

all edit the vanilla interface, this can also cause issues and can only be fixed by editing/removing the interfaces.txt file in the plugin.

### A Wonderful Worldship

Random sprites replaced by worldships Culprit: Intended Behavior of "A wonderful worldship mod"

### Bare Ships

clears all ships from shipyards, meaning only bare versions of ships will be available, any plugins adding other ships not to custom shipyards will likely be incompatible

### Elite Sky

creates an Interceptor "bay type" which seems to make any interceptor escort jump around randomly.

### Final Frontier

sets every government swizzle to 0, also has an image named raider which conflicts with vanilla korath raider.

### Star Wars

includes a copy of vanilla data files and will likely conflict with any missions added/changed since it was created. Specifically known to conflict with changes to the Remnant storyline.

Star Wars has an image named fury which conflicts with vanilla fury.

### Recovery Ships

NPC Ships unable to assist with fuel or repairs Culprit: Likely an old version of Recovery Ship, updated 2/8/2022. Please let me know if you still see the issue.

Escorts from missions not spawning correctly Culprit: use the “safe” variant of this plugin to fix this behavior, “safe” version ships can only carry "Fighter" from vanilla and "Heavy Fighter" and "Gunship"

### The Station of Dr. Rousseau

"Bounty" Arfecta is spawned directly outside starting location. Culprit: , Mission: "Puzzle 3". No location is defined so Arfecta is spawned on first "landing".

"Hunt Dread Pirate Roberts" mission offers everywhere due to a lack of a source filter

### Edge of Endless

Overrides Luxury Accommodations and give it much higher space, bunks, and crew requirement, might make some ships that comes with it appears to have negative space and/or bunks.

Ship "Colossus" conflicts with a ship of the same name from Adamas

### Adamas

Ship "Colossus" conflicts with a ship of the same name from Edge of Endless

### ES-Restock

Gatling gun texture has empty space at 200px tall, resultuing in the outfit display being 10px lower than others

### Akasha Chronicles

Ship "Seraphim" conflicts with a ship of the same name from AES Irm

### AES Irm*

Ship "Seraphim" conflicts with a ship of the same name from Akasha Chronicles

### Mata

Ship "Spectre" conflicts with a ship of the same name from Alterra

### Alterra

Ship "Spectre" conflicts with a ship of the same name from Mata

Ship "Gladius" conflicts with a ship of the same name from Eternals

### Eternals

Ship "Gladius" conflicts with a ship of the same name from Alterra

</details>

---

# Contribution

## Regarding Plugin Informations

As you may have noticed some plugins miss infos. That ranges from missing author name to full description, or just if it is still playable on the current Endless Sky version. 

Please help updating these, by either posting in discussions area or by doing a Pull Request changing the files in `/res/pluginlist/`. 
Thanks.

## Add your plugin

You want your plugin here? Fork this repository, upload your plugin and make a Pull Request. Beside that you can post it in the discussion area.

For Pull Requests... the folder structure has changed with this update. There are no more category folders for you to upload to. Instead you create a file with the plugin informations in `/res/pluginlist/` and your plugin at `Working/All Plugins`, so this README.md can get auto-generated by a script.

---

# Plugin Download

All Plugins (468)

[Cheats](https://github.com/zuckung/test3/blob/main/README.md#cheats) (36) | [Gameplay](https://github.com/zuckung/test3/blob/main/README.md#gameplay) (35) | [Graphics](https://github.com/zuckung/test3/blob/main/README.md#graphics) (17) | [Outfits](https://github.com/zuckung/test3/blob/main/README.md#outfits) (35)<br>
[Overhauls](https://github.com/zuckung/test3/blob/main/README.md#overhauls) (38) | [Overwrites](https://github.com/zuckung/test3/blob/main/README.md#overwrites) (1) | [Patches](https://github.com/zuckung/test3/blob/main/README.md#patches) (3) | [Races](https://github.com/zuckung/test3/blob/main/README.md#races) (64)<br>
[Ships](https://github.com/zuckung/test3/blob/main/README.md#ships) (116) | [Story](https://github.com/zuckung/test3/blob/main/README.md#story) (60) | [Weapons](https://github.com/zuckung/test3/blob/main/README.md#weapons) (40) | [Uncategorized](https://github.com/zuckung/test3/blob/main/README.md#uncategorized) (23)<br>



---

## Cheats

<p>36 plugins in this category.<p>

<details>

 

---

### AES Omnis


[AES.Omnis.zip](https://github.com/zuckung/test3/releases/download/Latest/AES.Omnis.zip) | 0.32 kb | 2023-05-15 | [view files](https://github.com/