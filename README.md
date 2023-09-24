# Item-Counter
An item counter for Breath of the Wild/Tears of the Kingdom 100% speedruns.

## Requirements
Needs some form of Python installed (ideally latest)

## Usage
Double-click to open the file, type by the > symbol to change items. If you can't see some of the parts, scroll up and they should be there.

Any changes made are saved automatically to a `save` file in the same folder as the .py script so it's recommended to separate the BOTW and TOTK scripts to avoid conflicts, as is done with the current file setup

## BOTW Counter Commands

### Item Commands

These are the counter prefixes used. Place them at the **start** of the command:

`o` confirms you have an item of that type. `o core3` confirms you can get Stasis+ and `o core5` confirms you can get the Ancient Short Sword. You can also use `o [weapon]` or `o [picture]` to confirm pictures.

(NOTE: This part below only relevant to the Granatus rupee printer route. If you're not using that route, you can ignore this bit of the program.)

`p` sets your part combination of 6 types, `Co` for cores, `ShGe` for shafts + gears, `ShSc` for shafts + screws `ShSp` for shafts + springs, `ShScSp` for shaft screws and springs, and `Sh` for shafts. 
This affects what pictures can be confirmed, as some combinations don't give enough parts to buy the Compendium pictures later on in the run. 

`h`, `c`, `f` and `s` all increment horns, claws, fangs and scales respectively, to be used with the `n`, `d` and `f` tags for Naydra, Dinraal and Farosh dragons.

### General Commands

`n [something]` is a way to write a note down for whatever reason, such as needing an extra item because you lost one or used it by accident.

`expand` is to reveal completed categories that are otherwise hidden

`core` is to add a core to the total core count, can be used instead of `core3` and `core5`.

`hide` is to hide the help options (where this information is on the program.

`reset` is to reset all values back to 0 as if the run has re-started.

`exit` is to exit the application

## TOTK Counter Commands

[TODO]
