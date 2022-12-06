# CPyProjectTemplate
Put a description for your project here!
This repo is a template VS code project for CircuitPython projects that automatically uploads your code to the board when you press F5. Requires F5Anything extension.
## Use
### Every new project:
1. Make a GitHub account if you don't have one with your normal school credentials and sign into it.
2. Click the big green Use This Template button at the top of this page.
3. Name the new repository something appropriate to the purpose of your project (Your first one should probably be named `CircuitPython`).
4. Hit "Create repository from template." (The default settings should be fine.)
5. Open VS Code on your machine. Click Clone Repository.
6. Paste in the link to the new repository you've just created from the template and hit enter.
7. For the location, select the "STUDENT" drive if you have it or the document folder if you don't.
8. Hit "Open Cloned Directory."
9. Install the reccomended extensions when you get that popup in the lower right corner.
### To commit from VS Code:
1. Go to the little branch icon in the left bar of VS Code.
2. Click the + icon next  to the files you want to commit.
3. Write a message that descibes your changes in the "Message" box and hit commit.
4. If you get an error about user.name and user.email, see the next section.
5. Click the "Sync changes" button.
### If you get an error about user.name and user.email
1. Open Git Bash from the Windows Search Bar.
2. FIlling in your actual information, run the following commands one line at a time. The paste shortcut is `Shift+Insert` or you can right click then hit paste. Spelling must match exactly:
```
git config --global user.name YOURUSERNAME
git config --global user.email YOURSCHOOLEMAIL
```
3. Return to step 3 of the previous section.
