# geekbook (manifesto) - note taking system for nerds/geeks!

[![Documentation Status](https://readthedocs.org/projects/geekbook/badge/?version=latest)](http://geekbook.readthedocs.io/en/latest/?badge=latest)


  * [Features](#features)
    * [Index](#index)
    * [Dashboard](#dashboard)
  * [EMACS\-powered](#emacs-powered)
    * [focus\-mode](#focus-mode)
    * [list notes in Emacs (sort by Date/Name)](#list-notes-in-emacs-sort-by-datename)
    * [magit\-based diff of your notes](#magit-based-diff-of-your-notes)
  * [On your OSX](#on-your-osx)
  * [On your phone](#on-your-phone)
  * [Food for thought](#food-for-thought)
    * [Long notes vs short notes](#long-notes-vs-short-notes)
    
![](preview/qubCXZcWHl.gif)

A neat way how to combine **Emacs (not requried) + Markdown Syntax + Git + Html engine** (bootstrap/python) to get the best notes-talking experience ever. Highly customizable with plugins written in Python. What's the most important, under the hood it's just a set of Markdown files.. you can do with them whatever you want, e.g. you can Pandoc (http://pandoc.org/epub.html) them to epub (that's origin of "book" part of the name). 

Freatures:

- Index html based
- Sync them with Dropbox/iCloud/github
- Read from console, grep them
- Edit with almost any text editor, I'm using Emacs!
- Keep images separately, edit them in any external tool or edit them in batch
- Customize html templates
- You can sync notes in your system with notes kept at virtual machines (mounted via sshfs) or drives
- Super light!
- Pandoc markdown files to anything you want!
- Use 3rd party editors, if you wish, on your computer or on your phone.

I recommend to use **Emacs** (or VIM or other super-powerfull editor) to:

- run git on your notes in your editor,
- grep them in the editor,
- make bookmarks to parts of your notes,
- copy-paste from your notes to your programs you're writing,
- use Google Translate (https://github.com/atykhonov/google-translate)
- ispell,
- outline mode,
- focuse mode.

Sync with **Github** to have your notes (full-text searchable) with you all the time (in a private repository):

![index](docs/imgs/geekbookx.png)

Kinda similar projects:

- www.geeknote.me

# Features
## Index

![index](docs/imgs/index.png)

## Dashboard

![dashboard](docs/imgs/dashboard.png)

# EMACS-powered
## Focus on your notes

![](docs/imgs/emacs_focus_mode.png)

## List your notes in Emacs (sort by Date/Name)

![](docs/imgs/emacs_list.png)

## magit-based diff of your notes

![](docs/imgs/emacs_git.png)

[https://www.emacswiki.org/emacs/Magit](https://www.emacswiki.org/emacs/Magit)

# On your OSX

Spotlight your notes:

![](docs/imgs/osx_file.png)

# On your phone
On your phone: (in this case using Dropbox & Byword on my iPhone).

![](docs/imgs/notes_at_phone.png)

Or Draft (http://lifehacker.com/draft-is-a-clean-note-taking-app-with-markdown-support-844836670) for Android (not tested by me).

# Food for thought
## Long notes vs short notes

You can combine short notes into long ones.
