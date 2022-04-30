# Tutorial 1 - setuid programs
## User Membership
    $ whoami
    $ groups
    $ id
    $ getent <database> <key>
    - get entries from <database> with <key>
    - getent passwd seed
    - getent group seed
## Process Membership
- effective, real, saved uid or gid
## File Access Control
    $ ls -l <file>
-rw-rw-r-- 1 seed seed 761 Dec 27  2020 cap_leak.c

## Directory Access Control
    $ ls -l Setuid
total <total_num_blocks_occupied>
-rw-rw-r-- 1 seed seed 761 Dec 27  2020 cap_leak.c
-rw-rw-r-- 1 seed seed 471 Feb 19  2021 catall.c
lrwxrwxrwx 1 seed seed  10 Apr  9 12:35 exploit.txt -> secret.txt
-rw-rw-r-- 1 seed seed 180 Dec 27  2020 myenv.c
-rw-rw-r-- 1 seed seed 418 Dec 27  2020 myprintenv.c
-rw-r--r-- 1 root root  17 Apr  9 12:36 secret.txt
-rw-rw-r-- 1 seed seed 258 Apr 27 15:21 tutorial_setuid.md

## Changing Permission Modes
1. chmod: the owner of a file or directory can change its permission bits
- relative form:
    $ chmod g+w file           # allow write by group members
    $ chmod a+x file           # allow execute by all (user+group+others)
    $ chmod ug+x,o-rwx file    # user+group can execute, deny all for others
- octal form
    $ chmod 0664 file          # mode rw-rw-r--
- absolute form:
    $ chmod u=rw, go=r file

    $ chmod g+s file           # set setgid bit
    $ chmod +t /tmp            # set sticky bit, only owner of file/directory can remove/rename
    $ ls -ld /tmp
    drwxrwxrwt 6 root root 4096 Apr 20 18:54 /tmp
2. chgrp: the owner of a file or directory can change its group to one which the owner is a member
    $ chgrp <group> <file>
3. chown: only the root (with uid 0) can change the owner of a file or directory
    $ chown <user>:<group> <file>
4. mode & ~umask: umask is used to disable default permissions in mode of a file
	              mode = 0666(rw-rw-rw-) for file and mode = 0777 for directory, 
				  set umask, then newly created file/directory will have permission mode & ~umask
$ umask 0022 # rw-r--r-- no write access for group+others
$ umask 0007 # rw-rw---- no access for others

# setuid & setgid for elevated rights
$ sudo chmod 4755 secret.txt
$ ls -la secret.txt 
-rwsr-xr-x 1 root root 17 Apr  9 12:36 secret.txt

# find all setuid root programs
$ find . -user root