# Pandoc intergraded

run this in Anaconda Powershell Prompt

```
pandoc --help

pandoc file.xx(support drag-and-drop) -o C:\Users\Administrator\Desktop\file.docx
```

# Import your own python files in Anaconda3 should follow this routine:

1. get path in iPython:

  >import sys 
  sys.path
  ['C:\\Users\\Administrator',
   'D:\\Administrator\\Anaconda3\\python37.zip',
   'D:\\Administrator\\Anaconda3\\DLLs',
   'D:\\Administrator\\Anaconda3\\lib',
   'D:\\Administrator\\Anaconda3',
   '',
   'D:\\Administrator\\Anaconda3\\lib\\site-packages',
   'D:\\Administrator\\Anaconda3\\lib\\site-packages\\win32',
   'D:\\Administrator\\Anaconda3\\lib\\site-packages\\win32\\lib',
   'D:\\Administrator\\Anaconda3\\lib\\site-packages\\Pythonwin',
   'D:\\Administrator\\Anaconda3\\lib\\site-packages\\IPython\\extensions',
   'C:\\Users\\Administrator\\.ipython']
 
 2. put your own python files here:
 
~\\Anaconda3\\lib\\site-packages
