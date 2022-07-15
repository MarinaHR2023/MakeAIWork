# MakeAIWork

## Projects

This repository contains sources to be used by python students. Directory <i>projects</i> contains the (re)sources:
<ul>
<li>p1, p2 and p3</i> containing
<i>cursus_materiaal</i> with a project description
</ul>

Directory <i>notebooks</i> contains Jupyter notebooks that can be used in Jupyter Lab. Directory <i>scripts</i> contains some example Python scripts. 

## Python AI Workspace Installation

### Clone the source code
To be able to use this repository and handover your code, you need to have remote access to Github.

<ol>

<li>

**Create an account at [Github](https://github.com)**

</li>

<li>

**Install [Git for Windows](https://gitforwindows.org/) (Windows only)**
Make sure you select "Checkout as-is, commit Unix-style line endings"

</li>

<li>

**Create a ssh key-pair token**

Start a (git) bash shell *and generate a secret key pair with your student email adress

```sh
ssh-keygen -t Ed25519 -C {your@student.email.com}
```

</li>

<li>

**Copy your <b>public</b> key to Github**

Enter the following in (git)bash to view the contents of you public key:
```sh
cat ~/.ssh/id_ed25519.pub
```
and copy this in the text area when adding a [new ssh key in GitHub](https://github.com/settings/ssh/new)

</li>

</li>

**Create a fork of this repository** 

</li>

</li>

**Clone your <b>fork</b>**

Ennter the following command in your (git)bash shell after replacing {your_github_username} with your Gihub username.
```sh
git clone git@github.com:{your_github_username}/MakeAIWork.git
```

</li>

<li>

**Add user to Git Config**

In order to commit and push your changes, you need identitify yourself. 

Open a (git)bash, enter directory MakeAIWork and run:
```bash
sh/git_config.sh {your_github_username} {your@student.email.com}
```

</li>

</ol>
### Install Docker
To be able to use Docker, Windows Subsystem for Linux (WSL) needs to be activated. 

<ol>

<li>

**Enable WSL2 (Windows only)**
Enter the following command in Windows Powershell:
```pwsh
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

</li>

<li>

**Enable the Virtual Machine Platform feature (Windows only)**
Enter the following command in Windows Powershell:
```pwsh
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

</li>

<li>

**Make WSL 2 Default (Windows only)**
Enter the following command in Windows Powershell:
```pwsh
wsl –set-default-version 2
```

</li>

<li>

**Download and install [Docker Desktop](https://desktop.docker.com) (Windows and MacOS)**
<br>
Check if you are able to use Docker by running the following in <b>(git) bash</b>
```sh
docker run hello-world
```
<li>

**Configure Docker Desktop to start when you login**

</li>

<li>

**Configure Docker Desktop to enable docker-compose**

</li>

</ol>

### Edit with Visual Studio Code
<ol>

<li>

Install [Visual Studio Code](https://code.visualstudio.com/). 

</li>

<li>

Start vscode with command from current directory.

Start a (git) bash shell and enter directory MakeAIWork, from there use the command <i>code</i> to start vscode.
```sh
cd MakeAIWork
code .
```

</li>

<li>

Install Live Share

Follow the instructions at [Collaborate with Live Share](https://code.visualstudio.com/learn/collaboration/live-share)

</li>

</ol>

## Python AI Workspace Usage
Students use a containerised Python environment running a [Docker](https://www.docker.com/) image. 

### Files available to the container
The project files are accessible in the containerised runtime environment by means of a bind mount between the current (host)directory project and/or notebooks on your laptop and <i>/home/student/project</i> and/or <i>/home/student/nontebooks</i> at the container instance.
<br>

***CAUTION***
<br>
You can remove both container and image without data loss but be aware that files removed from the container directory /project will also be removed from you host directory project.
<br>

### Start a Python container
Docker scripts can be found in <i>docker</i>. Each of the scripts below will call <i>docker/run/miw_container.sh</i> to facilitate the following runtimes:

<ul>

<li>

<b>REPL</b> (Read Evaluate Print Loop) modus to experimentally learn Python commands. Exit by pressing [Control+D].

```bash 
sh/python.sh
```

</li>

<li>

Start python with a <b>script</b> from directory <i>project</i>

```bash 
sh/python.sh scripts/lists/sum.py
```

</li>

<li>

Start <b>Jupyter Lab</b> to learn from the <i>notebooks</i> available at <i>project/notebooks</i>

```bash 
sh/jupyter.sh
```

</li>

<li>

Start container with an interactive <b>bash</b> (expert mode) to perform system operations

```sh
sh/bash.sh
```

### Docker artifacts
Each of the above scripts will call run/miw_container.sh which will spin up a container based on the latest version of 'jaboo/miw' which is either stored locally or will be fetched from available at [Dockerhub](https://hub.docker.com/repository/docker/jaboo/miw). 

Inspect locally stored images with
```sh
docker images
```

The containers will be removed automatically after being terminated. For overview of both running and terminated containers enter  
```sh
docker container
```

</li>

</ul>

### Removing Docker artifacts
Removing images and/containers will not cause data loss. After removing the image, Docker will pull a new instance when you start a container. 
Docker images and containers can be removed (if not done automatically) by running
```sh
run/clean_docker_artifacts.sh
```

---

### References
[How to Use Linux Terminal in Windows 10](https://allthings.how/how-to-use-linux-terminal-in-windows-10/)<br>
[Jupyter](https://jupyter.org/)
