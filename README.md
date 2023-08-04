# Instructions

1. Put the folder you have of the images in the directory. The folder should have BRIGHTFIELD, MERGE, GFP. If it doesn't, that's okay it just needs folders of images so if one of the folders is named PSUEDO then it would still work.

2. After you add your folder to the top folder, you now need to run 5 steps from your terminal
```
$] cd ~/Documents/
$] git clone https://github.com/a-v-kumar/EXP_Images.git
$] cd ~/Documents/EXP_Images/ && python3 make_readme.py && git status && git add -A && git commit -m "Adding images" && git push
$] rm -rf ~/Documents/EXP_Images/
```
Now, when you go to your github repo, you'll have all the images under the folder you had originally added in a nice and neat way.

### Example
For you to share this neat format with others just take the link like this one https://github.com/a-v-kumar/EXP-22.2/tree/master/exp22-2_8_2_23_24hrs_infection_astro_all/
